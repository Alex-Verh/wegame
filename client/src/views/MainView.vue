<script setup>
import Header from '../components/sections/HeaderSection.vue'
import Games from '../components/sections/GamesSection.vue'
import Applications from '../components/sections/ApplicationsSection.vue'
</script>

<template>
  <main class="main">
    <b-container>
      <Header
        text='Find new <span class="accent">friends</span> and make game <span class="accent">parties</span> easily and fast now.'
        image="/src/assets/main_image.jpg" />
      <Games />
      <Applications />
    </b-container>
  </main>
</template>

<style scoped></style>
