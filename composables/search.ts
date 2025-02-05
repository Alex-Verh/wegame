export const useGameSearch = () => {
  const { data: games } = useGames();

  const searchQuery = ref("");

  const searchResults = computed(() =>
    searchQuery.value
      ? games.value?.filter((game) =>
          game.title
            .toLowerCase()
            .includes(searchQuery.value.trim().toLowerCase())
        )
      : games.value
  );
  return {
    searchQuery,
    games: searchResults,
  };
};
