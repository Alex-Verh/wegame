export default defineEventHandler(async (event) => {
  const db = useDrizzle();
  return await db.query.platforms.findMany({});
});
