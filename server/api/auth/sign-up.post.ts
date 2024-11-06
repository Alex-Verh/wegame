export default defineEventHandler(async (event) => {
  const db = useDrizzle();
  const { nickname, email, password } = await readValidatedBody(
    event,
    z.object({
      nickname: z.string(),
      email: z.string().email(),
      password: z.string().min(8),
    }).parse
  );

  const hashedPassword = await hashPassword(password);

  const [user] = await db
    .insert(tables.users)
    .values({
      nickname,
      email,
      password: hashedPassword,
      isActive: false,
      isSuperuser: false,
    })
    .returning()
    .onConflictDoNothing();

  if (!user) {
    throw userAlreadyExistsError;
  }
  await setUserSession(event, {
    user: { id: user.id },
    loggedInAt: Date.now(),
  });
  setResponseStatus(event, 201);
  return { status: 201, message: "Registered" };
});
