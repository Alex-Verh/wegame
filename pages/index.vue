<script setup lang="ts">
</script>

<template>
  <Container>
    <Header
      :text="$t('homeHeader')"
      image="/images/main_image.jpg" :showStatistics="false" />
    <Games />
    <Applications />
  </Container>
</template>

<style scoped></style>
