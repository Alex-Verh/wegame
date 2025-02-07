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
        members: z.record(
          z.coerce.number(),
          z.enum(["accepted", "pending"]).nullable()
        ),
      })
      .partial().parse
  );

  const db = useDB();

  let members: { partyId: number; status: "pending" | "accepted" }[] = [];
  if (updatedParty.members) {
    const membersToInsert = [];
    for (const memberId in updatedParty.members) {
      if (updatedParty.members[memberId])
        membersToInsert.push({
          userId: Number(memberId),
          partyId: id,
          status: updatedParty.members[memberId],
        });
      else
        await db
          .delete(tables.partyMembers)
          .where(
            and(
              eq(tables.partyMembers.userId, Number(memberId)),
              eq(tables.partyMembers.partyId, id)
            )
          );
    }
    if (membersToInsert.length)
      await db.insert(tables.partyMembers).values(membersToInsert);

    members = await db.query.partyMembers.findMany({
      where: eq(tables.partyMembers.partyId, id),
      columns: {
        userId: false,
      },
    });
    delete updatedParty.members;
  }

  const [party] = updatedParty
    ? await db
        .update(tables.parties)
        .set(updatedParty)
        .where(
          and(eq(tables.parties.id, id), eq(tables.parties.leaderId, user.id))
        )
        .returning()
    : [{}];

  return { ...party, members };
});
