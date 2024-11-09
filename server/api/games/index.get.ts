export default defineEventHandler(async (event) => {
  const { limit } = await getValidatedQuery(
    event,
    z.object({
      limit: z.coerce.number().default(15),
    }).parse
  );
  const db = useDrizzle();
  const games = await db.query.games.findMany({
    limit,
  });
  return games;
});
