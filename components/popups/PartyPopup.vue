<script setup>
const { visible, close } = usePartyPopup()
const { data: games } = await useFetch('/api/games')
</script>

<template>
    <Popup :visible @close="close">
        <Container>
            <div class="party_title">Create Party</div>

            <div class="party_body">
                <label for="party_name" class="party_subtitle">Party Name</label>
                <input type="text" name="party_name" id="party_name" class="party_field" placeholder="Some cool name.." />

                <label for="party_description" class="party_subtitle">Party Description</label>
                <textarea name="party_description" id="party_description" class="party_field party_textarea" placeholder="We will be playing on Faceit.."></textarea>

                <Row>
                    <Col col="6">
                        <label for="party_age" class="party_subtitle">Select age range</label>
                        <div class="d-flex align-items-center party_numbers">
                            <input type="number" min="0" max="99" name="party_minage" id="party_minage" class="party_field party_minifield" placeholder="10">
                            <span> - </span>
                            <input type="number" min="0" max="99" name="party_maxage" id="party_maxage" class="party_field party_minifield" placeholder="99">
                            <span>years old</span>
                        </div>
                    </Col>
                    <Col col="6">
                        <label for="party_members" class="party_subtitle">Max. number of members</label>
                        <div class="d-flex align-items-center party_numbers">
                            <input type="number" min="2" max="30" name="party_members" id="party_members" class="party_field party_minifield" placeholder="5">
                            <span>members</span>
                        </div>
                    </Col>
                </Row>

                <label for="party_search" class="party_subtitle">Select your party game</label>
                <input v-model="partySearch" type="text" name="party_search" id="party_search"
                class="party_field" placeholder="Searching.."/>
                <div class="pop_section d-flex flex-row">
                    <Game v-for="game in games" :key="game.id" :title="game.title" :image="game.image" class="game_pop" />
                </div>

                <div class="party_buttons d-flex justify-content-center">
                    <div class="button_accent">Save Changes</div>
                    <div class="button_accent">See Members</div>
                    <div class="button_accent">Delete Party</div>
                </div>

            </div>
        </Container>
    </Popup>
</template>

<style scoped>
.party {
    width: 1000px;
}

.party_body {
    overflow-y: scroll;
    height: 500px;
    padding: 0 30px;
} 

.party_body::-webkit-scrollbar {
    width: 3px;
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

.party_minifield {
    width: 70px !important;
    margin-inline-end: 20px;
}

.party_minifield:nth-of-type(2) {
    margin-inline-start: 20px;
}

.party_textarea {
    resize: none;
    height: 100px;
}

.party_numbers {
    color: #444259;
}

.pop_section {
    margin-top: 20px;
    height: 130px;
    overflow-x: auto;
    overflow-y: hidden;
}

.game_pop {
    margin-inline-end: 25px;
    flex-shrink: 0;
    height: 100%;
    font-size: 12px !important;
    min-width: auto !important;
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