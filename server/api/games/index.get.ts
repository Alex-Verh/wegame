import { getTableColumns, count } from "drizzle-orm";
export default defineEventHandler(async (event) => {
  const { userId, limit, popular } = await getValidatedQuery(
    event,
    z.object({
      userId: z.coerce.number().default(0),
      limit: z.coerce.number().default(48),
      popular: z.coerce.boolean().default(false),
    }).parse
  );
  const db = useDB();

  let query: any = db
    .selectDistinct({
      ...getTableColumns(tables.games),
      ...(popular
        ? {
            applicationsCount: count(tables.applications.id),
            partiesCount: count(tables.parties.id),
            totalCount: sql`${count(tables.applications.id)} + ${count(
              tables.parties.id
            )}`,
          }
        : {}),
    })
    .from(tables.games)
    .limit(limit);
  if (popular)
    query = query
      .leftJoin(
        tables.applications,
        eq(tables.games.id, tables.applications.gameId)
      )
      .leftJoin(tables.parties, eq(tables.games.id, tables.parties.gameId))
      .groupBy(tables.games.id)
      .orderBy((t: any) =>
        desc(sql`${t.applicationsCount} + ${t.partiesCount}`)
      );

  if (userId) {
    const unionSubquery = db
      .select({ gameId: tables.applications.gameId })
      .from(tables.applications)
      .where(eq(tables.applications.authorId, userId))
      .union(
        db
          .select({ gameId: tables.parties.gameId })
          .from(tables.parties)
          .where(eq(tables.parties.leaderId, userId))
      );

    query = query.where(sql`${tables.games.id} IN (${unionSubquery})`);
  }
  return await query;
});
