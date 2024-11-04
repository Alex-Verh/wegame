<script setup>
defineProps(["showPopup"])
</script>

<template>
    <PopUp :visible="showPopup" :width="700" class="languagespop">
        <b-container>
            <div class="languages_title">Select Languages</div>

            <div class="languages_section">

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input class="languages_input" type="text" name="language_search" id="language_search"
                        placeholder="Search language" />
                    <div class="button_accent">Search</div>
                </div>

                <b-row class="g-1">
                    <b-col cols="6">
                        <div class="language">English</div>
                    </b-col>
                    <b-col cols="6">
                        <div class="language">Russian</div>
                    </b-col>
                    <b-col cols="6">
                        <div class="language">Ivrish</div>
                    </b-col>
                    <b-col cols="6">
                        <div class="language">Huivrish</div>
                    </b-col>
                    <b-col cols="6">
                        <div class="language language_selected">Latin</div>
                    </b-col>
                    <b-col cols="6">
                        <div class="language">Bomboclat</div>
                    </b-col>
                </b-row>

                <div class="button_accent">Save Languages</div>

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input class="languages_input" type="text" name="user_age" id="user_age"
                        placeholder="Enter your age number" />
                    <div class="button_accent">Enter</div>
                </div>

            </div>
        </b-container>
    </PopUp>
</template>

<style scoped>
.languages_title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 30px;
}

.languages_field {
    height: 55px;
    margin-bottom: 15px;
}

.languages_field .button_accent {
    background-color: #fff !important;
    height: 100%;
    margin: 0 !important;
}

.languages_input {
    border: 1px solid #444259;
    outline: none;
    background: none;
    font-size: 24px;
    width: 100%;
    color: #fff;
    height: 100%;
    padding-inline: 10px;
}

.language {
    border: 1px solid #444259;
    text-align: center;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    padding: 5px 0;
    font-size: 20px;
}

.language_selected {
    border: 1px solid #FE9F00;
    color: #FE9F00;
    background-color: #201F30;
}

.languages_section .button_accent {
    width: 175px;
    margin: 25px auto;
}
</style>