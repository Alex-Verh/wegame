export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();
  const result = await db
    .delete(tables.parties)
    .where(
      and(
        eq(tables.parties.id, id),
        user.isSuperuser ? undefined : eq(tables.parties.leaderId, user.id)
      )
    )
    .returning();
  if (result.length !== 1) {
    throw deletionError;
  }

  return result[0];
});
