<script setup lang="ts">
const { data: applications } = await useFetch('/api/applications')
</script>

<template>
    <section class="section" id="applications">
        <div class="section_title">Applications - Find One</div>
        <SearchBar />
        <div class="applications">
            <Application v-for="application in applications" :key="application.id" :text="application.text"
                :author="application.author" :game="application.game" />
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