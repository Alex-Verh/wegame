export default defineOAuthGoogleEventHandler({
  config: {
    scope: ["email"],
  },
  onSuccess: async (event, { user }) => {
    if (!user.email) {
      throw invalidCredentialsError;
    }
    const db = useDB();

    let dbUser = await db.query.users.findFirst({
      where: eq(tables.users.email, user.email),
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
      user: {
        id: dbUser.id,
        email: dbUser.email,
        profilePic: dbUser.profilePic,
        nickname: dbUser.nickname,
        age: dbUser.age,
        isActive: user.isActive,
        isSuperuser: user.isSuperuser,
      },
      loggedInAt: Date.now(),
    });
    return sendRedirect(event, "/");
  },
  // Optional, will return a json error and 401 status code by default
  onError: (event, error) => {
    console.error("GitHub OAuth error:", error);
    return sendRedirect(event, "/");
  },
});
