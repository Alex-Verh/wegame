export const useGames = defineQuery({
  key: ["games"],
  query: () => useRequestFetch()("/api/games") as Promise<Game[]>,
});

export const usePlatforms = defineQuery({
  key: ["platforms"],
  query: () => useRequestFetch()("/api/platforms") as Promise<Platform[]>,
});

export const useLanguages = defineQuery({
  key: ["languages"],
  query: () => useRequestFetch()("/api/languages") as Promise<Language[]>,
});

export const useCurrentUser = defineQuery(() => {
  const { user } = useUserSession();
  const result = useQuery({
    key: () => ["users", user.value?.id as number],
    query: () =>
      useRequestFetch()(`/api/users/${user.value?.id}`) as Promise<User>,
    enabled: () => user.value !== null,
  });
  return {
    ...result,
  };
});
