import jwt from "jsonwebtoken";

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

  const { sendMail } = useNodeMailer();
  const { secretKey } = useRuntimeConfig();

  const token = jwt.sign({ userId: user.id }, secretKey, {
    expiresIn: 60 * 10,
  });

  await sendMail({
    subject: "Wegame user email verification",
    text: `Verification link: http://localhost:3000/api/auth/activate?token=${token}`,
    to: user.email,
  });

  setResponseStatus(event, 201);
  return { status: 201, message: "Registered" };
});
