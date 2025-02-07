export default defineEventHandler(async (event) => {
  const { authorId, gameId, platformId, ranking, searchQuery, limit, offset } =
    await getValidatedQuery(
      event,
      z
        .object({
          authorId: z.coerce.number(),
          gameId: z.coerce.number(),
          platformId: z.coerce.number(),
          ranking: z.string(),
          searchQuery: z.string(),
          limit: z.coerce.number().default(16),
          offset: z.coerce.number().default(0),
        })
        .partial().parse
    );
  const db = useDB();
  const applications = await db.query.applications.findMany({
    with: {
      game: true,
      platform: true,
    },
    where: and(
      authorId ? eq(tables.applications.authorId, authorId) : undefined,
      gameId ? eq(tables.applications.gameId, gameId) : undefined,
      platformId ? eq(tables.applications.platformId, platformId) : undefined,
      ranking ? eq(tables.applications.ranking, ranking) : undefined,
      searchQuery
        ? sql`to_tsvector('english', ${tables.applications.text}) @@ websearch_to_tsquery('english', ${searchQuery})`
        : undefined
    ),
    limit,
    offset,
    orderBy: searchQuery
      ? desc(
          sql`ts_rank(to_tsvector('english', ${tables.applications.text}), websearch_to_tsquery('english', ${searchQuery}))`
        )
      : asc(tables.applications.text),
  });
  return applications;
});
