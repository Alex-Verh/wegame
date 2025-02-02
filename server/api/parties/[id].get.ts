export default defineEventHandler(async (event) => {
  const { id } = await getValidatedRouterParams(
    event,
    z.object({ id: z.coerce.number() }).parse
  );

  const db = useDB();

  const party = await db.query.parties.findFirst({
    with: {
      leader: {
        columns: { id: true, nickname: true, age: true, profilePic: true },
        with: {
          languages: { columns: { userId: false }, with: { language: true } },
        },
      },
      game: true,
      platform: true,
      members: {
        columns: { partyId: false },
      },
    },
    where: eq(tables.parties.id, id),
  });
  return party;
});
