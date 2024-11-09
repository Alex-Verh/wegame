<script setup>

const { visible, close } = useNewApplicationPopup()
const { data: games } = useFetch('/api/games')
</script>

<template>
    <Popup :visible @close="close">
        <b-container>
            <div class="application_title">Create Application</div>
            <label for="application_description" class="application_subtitle">Write an application message</label>
            <textarea name="application_description" id="application_description" class="application_field"></textarea>
            <label for="" class="application_subtitle">Select application game</label>
            <div class="pop_section d-flex flex-row">
                <Game v-for="game in games" :title="game.title" :image="game.image" class="game_pop" />
            </div>
            <div class="application_buttons d-flex justify-content-center">
                <div class="button_accent">Save Changes</div>
                <div class="button_accent">Delete application</div>
            </div>
        </b-container>
    </Popup>
</template>

<style scoped>
.application {
    width: 1000px;
}

.application_title {
    text-align: center;
    font-size: 34px;
}

.application_subtitle {
    font-size: 18px;
    margin: 20px 0;
    display: block;
}

.application_field {
    background: none;
    border: 1px solid #444259;
    width: 100%;
    color: #fff;
    resize: none;
    font-size: 20px;
    padding: 10px;
    height: 100px;
}

.pop_section {
    height: 130px;
    overflow-x: auto;
    overflow-y: hidden;
}

.game_pop {
    margin-inline-end: 25px;
    flex-shrink: 0;
    height: 130px !important;
    font-size: 12px !important;
}

.game_pop:last-of-type {
    margin-inline-end: 0px;
}

.application_buttons {
    margin-top: 20px;
}

.application_buttons .button_accent {
    width: 175px;
    margin-inline: 5px;
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