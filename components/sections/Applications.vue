<script setup lang="ts">
// import { useInfiniteQuery } from "@pinia/colada";
import { onWatcherCleanup } from "vue";
const title = ref("");
const gameId = ref(0);
const platformId = ref(0);
const languageId = ref(0);
const age = ref(null);
const ranking = ref("");

// const {
//   state: applications,
//   loadMore,
//   asyncStatus,
// } = useInfiniteQuery({
//   key: () => [
//     "applications",
//     {
//       title: title.value,
//       gameId: gameId.value,
//       platformId: platformId.value,
//       ranking: ranking.value,
//       languageId: languageId.value,
//       age: age.value,
//     },
//   ],
//   query: async ({ nextPage }) =>
//     nextPage != null
//       ? (useRequestFetch()("/api/applications", {
//           query: {
//             searchQuery: title.value,
//             gameId: gameId.value,
//             platformId: platformId.value,
//             ranking: ranking.value,
//             languageId: languageId.value,
//             age: age.value,
//             offset: (nextPage - 1) * 4,
//             limit: 4,
//           },
//         }) as Promise<Application[]>)
//       : null,
//   initialPage: {
//     data: new Set<Application>(),
//     nextPage: 1 as number | null,
//   },
//   merge(pages, newApplications) {
//     if (!newApplications) return pages;
//     const data = new Set([...pages.data, ...newApplications]);
//     return {
//       data,
//       nextPage: pages.nextPage != null ? pages.nextPage + 1 : null,
//     };
//   },
// });

// const loadMoreEl = useTemplateRef("loadMoreRef");

// watch(loadMoreEl, (el) => {
//   if (el) {
//     const observer = new IntersectionObserver(
//       (entries) => {
//         if (entries[0]?.isIntersecting) {
//           loadMore();
//         }
//       },
//       {
//         rootMargin: "300px",
//         threshold: [0],
//       }
//     );
//     observer.observe(el);
//     onWatcherCleanup(() => {
//       observer.disconnect();
//     });
//   }
// });
</script>

<template>
  <section class="section" id="applications">
    <div class="section_title">{{ $t("applicationHeader") }}</div>
    <!-- <SearchBar
      v-model:title="title"
      v-model:game="gameId"
      v-model:platform="platformId"
      v-model:language="languageId"
      v-model:age="age"
      v-model:ranking="ranking"
      :isAppSearch="true"
    />
    <div class="applications">
      <Application
        v-for="application in applications.data.data"
        :key="application.id"
        v-bind="application"
      />
      <p v-if="applications.data.nextPage" ref="loadMoreRef">Loading more...</p>
    </div> -->
  </section>
</template>

<style scoped>
.games_section {
  margin-top: 120px;
}

.applications {
  margin-top: 40px;
  margin-bottom: 100px;
}
</style>
