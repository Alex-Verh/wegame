export default defineEventHandler(async (event) => {
  const { authorId, gameId, platformId, searchQuery, limit, offset } =
    await getValidatedQuery(
      event,
      z
        .object({
          authorId: z.coerce.number(),
          gameId: z.coerce.number(),
          platformId: z.coerce.number(),
          searchQuery: z.string(),
          limit: z.coerce.number().default(16),
          offset: z.coerce.number().default(0),
        })
        .partial().parse
    );
  const db = useDrizzle();
  const applications = await db.query.applications.findMany({
    where: and(
      authorId ? eq(tables.applications.authorId, authorId) : undefined,
      gameId ? eq(tables.applications.gameId, gameId) : undefined,
      platformId ? eq(tables.applications.platformId, platformId) : undefined,
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
    with: {
      author: {
        columns: { id: true, nickname: true, age: true, profilePic: true },
        with: {
          languages: { columns: { userId: false }, with: { language: true } },
        },
      },
      game: true,
      platform: true,
    },
  });
  return applications;
});
