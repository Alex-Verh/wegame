import jwt from "jsonwebtoken";

export default defineEventHandler(async (event) => {
  const { token } = await getValidatedQuery(
    event,
    z.object({ token: z.string() }).parse
  );
  const { secretKey } = useRuntimeConfig();

  const { userId } = jwt.verify(token, secretKey);

  const db = useDrizzle();
  const [user] = await db
    .update(tables.users)
    .set({ isActive: true })
    .where(eq(tables.users.id, userId))
    .returning();

  return sendRedirect(event, "/sign-in");
});
