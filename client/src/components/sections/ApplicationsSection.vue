<script setup>
import SearchBar from '../bars/SearchBar.vue'
import ApplicationComponent from '../ApplicationComponent.vue'
</script>

<template>
    <section class="section">
        <div class="section_title">Applications - Find One</div>

        <SearchBar />

        <div class="applications">
            <ApplicationComponent />
            <ApplicationComponent />
            <ApplicationComponent />
            <ApplicationComponent />
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