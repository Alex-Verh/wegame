<script setup>
const { visible, close } = useNewPartyPopup()
const { data: games } = useFetch('/api/games')
</script>

<template>
    <Popup :visible @close="close">
        <b-container>
            <div class="party_title">Create Party</div>
            <label for="party_name" class="party_subtitle">Party Name</label>
            <textarea name="party_name" id="party_name" class="party_field"></textarea>
            <label for="party_description" class="party_subtitle">Party Description</label>
            <textarea name="party_description" id="party_description" class="party_field"></textarea>
            <label for="" class="party_subtitle">Select application game</label>
            <div class="pop_section d-flex flex-row">
                <Game v-for="game in games" :title="game.title" :image="game.image" class="game_pop" />
            </div>
            <div class="party_buttons d-flex justify-content-center">
                <div class="button_accent">Save Changes</div>
                <div class="button_accent">See Members</div>
                <div class="button_accent">Delete Party</div>
            </div>
        </b-container>
    </Popup>
</template>

<style scoped>
.party {
    width: 1000px;
}

.party_title {
    text-align: center;
    font-size: 34px;
}

.party_subtitle {
    font-size: 18px;
    margin: 20px 0;
    display: block;
}

.party_field {
    background: none;
    border: 1px solid #444259;
    width: 100%;
    color: #fff;
    resize: none;
    font-size: 20px;
    padding: 10px;
    outline: none;
}

.party_field:last-of-type {
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
    height: 130px;
    font-size: 12px !important;
}

.game_pop:last-of-type {
    margin-inline-end: 0px;
}

.party_buttons {
    margin-top: 20px;
}

.party_buttons .button_accent {
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