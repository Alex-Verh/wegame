<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <nav>
        <div class="logo">
            <img src="" alt="" class="logo_icon">
            <div class="logo_text">
                WE
                <span class="accent">GAME</span>
            </div>
        </div>
        <!-- TODO: add <RouterLink to="/"></RouterLink> to links -->
        <div class="links">
            <div class="links_row">
                <div class="link">Terms and Conditions</div>
                <div class="link">Support</div>
                <div class="link">FAQ</div>
                <div class="language_dropdown">
                    <img src="" alt="" class="language_icon">
                    <div class="language_text">English (US)</div>
                </div>
            </div>
            <div class="links_row">
                <div class="link"><img src="" alt="" class="link_icon">Find Friend Quickly</div>
                <div class="link"><img src="" alt="" class="link_icon">Create Your Application</div>
                <div class="link"><img src="" alt="" class="link_icon">Join A Party</div>
            </div>
        </div>
        <div class="buttons">
            <div class="button">See Messages</div>
            <div class="button accent">Enter Account</div>
        </div>

    </nav>
</template>

<style scoped></style>