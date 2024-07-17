<script setup>
import Header from '../components/sections/HeaderSection.vue'
import Parties from '../components/sections/PartiesSection.vue'
</script>

<template>
    <main>
        <b-container>
            <Header text='Let’s find an extra quality <span class="accent">lobby</span> for you, right now!'
                image="/src/assets/main_image.jpg" showStatistics="true" />
            <Parties />
        </b-container>
    </main>
</template>