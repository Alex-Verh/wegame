export default defineEventHandler(async (event) => {
  const { userId, gameId, platformId } = await getValidatedQuery(
    event,
    z.object({
      userId: z.coerce.number().optional(),
      gameId: z.coerce.number().optional(),
      platformId: z.coerce.number().optional(),
    }).parse
  );
  const db = useDrizzle();
  const applications = await db.query.applications.findMany({
    // TODO: add filters
    where: (applications, { eq }) => {
      if (userId) return eq(applications.authorId, userId);
    },
  });
  return applications;
});
