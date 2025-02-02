export default defineEventHandler(async (event) => {
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();

  const application = await db.query.applications.findFirst({
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
    where: eq(tables.applications.id, id),
  });
  return application;
});
