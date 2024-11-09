export default defineEventHandler(async (event) => {
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  // const { user } = await getUserSession(event);

  const db = useDrizzle();
  const dbUser = await db.query.users.findFirst({
    columns: {
      password: false,
    },
    where: (users, { eq }) => eq(users.id, id),
    with: {
      platforms: {
        columns: {
          userId: false,
        },
        with: { platform: true },
      },
      languages: {
        columns: {
          userId: false,
        },
        with: { language: true },
      },
      applications: true,
      own_parties: true,
    },
  });
  return dbUser;
});
