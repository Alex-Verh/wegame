<script setup lang="ts">
const { application } = defineProps({
    isOpen: Boolean,
    application: Object
})


const userData = inject<Ref<User>>("userData");

const { data: games } = await useFetch('/api/games')

const selectedGame = ref(application?.gameId || games?.value?.[0].id)
const applicationText = ref("")
const applicationSearch = ref("")
const applicationRank = ref("")
const applicationPlatform = ref("")

const createApplication = async () => {
    const application = await $fetch('/api/applications', {
        method: "POST",
        body: {
            gameId: selectedGame.value,
            platformId: 1,
            text: applicationText.value
        }
    })
    if (application)
        userData?.value.applications?.push(application)
    applicationText.value = ""
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

                <!-- TODO make the platform list dynamic (from db) -->
                <label for="application_platforms" class="application_subtitle">Select Game Platform</label>
                <div class="application_platforms">
                    <input v-model="applicationPlatform" type="radio" id="Steam" name="application_platform"
                        value="Steam" />
                    <label for="Steam" class="application_platform">Steam</label>

                    <input v-model="applicationPlatform" type="radio" id="EA" name="application_platform" value="EA" />
                    <label for="EA" class="application_platform">EA Play</label>

                    <input v-model="applicationPlatform" type="radio" id="Epic" name="application_platform"
                        value="Epic" />
                    <label for="Epic" class="application_platform">Epic Games</label>

                    <input v-model="applicationPlatform" type="radio" id="XBOX" name="application_platform"
                        value="XBOX" />
                    <label for="XBOX" class="application_platform">XBOX</label>

                    <input v-model="applicationPlatform" type="radio" id="Playstation" name="application_platform"
                        value="Playstation" />
                    <label for="Playstation" class="application_platform">Playstation</label>

                    <input v-model="applicationPlatform" type="radio" id="Battle" name="application_platform"
                        value="Battle" />
                    <label for="Battle" class="application_platform">Battle.net</label>
                </div>

                <label for="application_search" class="application_subtitle">Search your application game</label>
                <input v-model="applicationSearch" type="text" name="application_search" id="application_search"
                    class="application_field" placeholder="Searching.." />
                <div class="pop_section d-flex flex-row">
                    <Game v-for="game in games" :key="game.id" @click="selectedGame = game.id"
                        :isSelected="selectedGame == game.id" :title="game.title" :image="game.image"
                        class="game_pop" />
                </div>

                <div class="application_buttons d-flex justify-content-center">
                    <div @click="createApplication" class="button_accent">Save Changes</div>
                    <div class="button_accent">Delete application</div>
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

.application_platforms input[type="radio"] {
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