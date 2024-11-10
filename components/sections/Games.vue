<script setup>

const { data: games } = await useFetch('/api/games')
</script>

<template>
    <section class="section">
        <div class="section_title">
            Popular Games - Select One
        </div>
        <div class="games">
            <b-row class="g-5">
                <b-col v-for="game in games" :key="game.id" cols="4" class="d-flex justify-content-center">
                    <Game :title="game.title" :image="game.image" />
                </b-col>
            </b-row>
        </div>
    </section>
</template>

<style scoped>
.games {
    margin-top: 30px;
}
</style>