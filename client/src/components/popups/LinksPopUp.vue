<script setup>
import PopUp from './PopUpComponent.vue';


defineProps(["showPopup"])


</script>

<template>
    <PopUp :visible="showPopup" :width="500" class="linkpop">
    <b-container>
        <div class="linkpop_title">User Links</div>

        <label for="steam_url" class="linkpop_subtitle">Steam Profile</label>
        <input type="text" name="steam_url" id="steam_url" class="linkpop_field" />

        <label for="epic_url" class="linkpop_subtitle">Epic Games</label>
        <input type="text" name="epic_url" id="epic_url" class="linkpop_field" />

        <label for="origin_url" class="linkpop_subtitle">Origin Profile</label>
        <input type="text" name="origin_url" id="origin_url" class="linkpop_field" />

        <label for="xbox_url" class="linkpop_subtitle">Xbox Profile</label>
        <input type="text" name="xbox_url" id="xbox_url" class="linkpop_field" />

        <label for="playstation_url" class="linkpop_subtitle">Playstation Profile</label>
        <input type="text" name="playstation_url" id="playstation_url" class="linkpop_field" />

        <div class="button_accent">Save Changes</div>
    </b-container>
    </PopUp>
</template>

<style scoped>

.linkpop_title {
    text-align: center;
    font-size: 28px;
}

.linkpop_subtitle {
    font-size: 18px;
    margin: 15px 0;
    display: block;
}

.linkpop_field {
    background: none;
    border: 1px solid #444259;
    width: 100%;
    color: #FE9F00;
    resize: none;
    outline: none;
    font-size: 16px;
    padding: 10px;
}

.linkpop .button_accent {
    width: 175px;
    margin: 15px auto;
}
</style>