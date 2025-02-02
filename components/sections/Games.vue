<script setup lang="ts">

const { data: games } = await useFetch('/api/games', { query: { popular: true } })
</script>

<template>
    <section class="section">
        <div class="section_title">
            Popular Games - Select One
        </div>
        <div class="games">
            <Row class="g-5">
                <Col v-for="game in games" :key="game.id" col="4" class="d-flex justify-content-center">
                <Game v-bind="game" />
                </Col>
            </Row>
        </div>
    </section>
</template>

<style scoped>
.games {
    margin-top: 30px;
}
</style>