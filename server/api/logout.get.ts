export default defineEventHandler(async (event) => {
  await clearUserSession(event);

  return { status: 200, message: "Logged out" };
});
