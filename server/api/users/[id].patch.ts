export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );
  const updatedUser = await readValidatedBody(
    event,
    z
      .object({
        nickname: z.string(),
        email: z.string().email(),
        age: z.number(),
        profilePic: z.string(),
        languages: z.record(z.coerce.number(), z.boolean()),
        platforms: z.record(z.coerce.number(), z.string().nullable()),
      })
      .partial().parse
  );
  if (!user.isSuperuser && user.id !== id) {
    throw forbiddenError;
  }
  const db = useDrizzle();
  const result: any = {};
  if (updatedUser.languages) {
    const langsToInsert = [];
    for (const languageId in updatedUser.languages) {
      if (updatedUser.languages[languageId])
        langsToInsert.push({ userId: id, languageId: Number(languageId) });
      else
        await db
          .delete(tables.userLanguages)
          .where(
            and(
              eq(tables.userLanguages.userId, id),
              eq(tables.userLanguages.languageId, Number(languageId))
            )
          );
    }
    if (langsToInsert.length)
      await db.insert(tables.userLanguages).values(langsToInsert);
    result.languages = await db.query.userLanguages.findMany({
      where: eq(tables.userLanguages.userId, id),
      columns: {
        userId: false,
      },
    });
    delete updatedUser.languages;
  }
  if (updatedUser.platforms) {
    const platformsToInsert = [];
    for (const platformId in updatedUser.platforms) {
      if (updatedUser.platforms[platformId])
        platformsToInsert.push({
          userId: id,
          platformId: Number(platformId),
          link: updatedUser.platforms[platformId],
        });
      else
        await db
          .delete(tables.userPlatforms)
          .where(
            and(
              eq(tables.userPlatforms.userId, id),
              eq(tables.userPlatforms.platformId, Number(platformId))
            )
          );
    }
    if (platformsToInsert.length)
      await db
        .insert(tables.userPlatforms)
        .values(platformsToInsert)
        .onConflictDoUpdate({
          target: [
            tables.userPlatforms.userId,
            tables.userPlatforms.platformId,
          ],
          set: { link: sql`excluded.link` },
        });
    result.platforms = await db.query.userPlatforms.findMany({
      where: eq(tables.userPlatforms.userId, id),
      columns: {
        userId: false,
      },
    });
    delete updatedUser.platforms;
  }
  if (Object.keys(updatedUser).length) {
    const [userFields] = await db
      .update(tables.users)
      .set(updatedUser)
      .where(eq(tables.users.id, id))
      .returning(
        Object.keys(updatedUser).reduce(
          (acc, key) => ({ ...acc, [key]: tables.users[key] }),
          {}
        )
      );
    Object.assign(result, userFields);
  }

  return {
    updatedFields: result,
  };
});
