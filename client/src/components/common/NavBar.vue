<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <nav class="navigation">
            <b-row>
                <b-col cols="3">
                    <div class="logo d-flex align-items-center justify-content-center">
                        <img src="../../assets/logo.png" alt="Logo" class="logo_icon">
                        <div class="logo_text">
                            WE<span class="accent">GAME</span>
                        </div>
                    </div>
                </b-col>
                <b-col cols="7">
                    <!-- TODO: add <RouterLink to="/"></RouterLink> to links -->
                    <div class="links">
                        <div class="links_row_accent d-flex justify-content-left">
                            <div class="link">Terms and Conditions</div>
                            <div class="link">Support</div>
                            <div class="link">FAQ</div>
                            <div class="language_dropdown">
                                <!-- <img src="" alt="" class="language_icon"> -->
                                <div class="language_text">English (US)</div>
                                <!-- <img src="" alt="" class="language_icon"> -->
                            </div>
                        </div>
                        <div class="links_row d-flex justify-content-around">
                            <div class="link"><img src="" alt="" class="link_icon">Find Friend Quickly</div>
                            <div class="link"><img src="" alt="" class="link_icon">Create Your Application</div>
                            <div class="link"><img src="" alt="" class="link_icon">Join A Party</div>
                        </div>
                    </div>
                </b-col>
                <b-col cols="2">
                    <div class="buttons">
                        <div class="button">See Messages</div>
                        <div class="button_accent">Enter Account</div>
                    </div>
                </b-col>
            </b-row>
    </nav>
</template>

<style scoped>

.navigation {
    background-color: #201F30;
    color: #B9B8B8;
    font-size: 16px;
    box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.25);
}

.navigation .col-2, .navigation .col-7 {
    padding: 0 !important;
}

.logo {
    height: 100%;
    margin: 0 auto;
}

.logo_icon {
    height: 60px;
}

.logo_text {
    color: #fff;
    font-size: 48px;
    display: inline-block;
    margin-left: 10px;
}

.accent {
    color: #FE9F00;
}

.links_row, .links_row_accent {
    padding: 20px;
}

.links_row_accent {
    background-color: #14131E;
}

.links_row_accent .link {
    margin-left: 25px;
}

.link {
    cursor: pointer;
}

.link:hover {
    color: #FE9F00;
    }

.language_dropdown {
    margin-left: auto;
    margin-right: 0;
}

.button, .button_accent {
    font-weight: 700;
    text-align: center;
    padding: 20px 0;
    cursor: pointer;
}

.button_accent {
    background-color: #FE9F00;
    color: #000;
}


</style>