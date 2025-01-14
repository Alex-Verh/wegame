<script setup lang="ts">
import { useRouter } from 'vue-router';
const userData = inject<Ref<User>>("userData");

const { loggedIn, clear } = useUserSession()
const applicationPopup = usePopup()
const profilePopup = usePopup()
const router = useRouter();

const handleApplicationClick = () => {
    loggedIn ? applicationPopup.open() : router.push('/login');
}

const logout = async () => {
    await clear();
    navigateTo("/sign-in");
}
</script>

<template>
    <ProfilePopup :isOpen="profilePopup.isOpen.value" :user="userData" @close="profilePopup.close" />
    <ApplicationPopup :isOpen="applicationPopup.isOpen.value" @close="applicationPopup.close" isNew />
    <nav class="navigation">
        <div class="container-fluid">
            <Row>
                <Col col="3">
                <div class="logo d-flex align-items-center justify-content-center">
                    <img src="/images/logo.png" alt="Logo" class="logo_icon">
                    <NuxtLink to="/" class="logo_text">
                        WE<span class="accent">GAME</span>
                    </NuxtLink>
                </div>
                </Col>
                <Col col="7">
                <div class="links">
                    <div class="links_row_accent d-flex justify-content-left">
                        <NuxtLink to="/" class="link">Terms and Conditions</NuxtLink>
                        <NuxtLink to="/" class="link">Support</NuxtLink>
                        <NuxtLink to="/" class="link">FAQ</NuxtLink>
                        <div class="language_dropdown">
                            <!-- <img src="" alt="" class="language_icon"> -->
                            <div class="language_text">English (US)</div>
                            <!-- <img src="" alt="" class="language_icon"> -->
                        </div>
                    </div>
                    <div class="links_row d-flex justify-content-around">
                        <NuxtLink to="/#applications" class="link"><img src="" alt="" class="link_icon">Find Friend
                            Quickly</NuxtLink>
                        <button @click="handleApplicationClick()" class="link"><img src="" alt=""
                                class="link_icon">Create Your Application</button>
                        <NuxtLink to="/parties" class="link"><img src="" alt="" class="link_icon">Join A Party
                        </NuxtLink>
                    </div>
                </div>
                </Col>
                <Col col="2">
                <div class="buttons">
                    <NuxtLink v-if="!loggedIn" class="button" to="/sign-up">Register
                    </NuxtLink>
                    <button v-else @click="logout" class="button">Logout</button>
                    <NuxtLink v-if="!loggedIn" class="button_accent" to="/sign-in">Enter Account
                    </NuxtLink>
                    <button v-else @click="profilePopup.open" class="button_accent">View Profile</button>
                </div>
                </Col>
            </Row>
        </div>
    </nav>
</template>

<style scoped>
.navigation {
    color: #B9B8B8;
    background-color: #201F30;
    font-size: 16px;
    box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.25);
}

.navigation .col-2,
.navigation .col-7 {
    padding: 0 !important;
}

.links_row,
.links_row_accent {
    padding: 20px;
}

.links_row_accent {
    background-color: #14131E;
}

.links_row_accent .link {
    margin-left: 35px;
    color: #5c5c5c;
}

.link {
    display: block;
    text-decoration: none;
    background-color: transparent;
    border: none;
    color: inherit;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.link:hover {
    color: #FE9F00;
}

.language_dropdown {
    margin-left: auto;
    margin-right: 0;
}
</style>