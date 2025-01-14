<script setup lang="ts">
const { application } = defineProps({
    isNew: Boolean,
    isOpen: Boolean,
    application: Object,
})


const userData = inject<Ref<User>>("userData");

const { data: games } = await useFetch('/api/games')
const { data: platforms } = await useFetch('/api/platforms')

const gamesSearch = ref("")
const showedGames = computed(() =>
    gamesSearch.value ?
        games?.value?.filter((game) => game.title.toLowerCase().includes(gamesSearch.value.trim().toLowerCase())) :
        games?.value
)

const applicationGame = ref(application?.gameId || games?.value?.[0].id)
const applicationPlatform = ref(application?.gameId || games?.value?.[0].id)
const applicationText = ref("")
const applicationRank = ref("")

const createApplication = async () => {
    const application = await $fetch('/api/applications', {
        method: "POST",
        body: {
            gameId: applicationGame.value,
            platformId: applicationPlatform.value,
            text: applicationText.value,
            ranking: applicationRank.value,


        }
    })
    if (application)
        userData?.value.applications?.push(application)
    applicationText.value = ""
    applicationRank.value = ""
    close();

}
</script>

<template>
    <Popup :visible="isOpen">
        <Container>
            <div class="application_title">Create Application</div>

            <div class="application_body">

                <label for="application_description" class="application_subtitle">Write an application message</label>
                <textarea v-model="applicationText" name="application_description" id="application_description"
                    class="application_field application_textarea" placeholder="I am looking for a friend.."></textarea>

                <label for="application_rank" class="application_subtitle">Describe your game rank</label>
                <input v-model="applicationRank" type="text" name="application_rank" id="application_rank"
                    class="application_field" placeholder="Silver III" />

                <label for="application_platforms" class="application_subtitle">Select Game Platform</label>
                <div class="application_platforms">
                    <template v-for="platform in platforms" :key="platform.id">
                        <input v-model="applicationPlatform" type="radio" :id="`${platform.title}+${platform.id}`"
                            name="application_platform" :value="platform.id" />
                        <label :for="`${platform.title}+${platform.id}`" class="application_platform">{{ platform.title
                            }}</label>
                    </template>
                </div>

                <label for="games_search" class="application_subtitle">Search your application game</label>
                <input v-model="gamesSearch" type="text" name="games_search" id="games_search" class="application_field"
                    placeholder="Searching.." />
                <div class="pop_section d-flex flex-row">
                    <template v-for="game in showedGames" :key="game.id">
                        <input v-model="applicationGame" type="radio" :id="`${game.title}+${game.id}`"
                            name="application_game" :value="game.id" />
                        <label :for="`${game.title}+${game.id}`">
                            <Game :title="game.title" :image="game.image" class="game_pop" />
                        </label>
                    </template>

                </div>

                <div class="application_buttons d-flex justify-content-center">
                    <button v-if="isNew" @click="createApplication" class="button_accent">Save Changes</button>
                    <template v-else>
                        <button class="button_accent">Save Changes</button>
                        <button class="button_accent">Delete application</button>
                    </template>
                </div>

            </div>

        </Container>
    </Popup>
</template>

<style scoped>
.application {
    width: 1000px;
}

.application_body {
    overflow-y: scroll;
    height: 500px;
    padding: 0 30px;
}

.application_body::-webkit-scrollbar {
    width: 3px;
}

.application_title {
    text-align: center;
    font-size: 34px;
}

.application_subtitle {
    font-size: 18px;
    margin: 20px 0;
    display: block;
}

.application_field {
    background: none;
    border: 1px solid #444259;
    width: 100%;
    color: #fff;
    font-size: 20px;
    padding: 10px;
}

.application_textarea {
    resize: none;
    height: 100px;
}

.application_platforms {
    display: flex;
    justify-content: space-between;
    color: #444259;
}

.application_platforms input[type="radio"],
.pop_section input[type="radio"] {
    display: none;
}

.application_platforms input[type="radio"]:checked+.application_platform {
    color: #FE9F00;
}

.application_platform {
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.pop_section {
    margin-top: 20px;
    height: 130px;
    overflow-x: auto;
    overflow-y: hidden;
}

.pop_section label {
    display: block;
    margin-inline-end: 25px;
}

.game_pop {
    margin-inline-end: 25px;
    flex-shrink: 0;
    height: 100%;
    min-width: auto !important;
    font-size: 12px !important;
}

.game_pop:last-of-type {
    margin-inline-end: 0px;
}

.application_buttons {
    margin-top: 20px;
}

.application_buttons .button_accent {
    width: 175px;
    margin-inline: 5px;
}

/* Scroll */
::-webkit-scrollbar {
    height: 3px;
}

/* Handle */
::-webkit-scrollbar-thumb {
    background: #FE9F00;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
    background: #201F30;
}
</style>