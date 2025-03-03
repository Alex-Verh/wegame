<script setup lang="ts">
import ApplicationPopup from './ApplicationPopup.vue';
import PartyPopup from './PartyPopup.vue';
import UserDetailsPopup from './UserDetailsPopup.vue';
import UserLinksPopup from './UserLinksPopup.vue';

const { user } = defineProps<{
    user: User
}>()

defineEmits()

const { user: sessionUser } = useUserSession()
const isOwnProfile = computed(() => user.id === sessionUser.value?.id)

const { handleFileInput: onPicInput, files: profilePic } = useFileStorage()

const { data: userGames } = useQuery({
    key: () => ["users", user.id, "games"],
    query: () => useRequestFetch()(`/api/games`, { query: { userId: user.id } }) as Promise<Game[]>
})

const { data: userApplications } = useQuery({
    key: () => ["users", user.id, "applications"],
    query: () => useRequestFetch()(`/api/applications`, { query: { authorId: user.id } }) as Promise<Application[]>,
})
const { data: userOwnParties } = useQuery({
    key: () => ["users", user.id, "parties", "own"],
    query: () => useRequestFetch()(`/api/parties`, { query: { leaderId: user.id } }) as Promise<Party[]>,
})
const { data: userMemberParties } = useQuery({
    key: () => ["users", user.id, "parties", "member"],
    query: () => useRequestFetch()(`/api/parties`, { query: { memberId: user.id } }) as Promise<Party[]>,
})

const userParties = computed(() => [...(userOwnParties.value || []), ...(userMemberParties.value || [])])

const queryCache = useQueryCache()
const { mutate: updatePic } = useMutation({
    mutation: (file: typeof profilePic.value) => {
        return $fetch(`/api/users/${user.id}`, {
            method: "PATCH",
            body: {
                profilePic: file
            }
        })
    },
    onSuccess: async () => {
        await queryCache.invalidateQueries({ key: ['users', user.id], exact: true })
        useToast("Profile picture updated")
    },
    onError: (err) => {
        useToast(err.message)
    }
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
        <ApplicationPopup :modalId="applicationPopup.modalId" @close="applicationPopup.close" />
        <Container>
            <Row class="g-5">
                <Col col="3">
                <div class="profile_img">
                    <img class="profile_picture" :src="user.profilePic as string" alt="Profile Username" />
                    <input type="file" @input="onPicInput" accept="image/*" style="" />
                    <img v-if="isOwnProfile" @click="updatePic(profilePic)" src="~/assets/icons/upload.svg"
                        class="profile_upload" alt="Upload" />
                </div>
                <p class="profile_username accent">{{ user.nickname }}</p>
                <template v-if="isOwnProfile">
                    <button @click="userLinksPopup.open" class="button_accent button_pop">{{ $t('editContact')
                        }}</button>
                    <button @click="userDetailsPopup.open" class="button_accent button_pop">{{ $t('settings')
                        }}</button>
                </template>
                <template v-else>
                    <button @click="userLinksPopup.open" class="button_accent button_pop">{{ $t('seeContacts')
                        }}</button>
                </template>
                </Col>
                <Col col="9">
                <div class="profile_games">
                    <Container>
                        <div class="profile_subtitle">{{ $t('games') }}</div>
                        <Row class="g-3">
                            <template v-for="game in userGames">
                                <Col col="3">
                                <Game :key="game.id" v-bind="game" class="profile_game" />
                                </Col>
                            </template>
                        </Row>

                        <div class="profile_subtitle">{{ $t('applications') }} <span @click="applicationPopup.open"
                                v-if="isOwnProfile" class="profile_createapp">- {{ $t('createNew')
                                }}</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="application in userApplications" :key="application.id"
                                @click="isOwnProfile && editApplication(application)"
                                class="profile_box d-inline-flex align-items-center">
                                <div>{{ application.text }}</div>
                                <img v-if="isOwnProfile" src="~/assets/icons/edit.svg" class="profile_edit"
                                    alt="Edit" />
                            </div>
                        </div>

                        <div class="profile_subtitle">{{ $t('parties') }} <span @click="partyPopup.open"
                                v-if="isOwnProfile" class="profile_createapp">- {{ $t('createNew')
                                }}</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="party in userParties" :key="party.id" @click="isOwnProfile && editParty(party)"
                                class="profile_box">
                                <img v-if="sessionUser?.id === party.leaderId" src="~/assets/icons/leader.svg"
                                    class="profile_party_leader" alt="Leader" />
                                <div class="profile_party_title accent">{{ party.title }}</div>
                                <div>{{ party.description }}</div>
                                <img v-if="isOwnProfile" src="~/assets/icons/edit.svg" class="profile_edit"
                                    alt="Edit" />
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

.profile_img {
    flex-shrink: 0;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    position: relative;
    background-color: #000000;
}

.profile_img:hover .profile_picture {
    opacity: 0.3;
    transition: opacity 0.3s ease;
}

.profile_img:hover .profile_upload {
    opacity: 1 !important;
}

.profile_upload {
    width: 35px;
    top: 45%;
}

.profile_edit {
    top: 40%;
    width: 35px;
}

.profile_edit,
.profile_upload {
    position: absolute;
    transform: translateX(-50%);
    left: 50%;
    transition: opacity 0.1s ease;
    opacity: 0;
}

.profile_subtitle {
    font-size: 24px;
    margin-bottom: 20px;
    margin-top: 10px;
    text-transform: capitalize;
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
    flex-shrink: 0;
    padding: 10px 25px;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    position: relative;
}

.profile_box:hover *:not(.profile_edit) {
    opacity: 0.3;
    transition: all 0.3s ease;
}

.profile_box:hover {
    background-color: #201f3085;
}

.profile_box:hover .profile_edit {
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

.profile_party_leader {
    position: absolute;
    top: 5px;
    left: 5px;
}

/* Scroll */
::-webkit-scrollbar {
    height: 3px;
}
</style>