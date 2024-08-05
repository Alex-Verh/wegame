<script setup>
import PopUp from './PopUpComponent.vue';
import Game from '../GameComponent.vue';


defineProps(["showPopup"])


</script>

<template>
    <PopUp :visible="showPopup" class="profile_pop">
    <b-container>
        <b-row class="g-5">
            <b-col cols="2">
                <img class="pfp_pop" src="../../assets/profile.jpg" alt="Profile Username">
            </b-col>
            <b-col cols="10">
                <div class="games_pop">
                <b-container>
                    <div class="pop_title">Games</div>
                    <b-row class="g-3">
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="2">
                            <Game class="game_pop"/>
                        </b-col>
                    </b-row>
                </b-container>
                </div>

            </b-col>
        </b-row>
    </b-container>
    </PopUp>
</template>

<style scoped>
.pfp_pop {
    width: 175px;
    height: 175px;
    border: 1px solid #FE9F00;
}

.pop_title {
    font-size: 24px;
    margin-bottom: 20px;
}

.game_pop {
    width: 125px;
    height: 70px;
}
</style>