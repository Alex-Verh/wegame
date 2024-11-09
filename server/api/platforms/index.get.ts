export default defineEventHandler(async (event) => {
  const { limit } = await getValidatedQuery(
    event,
    z.object({
      limit: z.coerce.number().default(15),
    }).parse
  );
  const db = useDrizzle();
  const platforms = await db.query.platforms.findMany({
    limit,
  });
  return platforms;
});
