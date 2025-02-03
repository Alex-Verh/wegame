export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();
  const [application] = await db
    .delete(tables.applications)
    .where(
      and(
        eq(tables.applications.id, id),
        eq(tables.applications.authorId, user.id)
      )
    )
    .returning();
  return application;
});
