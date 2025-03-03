<script setup lang="ts">

const stats = useFetch('/api/stats')

</script>

<template>
    <Container>
        <Header v-if="stats" :text="$t('partyHeader')" image="/images/parties_image.jpg" :stats="stats" />
        <Parties />
    </Container>
</template>