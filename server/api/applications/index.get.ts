export default defineEventHandler(async (event) => {
  const { userId, gameId, platformId } = await getValidatedQuery(
    event,
    z
      .object({
        userId: z.coerce.number(),
        gameId: z.coerce.number(),
        platformId: z.coerce.number(),
        limit: z.coerce.number().default(15),
        offset: z.coerce.number().default(0),
        search: z.string(),
      })
      .partial().parse
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
