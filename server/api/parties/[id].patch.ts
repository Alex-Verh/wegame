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
      })
      .partial().parse
  );

  const db = useDB();
  const [party] = await db
    .update(tables.parties)
    .set(updatedParty)
    .where(and(eq(tables.parties.id, id), eq(tables.parties.leaderId, user.id)))
    .returning();

  if (!party) {
    throw forbiddenError;
  }
  return party;
});
