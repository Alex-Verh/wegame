<script setup>
import { RouterView } from 'vue-router'
import Footer from "./components/common/Footer.vue"
import NavBar from "./components/common/NavBar.vue"
</script>

<template>
  <NavBar />
  <RouterView />
  <Footer />
</template>

<style scoped>
</style>
