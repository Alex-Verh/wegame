import { exists, gte, lte } from "drizzle-orm";

export default defineEventHandler(async (event) => {
  const {
    leaderId,
    memberId,
    gameId,
    platformId,
    searchQuery,
    age,
    membersLimit,
    limit,
    offset,
  } = await getValidatedQuery(
    event,
    z
      .object({
        leaderId: z.coerce.number(),
        memberId: z.coerce.number(),
        gameId: z.coerce.number(),
        platformId: z.coerce.number(),
        searchQuery: z.string(),
        age: z.coerce.number(),
        membersLimit: z.coerce.number(),
        limit: z.coerce.number().default(16),
        offset: z.coerce.number().default(0),
      })
      .partial().parse
  );
  const db = useDB();
  const query = {
    with: {
      game: true,
      platform: true,
      members: {
        columns: { partyId: false },
        with: {
          user: { columns: { password: false } },
        },
      },
    },
    where: and(
      leaderId ? eq(tables.parties.leaderId, leaderId) : undefined,
      memberId
        ? exists(
            db
              .select()
              .from(tables.partyMembers)
              .where(
                and(
                  eq(tables.partyMembers.partyId, tables.parties.id),
                  eq(tables.partyMembers.userId, memberId),
                  eq(tables.partyMembers.status, "accepted")
                )
              )
          )
        : undefined,
      gameId ? eq(tables.parties.gameId, gameId) : undefined,
      platformId ? eq(tables.parties.platformId, platformId) : undefined,
      searchQuery
        ? sql`(
            setweight(to_tsvector('english', ${tables.parties.title}), 'A') ||
            setweight(to_tsvector('english', ${tables.parties.description}), 'B')
            ) @@ websearch_to_tsquery('english', ${searchQuery})`
        : undefined,
      age
        ? and(lte(tables.parties.minAge, age), gte(tables.parties.maxAge, age))
        : undefined,
      membersLimit ? eq(tables.parties.membersLimit, membersLimit) : undefined
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
  } as const;

  return await db.query.parties.findMany(query);
});
