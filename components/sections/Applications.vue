<script setup lang="ts">

const title = ref("")
const gameId = ref(0)
const platformId = ref(0)
const languageId = ref(0) // TODO
const age = ref(0) // TODO
const ranking = ref("")


const { data: applications, isLoading } = useQuery({
    key: () => ["applications", { title: title.value, gameId: gameId.value, platformId: platformId.value, ranking: ranking.value }],
    query: () => useRequestFetch()("/api/applications", { query: { searchQuery: title.value, gameId: gameId.value, platformId: platformId.value, ranking: ranking.value } }) as Promise<Application[]>,
})

</script>

<template>
    <section class="section" id="applications">
        <div class="section_title">Applications - Find One</div>
        <SearchBar v-model:title="title" v-model:game="gameId" v-model:platform="platformId"
            v-model:language="languageId" v-model:age="age" v-model:ranking="ranking" />
        <div class="applications">
            <Application v-for="application in applications" :key="application.id" v-bind="application" />
            <div v-if="isLoading">Loading</div>
        </div>
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