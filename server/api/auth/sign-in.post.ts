export default defineEventHandler(async (event) => {
  const db = useDrizzle();
  const { email, password } = await readValidatedBody(
    event,
    z.object({
      email: z.string().email(),
      password: z.string().min(8),
    }).parse
  );

  const user = await db.query.users.findFirst({
    where: (users, { eq }) => eq(users.email, email),
  });

  if (!user) {
    throw invalidCredentialsError;
  }

  if (!(await verifyPassword(user.password, password))) {
    throw invalidCredentialsError;
  }

  await setUserSession(event, {
    user: {
      id: user.id,
      email: user.email,
      nickname: user.nickname,
      age: user.age,
      profilePic: user.profilePic,
    },
    loggedInAt: Date.now(),
  });

  setResponseStatus(event, 201);
  return { status: 201, message: "Logged in" };
});
