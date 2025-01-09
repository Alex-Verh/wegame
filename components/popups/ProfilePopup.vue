<script setup lang="ts">
const loading = ref(false);
const userData = inject("userData");

const { clear } = useUserSession()

const { visible, close } = useProfilePopup()
const applicationPopup = useApplicationPopup()
const partyPopup = usePartyPopup()
const userDetailsPopup = useUserDetailsPopup()
const userLinksPopup = useUserLinksPopup()

const logout = async () => {
    loading.value = true;
    await clear();
    loading.value = false;
    close();
    navigateTo("/sign-in");
}
</script>


<template>
    <Popup :visible @close="close" :style="{ zIndex: 800 }" class="profile">
        <Container>
            <Row class="g-5">
                <Col col="3">
                <img class="profile_picture" src="/images/profile.jpg" alt="Profile Username">
                <p class="profile_username accent">{{ userData?.nickname }}</p>
                <button @click="userLinksPopup.open" class="button_accent button_pop">Edit Links</button>
                <button @click="userDetailsPopup.open" class="button_accent button_pop">Edit Details</button>
                <button @click="logout" class="button_accent button_pop">{{ loading ? 'Loading...' : 'Logout'
                    }}</button>
                </Col>
                <Col col="9">
                <div class="profile_games">
                    <Container>
                        <div class="profile_subtitle">Games</div>
                        <Row class="g-3">
                            <Col col="3">
                            <Game title="Counter-Strike: Global Offensive" image="/images/csgo.jpg"
                                class="profile_game" />
                            </Col>
                        </Row>

                        <div class="profile_subtitle">Applications - <span @click="applicationPopup.open"
                                class="profile_createapp">Create
                                New</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="application in userData?.applications" :key="application.id"
                                class="profile_box d-inline-flex align-items-center">
                                {{ application.text }}
                                <img src="~/assets/icons/trash.svg" class="profile_box_trash" alt="Delete">
                            </div>
                        </div>

                        <div class="profile_subtitle">Parties - <span @click="partyPopup.open"
                                class="profile_createapp">Create
                                New</span></div>
                        <div class="profile_section d-flex flex-row">
                            <div v-for="party in userData?.own_parties" :key="party.id" class="profile_box">
                                <div class="profile_party_title accent">Juicy Bastards</div>
                                <img src="~/assets/icons/trash.svg" class="profile_box_trash" alt="Delete">
                                <div>{{ party.title }}</div>
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
    width: 100%;
    font-size: 12px !important;
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

/* Handle */
::-webkit-scrollbar-thumb {
    background: #FE9F00;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
    background: #201F30;
}
</style>