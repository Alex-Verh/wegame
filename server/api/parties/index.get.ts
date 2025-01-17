export default defineEventHandler(async (event) => {
  const { leaderId, gameId, platformId, searchQuery, limit, offset } =
    await getValidatedQuery(
      event,
      z
        .object({
          leaderId: z.coerce.number(),
          gameId: z.coerce.number(),
          platformId: z.coerce.number(),
          searchQuery: z.string(),
          limit: z.coerce.number().default(16),
          offset: z.coerce.number().default(0),
        })
        .partial().parse
    );
  const db = useDrizzle();
  const parties = await db.query.parties.findMany({
    with: {
      leader: {
        columns: { id: true, nickname: true, age: true, profilePic: true },
        with: {
          languages: { columns: { userId: false }, with: { language: true } },
        },
      },
      game: true,
      platform: true,
      members: {
        columns: { partyId: false },
      },
    },
    where: and(
      leaderId ? eq(tables.parties.leaderId, leaderId) : undefined,
      gameId ? eq(tables.parties.gameId, gameId) : undefined,
      platformId ? eq(tables.parties.platformId, platformId) : undefined,
      searchQuery
        ? sql`(
            setweight(to_tsvector('english', ${tables.parties.title}), 'A') ||
            setweight(to_tsvector('english', ${tables.parties.description}), 'B')
            ) @@ websearch_to_tsquery('english', ${searchQuery})`
        : undefined
    ),
    limit,
    offset,
    orderBy: searchQuery
      ? desc(
          sql`ts_rank((
            setweight(to_tsvector('english', ${tables.parties.title}), 'A') ||
            setweight(to_tsvector('english', ${tables.parties.description}), 'B')
            ), websearch_to_tsquery('english', ${searchQuery}))`
        )
      : asc(tables.parties.title),
  });
  return parties;
});
