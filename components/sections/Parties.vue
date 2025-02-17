<script setup lang="ts">

const title = ref("")
const gameId = ref(0)
const platformId = ref(0)
const languageId = ref(0) // TODO (remove)
const age = ref(0) // TODO (rename to members number)
const ranking = ref("")  // TODO (remove)

const { data: parties } = useQuery({
    key: () => ["parties", { title: title.value, gameId: gameId.value, platformId: platformId.value, age: age.value }],
    query: () => useRequestFetch()("/api/parties", { query: { searchQuery: title.value, gameId: gameId.value, platformId: platformId.value, age: age.value } }) as Promise<Party[]>,
})
</script>

<template>
    <section class="section">
        <div class="section_title">Parties - Find your brothers from another mother</div>
        <SearchBar v-model:title="title" v-model:game="gameId" v-model:platform="platformId"
            v-model:language="languageId" v-model:age="age" v-model:ranking="ranking" :isAppSearch="false"/>
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