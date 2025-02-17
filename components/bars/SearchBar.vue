<script setup lang="ts">
defineProps<{
    isAppSearch: boolean
}>()

const title = defineModel<string>("title")
const platformId = defineModel<number>("platform")
const languageId = defineModel<number>("language")
const gameId = defineModel<number>("game")
const age = defineModel<number>("age")
const memberLimit = defineModel<number>("memberlimit")
const ranking = defineModel<string>("ranking")

const { data: games } = useGames()
const { data: platforms } = usePlatforms()
const { data: languages } = useLanguages()

</script>

<template>
    <div class="search_bar">
        <Row class="g-3">
            <Col col="4">
            <input v-model.lazy="title" type="text" name="find_by_title" placeholder="Find by title"
                class="search_field" />
            </Col>
            <template v-if="isAppSearch">
                <Col col="4">
                <select v-model="platformId" class="search_filter accent">
                    <option disabled :value="0" class="search_result">Filter by platform</option>
                    <option v-for="platform in platforms" class="search_result" :key="platform.id" :value="platform.id">{{ platform.title }}
                    </option>
                </select>
                </Col>
                <Col col="4">
                <select v-model="languageId" class="search_filter accent">
                    <option disabled :value="0" class="search_result">Filter by language</option>
                    <option v-for="language in languages" class="search_result" :key="language.id" :value="language.id">{{ language.title }}
                    </option>
                </select>
                </Col>
                <Col col="4">
                <select v-model="gameId" class="search_filter accent">
                    <option disabled :value="0" class="search_result">Filter by game</option>
                    <option v-for="game in games" class="search_result" :key="game.id" :value="game.id">{{ game.title }}</option>
                </select>
                </Col>
                <Col col="3">
                <input v-model.lazy="age" type="number" name="find_by_age" placeholder="Find by age" class="search_field" />
                </Col>
                <Col col="5">
                <input v-model.lazy="ranking" type="text" name="find_by_ranking" placeholder="Find by ranking"
                    class="search_field" />
                </Col>
            </template>
            <template v-else="isAppSearch">
                <Col col="3">
                <select v-model="platformId" class="search_filter accent">
                    <option disabled :value="0" class="search_result">Filter by platform</option>
                    <option v-for="platform in platforms" class="search_result" :key="platform.id" :value="platform.id">{{ platform.title }}
                    </option>
                </select>
                </Col>
                <Col col="3">
                <select v-model="gameId" class="search_filter accent">
                    <option disabled :value="0" class="search_result">Filter by game</option>
                    <option v-for="game in games" class="search_result" :key="game.id" :value="game.id">{{ game.title }}</option>
                </select>
                </Col>
                <Col col="2">
                <input v-model.lazy="memberLimit" type="number" name="find_by_memberlimit" placeholder="Find by lobby size" class="search_field" />
                </Col>
            </template>
        </Row>
    </div>
</template>

<style scoped>
.games_section {
    margin-top: 120px;
}

.section_title {
    color: #fff;
    font-size: 32px;
    font-weight: 700;
}

.search_bar {
    margin-top: 40px;
    background-color: #201F30;
    padding: 25px;
}

.search_filter,
.search_field {
    border: 1px solid #FE9F00;
    /* Change border color */
    border-radius: 5px;
    /* Optional: rounded corners */
    padding: 10px;
    /* Add some padding */
    width: 100%;
    /* Optional: make it full width */
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.search_filter {
    -webkit-appearance: none;
    appearance: none;
    background-image: url("~/assets/icons/expand.svg") !important;
    background-repeat: no-repeat !important;
    background-position: calc(100% - 12px) center !important;
    background: transparent;
}

.search_result {
    background-color: #201F30;
}

.search_field {
    background: transparent;
    /* Remove background */
    font-size: 16px;
    /* Adjust font size */
    color: #fff;
    /* Text color */
}

/* Placeholder styling */
.search_field::placeholder {
    color: #FE9F00;
    /* Placeholder text color */
    opacity: 1;
    /* Ensure the color is fully opaque */
}

.search_field:focus {
    outline: none;
    /* Remove default outline */
    box-shadow: 0 0 5px #fea100a5;
    /* Optional: add a shadow */
}
</style>