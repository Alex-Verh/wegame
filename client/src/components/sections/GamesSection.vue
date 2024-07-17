<script setup>
import Game from '../GameComponent.vue'
</script>

<template>
    <section class="section">
        <div class="section_title">
            Popular Games - Select One
        </div>
        <div class="games">
            <b-row class="g-5">
                <b-col cols="4" class="d-flex justify-content-center">
                    <Game />
                </b-col>

                <b-col cols="4" class="d-flex justify-content-center">
                    <Game />
                </b-col>

                <b-col cols="4" class="d-flex justify-content-center">
                    <Game />
                </b-col>

                <b-col cols="4" class="d-flex justify-content-center">
                    <Game />
                </b-col>
                
                <b-col cols="4" class="d-flex justify-content-center">
                    <Game />
                </b-col>
                
                <b-col cols="4" class="d-flex justify-content-center">
                    <Game />
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