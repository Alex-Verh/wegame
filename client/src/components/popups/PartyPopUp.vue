<script setup>
import PopUp from './PopUpComponent.vue';
import Game from '../GameComponent.vue';


defineProps(["showPopup"])


</script>

<template>
    <PopUp :visible="showPopup">
    <b-container>
        <div class="partypop_title">Create Party</div>
        <label for="party_name" class="partypop_subtitle">Party Name</label>
        <textarea name="party_name" id="party_name" class="partypop_field"></textarea>
        <label for="party_description" class="partypop_subtitle">Party Description</label>
        <textarea name="party_description" id="party_description" class="partypop_field"></textarea>
        <label for="" class="partypop_subtitle">Select application game</label>
        <div class="pop_section d-flex flex-row">
            <Game class="game_pop"/>
            <Game class="game_pop"/>
            <Game class="game_pop"/>
            <Game class="game_pop"/>
            <Game class="game_pop"/>
            <Game class="game_pop"/>
        </div>
        <div class="partypop_buttons d-flex justify-content-center">
            <div class="button_accent">Save Changes</div>
            <div class="button_accent">See Members</div>
            <div class="button_accent">Delete Party</div>
        </div>
    </b-container>
    </PopUp>
</template>

<style scoped>
.partypop {
    width: 1000px;
}

.partypop_title {
    text-align: center;
    font-size: 34px;
}

.partypop_subtitle {
    font-size: 18px;
    margin: 20px 0;
    display: block;
}

.partypop_field {
    background: none;
    border: 1px solid #444259;
    width: 100%;
    color: #fff;
    resize: none;
    font-size: 20px;
    padding: 10px;
}

.partypop_field:last-of-type {
    height: 100px;
}

.pop_section {
    height: 130px;
    overflow-x: auto;
    overflow-y: hidden;
}

.game_pop {
    margin-inline-end: 25px;
    /* height: 100%; */
    flex-shrink: 0;
    width: 20%;
}

.game_pop:last-of-type {
    margin-inline-end: 0px;
}

.partypop_buttons {
    margin-top: 20px;
}

.partypop_buttons .button_accent {
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