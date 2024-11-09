<script setup>
defineProps(["title", "author"])
</script>

<template>
    <div class="application">
        <b-row>
            <b-col cols="1">
                <img src="/images/profile.jpg" alt="Profile Picture" class="application_img">
            </b-col>
            <b-col cols="2">
                <div class="applicator_info">
                    <div class="applicator_name accent">xxx_destroyer_x89</div>
                    <div class="applicator_age">21 years old</div>
                    <div class="applicator_location">Russian, English</div>
                </div>
            </b-col>
            <b-col cols="8">
                <div class="application_text d-flex align-items-center">
                    Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.
                </div>
            </b-col>
            <b-col cols="1">
                <img src="/images/cs_logo.jpg" alt="Counter Strike 2" class="application_game">
            </b-col>
        </b-row>
    </div>
</template>

<style scoped>
.application {
    background-color: #201F30;
    margin-bottom: 20px;
    padding: 15px;
    color: #fff;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.applicator_info {
    font-size: 13px;
}

.applicator_name {
    font-size: 20px;
}

.application_text {
    font-size: 20px;
    height: 100%;
}
</style>