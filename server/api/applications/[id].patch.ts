export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );
  const updatedApplication = await readValidatedBody(
    event,
    z
      .object({
        text: z.string(),
        ranking: z.string(),
        gameId: z.number(),
        platformId: z.number(),
      })
      .partial().parse
  );

  const db = useDB();
  const [application] = await db
    .update(tables.applications)
    .set(updatedApplication)
    .where(
      and(
        eq(tables.applications.id, id),
        eq(tables.applications.authorId, user.id)
      )
    )
    .returning();

  if (!application) {
    throw forbiddenError;
  }
  return application;
});
