export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { gameId, platformId, text, ranking } = await readValidatedBody(
    event,
    z.object({
      gameId: z.number(),
      platformId: z.number(),
      text: z.string(),
      ranking: z.string().optional(),
    }).parse
  );
  const db = useDB();

  const [application] = await db
    .insert(tables.applications)
    .values({
      authorId: user.id,
      gameId,
      platformId,
      text,
      ranking,
    })
    .returning()
    .onConflictDoNothing();
  return application;
});
