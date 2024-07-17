<script setup>
import { RouterView } from 'vue-router'
import Footer from "./components/bars/FootBar.vue"
import NavBar from "./components/bars/NavBar.vue"
</script>

<template>
  <NavBar />
  <RouterView />
  <Footer />
</template>

<style scoped></style>
