export default defineEventHandler(async (event) => {
  const db = useDB();
  return await db.query.languages.findMany({});
});
