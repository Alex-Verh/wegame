export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );
  const updatedParty = await readValidatedBody(
    event,
    z
      .object({
        title: z.string(),
        description: z.string(),
        gameId: z.number(),
        platformId: z.number(),
        minAge: z.number(),
        maxAge: z.number(),
        membersLimit: z.number(),
        discordLink: z.string(),
        members: z.record(
          z.coerce.number(),
          z.enum(["accepted", "pending", "denied"]).nullable()
        ),
      })
      .partial().parse
  );

  const db = useDB();

  let members: {
    partyId: number;
    status: "pending" | "accepted";
  }[] = [];
  if (updatedParty.members) {
    const membersToInsert: {
      userId: number;
      partyId: number;
      status: "pending" | "accepted";
    }[] = [];
    const leaderId = await db.query.parties.findFirst({
      where: eq(tables.parties.id, id),
      columns: { leaderId: true },
    });
    for (const memberId in updatedParty.members) {
      switch (updatedParty.members[memberId]) {
        case "pending":
          membersToInsert.push({
            userId: Number(memberId),
            partyId: id,
            status: "pending",
          });
          break;
        case "accepted":
          if (leaderId?.leaderId === user.id) {
            membersToInsert.push({
              userId: Number(memberId),
              partyId: id,
              status: "accepted",
            });
          }
          break;
        case "denied":
          if (leaderId?.leaderId === user.id) {
            await db
              .delete(tables.partyMembers)
              .where(
                and(
                  eq(tables.partyMembers.userId, Number(memberId)),
                  eq(tables.partyMembers.partyId, id)
                )
              );
          }
          break;
      }
    }
    if (membersToInsert.length)
      await db
        .insert(tables.partyMembers)
        .values(membersToInsert)
        .onConflictDoUpdate({
          target: [tables.partyMembers.userId, tables.partyMembers.partyId],
          set: { status: sql`excluded.request_status` },
        });

    members = await db.query.partyMembers.findMany({
      where: eq(tables.partyMembers.partyId, id),
      columns: {
        userId: false,
      },
    });
    delete updatedParty.members;
  }

  if (Object.keys(updatedParty).length > 0) {
    const result = await db
      .update(tables.parties)
      .set(updatedParty)
      .where(
        and(
          eq(tables.parties.id, id),
          user.isSuperuser ? undefined : eq(tables.parties.leaderId, user.id)
        )
      )
      .returning();
    if (result.length !== 1) {
      throw forbiddenError;
    }
    return { ...result[0], members };
  }

  return {
    ...(await db.query.parties.findFirst({ where: eq(tables.parties.id, id) })),
    members,
  };
});
