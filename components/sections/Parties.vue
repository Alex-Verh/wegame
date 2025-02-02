<script setup lang="ts">
const { data: parties } = await useFetch('/api/parties')
</script>

<template>
    <section class="section">
        <div class="section_title">Parties - Find your brothers from another mother</div>

        <SearchBar />

        <div class="parties">
            <Row class="g-5">
                <template v-for="party in parties" :key="party.id">
                    <Col col="6">
                    <Party v-bind="party" />
                    </Col>
                </template>
            </Row>
        </div>
    </section>
</template>

<style scoped>
.parties {
    margin-top: 40px;
    margin-bottom: 100px;
}
</style>