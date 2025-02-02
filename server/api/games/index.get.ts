import { getTableColumns, count } from "drizzle-orm";
export default defineEventHandler(async (event) => {
  const { popular } = await getValidatedQuery(
    event,
    z.object({ popular: z.coerce.boolean().default(false) }).parse
  );
  const db = useDB();
  if (popular)
    return await db
      .select({
        ...getTableColumns(tables.games),
        applicationsCount: count(tables.applications.id),
        partiesCount: count(tables.parties.id),
      })
      .from(tables.games)
      .leftJoin(
        tables.applications,
        eq(tables.games.id, tables.applications.gameId)
      )
      .leftJoin(tables.parties, eq(tables.games.id, tables.parties.gameId))
      .groupBy(tables.games.id)
      .orderBy((t) => desc(sql`${t.applicationsCount} + ${t.partiesCount}`));
  return await db.query.games.findMany({});
});
