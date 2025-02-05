export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();
  const [party] = await db
    .delete(tables.parties)
    .where(and(eq(tables.parties.id, id), eq(tables.parties.leaderId, user.id)))
    .returning();
  return party;
});
