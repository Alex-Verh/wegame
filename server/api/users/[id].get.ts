export default defineEventHandler(async (event) => {
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDrizzle();
  const dbUser = await db.query.users.findFirst({
    columns: {
      password: false,
      email: false,
    },
    where: eq(tables.users.id, id),
    with: {
      platforms: {
        columns: {
          userId: false,
        },
      },
      languages: {
        columns: {
          userId: false,
        },
      },
      applications: true,
      own_parties: true,
      member_parties: {
        columns: {
          userId: false,
        },
        with: {
          party: true,
        },
      },
    },
  });
  if (!dbUser) throw userNotFoundError;

  return {
    id: dbUser.id,
    profilePic: dbUser.profilePic,
    nickname: dbUser.nickname,
    age: dbUser.age,
    isActive: dbUser.isActive,
    isSuperuser: dbUser.isSuperuser,
    platforms: dbUser.platforms,
    languages: dbUser.languages,
    applications: dbUser.applications,
    parties: [
      ...dbUser.own_parties,
      ...dbUser.member_parties.map(({ party }) => party),
    ],
  };
});
