export default defineEventHandler(async (event) => {
  const db = useDB();
  const { email, password } = await readValidatedBody(
    event,
    z.object({
      email: z.string().email(),
      password: z.string().min(8),
    }).parse
  );

  const user = await db.query.users.findFirst({
    where: eq(tables.users.email, email),
  });

  if (!user) throw invalidCredentialsError;

  if (!(await verifyPassword(user.password as string, password)))
    throw invalidCredentialsError;

  if (!user.isActive) throw userNotActiveError;

  await setUserSession(event, {
    user: {
      id: user.id,
      email: user.email,
      nickname: user.nickname,
      age: user.age,
      profilePic: user.profilePic,
      isActive: user.isActive,
      isSuperuser: user.isSuperuser,
    },
    loggedInAt: Date.now(),
  });

  setResponseStatus(event, 201);
  return { status: 201, message: "Logged in" };
});
