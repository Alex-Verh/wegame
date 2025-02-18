export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();
  const result = await db
    .delete(tables.applications)
    .where(
      and(
        eq(tables.applications.id, id),
        user.isSuperuser ? undefined : eq(tables.applications.authorId, user.id)
      )
    )
    .returning();
  if (result.length !== 1) {
    throw deletionError;
  }

  return result[0];
});
