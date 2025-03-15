import jwt from "jsonwebtoken";
export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { maxFileSize, allowedFileTypes } = useRuntimeConfig();
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
        profilePic: z
          .any()
          .refine(
            (files) => files?.[0]?.size <= maxFileSize,
            `Max image size is 5MB.`
          )
          .refine(
            (files) => allowedFileTypes.includes(files?.[0]?.type),
            "Only .jpg, .jpeg, .png and .webp formats are supported."
          ),
        languages: z.record(z.coerce.number(), z.boolean()),
        platforms: z.record(z.coerce.number(), z.string().nullable()),
      })
      .partial().parse
  );
  if (!user.isSuperuser && user.id !== id) {
    throw forbiddenError;
  }

  const { sendMail } = useNodeMailer();
  const { secretKey } = useRuntimeConfig();

  const db = useDB();

  let languages: { languageId: number }[] = [];
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
    languages = await db.query.userLanguages.findMany({
      where: eq(tables.userLanguages.userId, id),
      columns: {
        userId: false,
      },
    });
    delete updatedUser.languages;
  }

  let platforms: { platformId: number; link: string }[] = [];
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
    platforms = await db.query.userPlatforms.findMany({
      where: eq(tables.userPlatforms.userId, id),
      columns: {
        userId: false,
      },
    });
    delete updatedUser.platforms;
  }
  if (updatedUser.email) {
    const token = jwt.sign(
      { userId: user.id, email: updatedUser.email },
      secretKey,
      {
        expiresIn: 60 * 10,
      }
    );
    await sendMail({
      subject: "Wegame user email verification",
      text: `Verification link: http://localhost:3000/api/users/email?token=${token}`,
      to: updatedUser.email,
    });
    delete updatedUser.email;
  }
  if (updatedUser.profilePic) {
    const filename = await storeFileLocally(
      updatedUser.profilePic[0],
      10,
      "/profile_pics"
    );
    updatedUser.profilePic = "/profile_pics/" + filename;
  }

  const [userFields] = Object.keys(updatedUser).length
    ? await db
        .update(tables.users)
        .set(updatedUser)
        .where(eq(tables.users.id, id))
        .returning()
    : [{}];

  return {
    ...userFields,
    languages,
    platforms,
  };
});
