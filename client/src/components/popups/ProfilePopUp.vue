<script setup>
import PopUp from './PopUpComponent.vue';
import Game from '../GameComponent.vue';


defineProps(["showPopup"])


</script>

<template>
    <PopUp :visible="showPopup" class="profile_pop">
    <b-container>
        <b-row class="g-5">
            <b-col cols="3">
                <img class="pfp_pop" src="../../assets/profile.jpg" alt="Profile Username">
                <p class="username_pop accent">xxx_destroyer_x89</p>
                <div class="button_accent button_pop">Edit Links</div>
                <div class="button_accent button_pop">Edit Details</div>
            </b-col>
            <b-col cols="9">
                <div class="games_pop">
                <b-container>
                    <div class="pop_title">Games</div>
                    <b-row class="g-3">
                        <b-col cols="3">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="3">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="3">
                            <Game class="game_pop"/>
                        </b-col>
                        <b-col cols="3">
                            <Game class="game_pop"/>
                        </b-col>

                    </b-row>

                    <div class="pop_title">Applications - <span class="pop_createapp">Create New</span></div>
                    <div class="pop_section d-flex flex-row">
                        <div class="pop_box d-inline-flex align-items-center">
                            Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                        </div>
                        <div class="pop_box d-inline-flex align-items-center">
                            Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                        </div>
                        <div class="pop_box d-inline-flex align-items-center">
                            Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                        </div>
                        <div class="pop_box d-inline-flex align-items-center">
                            Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                        </div>
                    </div>

                    <div class="pop_title">Parties</div>
                    <div class="pop_section d-flex flex-row">
                        <div class="pop_box">
                            <div class="pop_party_title accent">Juicy Bastards</div>
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                            <div>Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.</div>
                        </div>
                        <div class="pop_box">
                            <div class="pop_party_title accent">Juicy Bastards</div>
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                            <div>Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.</div>
                        </div>
                        <div class="pop_box">
                            <div class="pop_party_title accent">Juicy Bastards</div>
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                            <div>Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.</div>
                        </div>
                        <div class="pop_box">
                            <div class="pop_party_title accent">Juicy Bastards</div>
                            <img src="../../assets/trash.svg" class="pop_box_trash" alt="Delete">
                            <div>Looking for a cool CS 2 player, preferably higher than gold nova 1 and know russian.</div>
                        </div>
                    </div>
                </b-container>
                </div>

            </b-col>
        </b-row>
    </b-container>
    </PopUp>
</template>

<style scoped>
.pfp_pop {
    width: 100%;
    border: 1px solid #FE9F00;
}

.pop_title {
    font-size: 24px;
    margin-bottom: 20px;
    margin-top: 10px;
}

.pop_createapp {
    text-decoration: underline;
    font-size: 16px;
    cursor: url('../../assets/cursor-pointer.svg'), pointer;
}

.game_pop {
    width: 100%;
    font-size: 12px !important;
}

.username_pop {
    font-size: 24px;
    text-align: center;
}

.button_pop {
    width: 100%;
    margin-bottom: 15px;
}

.pop_section {
    height: 130px;
    overflow-x: auto;
    overflow-y: hidden;
}

.pop_box {
    background-color: #201F30;
    width: 300px;
    margin-inline-end: 25px;
    height: 100%;
    padding: 10px 25px;
    flex-shrink: 0;
    cursor: url('../../assets/cursor-pointer.svg'), pointer;
    position: relative;
}

.pop_box:hover {
    background-color: #b100007e;
    transition: opacity 0.3s ease;
}

.pop_box_trash {
  position: absolute;
  right: auto;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.pop_box:hover .pop_box_trash {
  opacity: 1;
}

.pop_box:last-of-type {
    margin-inline-end: 0px;
}

.pop_party_title {
    font-weight: 600;
    text-align: center;
    margin-bottom: 5px;
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

/* Selection color */
::-moz-selection { /* Code for Firefox */
    color: #000;
    background: #201F30;
  }
  
</style>