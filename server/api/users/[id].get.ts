export default defineEventHandler(async (event) => {
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();
  const dbUser = await db.query.users.findFirst({
    columns: {
      password: false,
      email: false,
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
      applications: true,
      own_parties: true,
      member_parties: {
        columns: { userId: false },
        with: { party: true },
      },
    },
  });
  if (!dbUser) throw userNotFoundError;

  const { own_parties, member_parties, languages, ...user } = dbUser;
  return {
    ...user,
    parties: [...own_parties, ...member_parties.map(({ party }) => party)],
    languages: languages.map(({ language }) => language),
  };
});
