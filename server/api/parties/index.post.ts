export default defineEventHandler(async (event) => {
  const { user } = await requireUserSession(event);
  const {} = await readValidatedBody(event, z.object({}).parse);
  const db = useDrizzle();

  const [party] = await db
    .insert(tables.parties)
    .values({
      leaderId: user.id,
      //   todo
    })
    .returning()
    .onConflictDoNothing();
  return party;
});
