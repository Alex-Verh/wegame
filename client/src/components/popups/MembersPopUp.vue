<script setup>
import PopUp from './PopUpComponent.vue';


defineProps(["showPopup"])


</script>

<template>
    <PopUp :visible="showPopup" :width="700" class="memberspop">
    <b-container>
        <div class="memberspop_title">Party Members</div>

        <div class="memberspop_section">
            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>

            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>

            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>

            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>

            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>

            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>

            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>

            <div class="memberspop_member d-flex align-items-center justify-content-between">
                <span class="memberspop_name">
                    @alllexlelfef
                </span>
                <div>
                    <div class="button_accent">See User</div>
                    <div class="button_accent">Kick</div>
                </div>
            </div>
        </div>


        <div class="button_accent">Kick All</div>
    </b-container>
    </PopUp>
</template>

<style scoped>

.memberspop_title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 30px;
}

.memberspop_section {
    height: 300px;
    overflow-y: auto;
    margin-bottom: 30px;
}

.memberspop_member {
    border: 1px solid #444259;
    padding:  0 0 0 15px;
    margin-bottom: 20px;
}

.memberspop_member:last-of-type {
    margin-bottom: 0px;
}

.memberspop_name {
    font-size: 26px;
    color: #FE9F00;
}

.memberspop_member .button_accent {
    margin: 0 auto 0 0!important;
    display: inline-block;
    width: 100px !important;
}

.memberspop_member .button_accent:first-of-type {
    background-color: #fff;
}

.memberspop_member .button_accent:last-of-type {
    background-color: #CF1E1E;
}

.memberspop .button_accent {
    width: 175px;
    margin: 15px auto;
}
</style>