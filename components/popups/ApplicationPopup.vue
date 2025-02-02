<script setup lang="ts">

const { application } = defineProps<{
    isNew: boolean,
    isOpen: boolean,
    application?: Application,
}>()

const emit = defineEmits()

const { data: games } = useGames()
const { data: platforms } = usePlatforms()

const { loggedIn } = useUserSession()

const gamesSearch = ref("")
const showedGames = computed(() =>
    gamesSearch.value ?
        games.value?.filter((game) => game.title.toLowerCase().includes(gamesSearch.value.trim().toLowerCase())) :
        games.value
)


const appText = ref("")
const appRank = ref("")
const appGame = ref(application?.gameId || 0)
const appPlatform = ref(application?.platformId || 0)

const queryCache = useQueryCache()

interface ApplicationData {
    text: string, ranking: string, gameId: number, platformId: number
}

const { mutate: createApplication, isLoading: loading } = useMutation({
    mutation: (app: ApplicationData) => {
        if (!loggedIn) throw new Error('Login required')
        if (!app.text.trim()) throw new Error('Title is required')
        if (!app.gameId) throw new Error('Game is required')
        if (!app.platformId) throw new Error('Platform is required')
        return $fetch('/api/applications', {
            method: "POST",
            body: {
                ...app
            }
        })
    },

    async onSuccess(application) {
        await queryCache.invalidateQueries({ key: ['users', application.authorId, "applications"] })

        appText.value = ""
        appRank.value = ""
        appGame.value = 0
        appPlatform.value = 0

        useToast(`Application "${application.text}" created.`)
        emit("close")
    },

    onError(err) {
        console.error(err)
        useToast(err.message)
    }
})

</script>

<template>
    <Popup :visible="isOpen">
        <Container>
            <div class="application_title">Create Application</div>

            <div class="application_body">

                <label for="application_description" class="application_subtitle">Write an application message</label>
                <textarea v-model="appText" name="application_description" id="application_description"
                    class="application_field application_textarea" placeholder="I am looking for a friend.."></textarea>

                <label for="application_rank" class="application_subtitle">Describe your game rank</label>
                <input v-model="appRank" type="text" name="application_rank" id="application_rank"
                    class="application_field" placeholder="Silver III" />

                <label for="application_platforms" class="application_subtitle">Select Game Platform</label>
                <div class="application_platforms">
                    <template v-for="platform in platforms" :key="platform.id">
                        <input v-model="appPlatform" type="radio" :id="`${platform.title}+${platform.id}`"
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
                        <input v-model="appGame" type="radio" :id="`${game.title}+${game.id}`" name="application_game"
                            :value="game.id" />
                        <label :for="`${game.title}+${game.id}`">
                            <Game v-bind="game" class="game_pop" :isSelected="game.id === appGame" />
                        </label>
                    </template>
                </div>

                <div class="application_buttons d-flex justify-content-center">
                    <button v-if="isNew"
                        @click="createApplication({ text: appText, ranking: appRank, gameId: appGame, platformId: appPlatform })"
                        class="button_accent">Save Changes</button>
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

.pop_section label:last-of-type {
    margin-inline-end: 0px;
}

.game_pop {
    flex-shrink: 0;
    height: 100%;
    min-width: auto !important;
    font-size: 12px !important;
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
</style>