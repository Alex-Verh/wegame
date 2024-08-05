<script setup>
import ProfilePop from './popups/ProfilePopUp.vue';
import PartyPop from './popups/PartyPopUp.vue'
import { ref } from 'vue';


defineProps(["title"])

const userObj = {
    username: "",
    email_address: "",
    password: ""
}

const signIn = () => {
    console.log("Sign In")
    console.log(userObj)
}

const signGoogle = () => {
    console.log("Sign Google")
    console.log(userObj)
}

const showPopup = ref(false); 
</script>

<template>
    <section>
        <PartyPop :showPopup="showPopup" @close="showPopup = false" />
        
        <form action="" class="form">
            <div class="form_title" v-html="title"></div>
            <div class="form_fields">
                <div class="form_field">
                    <label for="username" class="form_label">Username</label>
                    <input type="text" v-model="userObj.username" name="username" class="form_input" id="username">
                </div>
                <div class="form_field">
                    <label for="email_address" class="form_label">Email</label>
                    <input type="email" v-model="userObj.email_address" name="email_address" class="form_input" id="email_address">
                </div>
                <div class="form_field">
                    <label for="password" class="form_label">Password</label>
                    <input type="password" v-model="userObj.password" name="password" class="form_input" id="password">
                </div>
            </div>
            <div class="form_buttons d-flex justify-content-between">
                <div class="button_accent form_button" v-on:click="signIn()">Sign Up</div>
                <div class="button_accent form_button" v-on:click="signGoogle()">Google Account</div>
                <div class="button_accent form_button" @click="showPopup = true">Show PopUp</div>
            </div>
            <div class="form_switch">Switch to Sign In</div>
        </form>
    </section>
</template>

<style>
.form_name {
    font-size: 64px;
    font-weight: 700;
}
</style>

<style scoped>
.form {
    padding: 25px;
    margin-top: 15px;
}

.form_title {
    font-size: 36px;
    color: #fff;
    margin-bottom: 55px;
}

.form_field {
    width: 100%;
    margin-bottom: 15px;
    font-size: 16px;
}

.form_label {
    color: #FE9F00;
    display: block;
    font-weight: 600;
    margin-bottom: 8px;
}

.form_input {
    border: 1px solid #444259;
    outline: none;
    background: none;
    width: 100%;
    padding: 10px 15px;
    color: #fff;
}

.form_button {
    width: 100%;
    margin-inline: 3px;
}

.form_switch {
    text-align: center;
    color: #FE9F00;
    text-decoration: underline;
    cursor: url('../assets/cursor-pointer.svg'), pointer;
    margin-top: 20px;
}
</style>