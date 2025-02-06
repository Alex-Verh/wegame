export default defineEventHandler(async (event) => {
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();
  const dbUser = await db.query.users.findFirst({
    columns: {
      password: false,
    },
    where: eq(tables.users.id, id),
    with: {
      platforms: {
        columns: { userId: false, platformId: false },
        with: { platform: true },
      },
      languages: {
        columns: { userId: false, languageId: false },
        with: { language: true },
      },
    },
  });
  if (!dbUser) throw userNotFoundError;

  const { languages, ...user } = dbUser;
  return {
    ...user,
    languages: languages.map(({ language }) => language),
  };
});
