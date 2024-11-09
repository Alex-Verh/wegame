<script setup lang="ts">
const { loggedIn } = useUserSession()
const applicationPopup = useApplicationPopup()
const profilePopup = useProfilePopup()
</script>

<template>
    <nav class="navigation">
        <b-container fluid>
            <b-row>
                <b-col cols="3">
                    <div class="logo d-flex align-items-center justify-content-center">
                        <img src="/images/logo.png" alt="Logo" class="logo_icon">
                        <NuxtLink to="/" class="logo_text">
                            WE<span class="accent">GAME</span>
                        </NuxtLink>
                    </div>
                </b-col>
                <b-col cols="7">
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
                            <button class="link"><img src="" alt="" class="link_icon">Find Friend Quickly</button>
                            <button @click="applicationPopup.open" class="link"><img src="" alt=""
                                    class="link_icon">Create Your Application</button>
                            <button class="link"><img src="" alt="" class="link_icon">Join A Party</button>
                        </div>
                    </div>
                </b-col>
                <b-col cols="2">
                    <div class="buttons">
                        <button class="button">See Messages
                        </button>
                        <NuxtLink v-if="!loggedIn" class="button_accent" to="/sign-in">Enter Account
                        </NuxtLink>
                        <button v-else @click="profilePopup.open" class="button_accent">View Profile</button>
                    </div>
                </b-col>
            </b-row>
        </b-container>
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