<script setup lang="ts">


const { data: applications } = useQuery({
    key: ["applications"],

    query: () => useRequestFetch()("/api/applications", { query: {} }) as Promise<Application[]>,
})
</script>

<template>
    <section class="section" id="applications">
        <div class="section_title">Applications - Find One</div>
        <SearchBar />
        <div class="applications">
            <Application v-for="application in applications" :key="application.id" v-bind="application" />
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