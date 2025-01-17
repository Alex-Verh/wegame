export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const { gameId, platformId, title, description, minAge, maxAge, membersLimit } = await readValidatedBody(
    event,
    z.object({
      gameId: z.number(),
      platformId: z.number(),
      minAge: z.number(),
      maxAge: z.number(),
      membersLimit: z.number(),
      title: z.string(),
      description: z.string().optional(),
    }).parse
  );
  const db = useDrizzle();

  const [party] = await db
    .insert(tables.parties)
    .values({
      leaderId: user.id,
      gameId,
      platformId,
      minAge,
      maxAge,
      membersLimit,
      title,
      description
    })
    .returning()
    .onConflictDoNothing();
  return party;
});
