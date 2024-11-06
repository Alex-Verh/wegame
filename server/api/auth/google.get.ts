export default defineOAuthGoogleEventHandler({
  config: {
    scope: ["email"],
  },
  async onSuccess(event, { user }) {
    if (!user.email) {
      throw invalidCredentialsError;
    }
    const db = useDrizzle();

    let dbUser = await db.query.users.findFirst({
      where: (users, { eq }) => eq(users.email, user.email),
    });
    if (!dbUser) {
      [dbUser] = await db
        .insert(tables.users)
        .values({
          email: user.email,
          profilePic: user.picture,
          nickname: user.name,
          password: "",
          isSuperuser: false,
          isActive: true,
        })
        .returning();
    }
    await setUserSession(event, {
      user: { id: dbUser.id },
      loggedInAt: Date.now(),
    });
    return sendRedirect(event, "/");
  },
  // Optional, will return a json error and 401 status code by default
  onError(event, error) {
    console.error("GitHub OAuth error:", error);
    return sendRedirect(event, "/");
  },
});
