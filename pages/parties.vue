<script setup>
</script>

<template>
    <Container>
        <Header :text="$t('partyHeader')"
            image="/images/parties_image.jpg" :showStatistics="true" />
        <Parties />
    </Container>
</template>