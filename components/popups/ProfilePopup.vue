<script setup lang="ts">
const { user } = defineProps({
    isOpen: Boolean,
    user: Object as PropType<User>
})

const { user: sessionUser } = useUserSession()

const isOwner = computed(() => sessionUser.value?.id === user?.id)
const emit = defineEmits(["close"])
const applicationPopup = usePopup()
const partyPopup = usePopup()
const userDetailsPopup = usePopup()
const userLinksPopup = usePopup()


</script>


<template>
    <ApplicationPopup :isOpen="applicationPopup.isOpen.value" @close="applicationPopup.close" isNew />
    <PartyPopup :isOpen="partyPopup.isOpen.value" @close="partyPopup.close" isNew/>
    <UserDetailsPopup :isOpen="userDetailsPopup.isOpen.value" @close="userDetailsPopup.close" />
    <UserLinksPopup :isOpen="userLinksPopup.isOpen.value" @close="userLinksPopup.close" :isEditable="isOwner" />
    <Popup :visible="isOpen" :style="{ zIndex: 800 }" @close="emit('close')" class="profile">
        <Container>
            <Row class="g-5">
                <Col col="3">
                <img class="profile_picture" :src="user?.profilePic" alt="Profile Username">
                <p class="profile_username accent">{{ user?.nickname }}</p>
                <template v-if="isOwner">
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
                            <Game title="Counter-Strike: Global Offensive" image="/images/csgo.jpg"
                                class="profile_game" @click="useToast('Counter-Strike: Global Offensive', 'info')"/>
                            </Col>
                        </Row>

                        <div class="profile_subtitle">Applications - <span @click="applicationPopup.open"
                                class="profile_createapp">Create
                                New</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="application in user?.applications" :key="application.id"
                                class="profile_box d-inline-flex align-items-center">
                                {{ application.text }}
                                <img src="~/assets/icons/trash.svg" class="profile_box_trash" alt="Delete">
                            </div>
                        </div>

                        <div class="profile_subtitle">Parties - <span @click="partyPopup.open"
                                class="profile_createapp">Create
                                New</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="party in user?.parties" :key="party.id" class="profile_box">
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