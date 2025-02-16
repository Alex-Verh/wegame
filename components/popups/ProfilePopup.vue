<script setup lang="ts">
import ApplicationPopup from './ApplicationPopup.vue';
import PartyPopup from './PartyPopup.vue';
import UserDetailsPopup from './UserDetailsPopup.vue';
import UserLinksPopup from './UserLinksPopup.vue';

const { user } = defineProps<{
    user: User
}>()

const { user: sessionUser } = useUserSession()

const { data: userGames } = useQuery({
    key: () => ["users", user.id, "games"],
    query: () => useRequestFetch()(`/api/games`, { query: { userId: user.id } }) as Promise<Game[]>
})

const { data: userApplications } = useQuery({
    key: () => ["users", user.id, "applications"],
    query: () => useRequestFetch()(`/api/applications`, { query: { authorId: user.id } }) as Promise<Application[]>,
})
const { data: userParties } = useQuery({
    key: () => ["users", user.id, "parties"],
    query: () => useRequestFetch()(`/api/parties`, { query: { leaderId: user.id } }) as Promise<Party[]>,
})


const applicationPopup = useModal({
    component: ApplicationPopup,
    attrs: {
        onClose: () => {
            applicationPopup.close()
        }
    }
})
const partyPopup = useModal({
    component: PartyPopup,
    attrs: {
        onClose: () => {
            partyPopup.close()
        }
    }
})
const userDetailsPopup = usePopup("myUserDetails")
const userLinksPopup = usePopup("myUserLinks")

const applicationEditPopup = useModal({
    component: ApplicationPopup,
    attrs: {
        onClose: () => {
            applicationEditPopup.close()
        }
    }
})

const editApplication = (application: Application) => {
    applicationEditPopup.patchOptions({ attrs: { application } })
    applicationEditPopup.open()
}

const partyEditPopup = useModal({
    component: PartyPopup,
    attrs: {
        onClose: () => {
            partyEditPopup.close()
        }
    }
})

const editParty = (party: Party) => {
    partyEditPopup.patchOptions({ attrs: { party } })
    partyEditPopup.open()
}

</script>

<template>
    <Popup :style="{ zIndex: 800 }" class="profile">
        <UserDetailsPopup :modalId="userDetailsPopup.modalId" @close="userDetailsPopup.close" :user="user" />
        <UserLinksPopup :modalId="userLinksPopup.modalId" @close="userLinksPopup.close" :user="user" />
        <Container>
            <Row class="g-5">
                <Col col="3">
                <img class="profile_picture" :src="user.profilePic as string" alt="Profile Username">
                <p class="profile_username accent">{{ user.nickname }}</p>
                <template v-if="sessionUser?.id === user.id">
                    <button @click="userLinksPopup.open" class="button_accent button_pop">Edit Contact</button>
                    <button @click="userDetailsPopup.open" class="button_accent button_pop">Settings</button>
                </template>
                <template v-else>
                    <button @click="userLinksPopup.open" class="button_accent button_pop">See Contact</button>
                </template>
                </Col>
                <Col col="9">
                <div class="profile_games">
                    <Container>
                        <div class="profile_subtitle">Games</div>
                        <Row class="g-3">
                            <Col col="3">
                            <Game v-for="game in userGames" :key="game.id" v-bind="game" class="profile_game" />
                            </Col>
                        </Row>

                        <div class="profile_subtitle">Applications - <span @click="applicationPopup.open"
                                class="profile_createapp">Create
                                New</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="application in userApplications" :key="application.id"
                                @click="editApplication(application)"
                                class="profile_box d-inline-flex align-items-center">
                                {{ application.text }}
                                <img src="~/assets/icons/trash.svg" class="profile_box_trash" alt="Edit" />
                            </div>
                        </div>

                        <div class="profile_subtitle">Parties - <span @click="partyPopup.open"
                                class="profile_createapp">Create
                                New</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="party in userParties" :key="party.id" @click="editParty(party)"
                                class="profile_box">
                                <div class="profile_party_title accent">{{ party.title }}</div>
                                <img src="~/assets/icons/trash.svg" class="profile_box_trash" alt="Delete">
                                <div>{{ party.description }}</div>
                            </div>
                        </div>
                    </Container>
                </div>
                </Col>
            </Row>
        </Container>
    </Popup>
</template>

<style scoped>
.profile_picture {
    width: 100%;
    border: 1px solid #FE9F00;
}

.profile_subtitle {
    font-size: 24px;
    margin-bottom: 20px;
    margin-top: 10px;
}

.profile_createapp {
    text-decoration: underline;
    font-size: 16px;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.profile_game {
    min-width: 100% !important;
    font-size: 0px !important;
}

.profile_username {
    font-size: 24px;
    text-align: center;
}

.button_pop {
    width: 100%;
    margin-bottom: 15px;
}

.profile_section {
    height: 130px;
    overflow-x: auto;
    overflow-y: hidden;
}

.profile_box {
    background-color: #201F30;
    width: 300px;
    margin-inline-end: 25px;
    height: 100%;
    padding: 10px 25px;
    flex-shrink: 0;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    position: relative;
}

.profile_box:hover {
    background-color: #b100007e;
    transition: opacity 0.3s ease;
}

.profile_box_trash {
    position: absolute;
    right: auto;
    left: 50%;
    transform: translateX(-50%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.profile_box:hover .profile_box_trash {
    opacity: 1;
}

.profile_box:last-of-type {
    margin-inline-end: 0px;
}

.profile_party_title {
    font-weight: 600;
    text-align: center;
    margin-bottom: 5px;
}

/* Scroll */
::-webkit-scrollbar {
    height: 3px;
}
</style>