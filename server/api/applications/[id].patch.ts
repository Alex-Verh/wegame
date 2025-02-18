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

  if (!updatedApplication) {
    throw validationError;
  }

  const result = await db
    .update(tables.applications)
    .set(updatedApplication)
    .where(
      and(
        eq(tables.applications.id, id),
        user.isSuperuser ? undefined : eq(tables.applications.authorId, user.id)
      )
    )
    .returning();

  if (result.length !== 1) {
    throw forbiddenError;
  }
  return result[0];
});
