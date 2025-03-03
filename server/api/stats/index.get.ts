export default defineEventHandler(async (event) => {
  const db = useDB();

  const parties = await db.$count(tables.parties);
  const games = await db.$count(tables.games);
  const players = await db.$count(tables.users);

  return {
    parties,
    games,
    players,
  };
});
