import jwt from "jsonwebtoken";

export default defineEventHandler(async (event) => {
  const { token } = await getValidatedQuery(
    event,
    z.object({ token: z.string() }).parse
  );
  const { secretKey } = useRuntimeConfig();

  const { userId, email } = jwt.verify(token, secretKey) as {
    userId: number;
    email: string;
  };
  const db = useDB();
  const [user] = await db
    .update(tables.users)
    .set({ email })
    .where(eq(tables.users.id, userId))
    .returning();

  return sendRedirect(event, "/");
});
