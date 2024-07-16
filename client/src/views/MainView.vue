<script setup>
import Header from '../components/Header.vue'
import Games from '../components/Games.vue'
import Applications from '../components/Applications.vue'
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
