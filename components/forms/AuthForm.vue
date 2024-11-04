<script setup>

defineProps({
    title: String,
    submitButtonText: String,
    fields: Array,
    onSubmit: Function,
    switchText: String,
    switchLink: String,
});


const showPopup = ref(false); 
</script>

<template>
    <b-container fluid>
        <b-row class="g-1">
            <b-col cols="8">
                <img src="/images/register_image_1.jpg" alt="Friends Gaming" class="form_image">
            </b-col>
            <b-col cols="4">
                <section>
                    <ProfilePopUp :showPopup="showPopup" @close="showPopup = false" />

                    <form action="" class="form" @submit.prevent="onSubmit($event)">
                        <div class="form_title" v-html="title"></div>
                        <div class="form_fields">
                            <div v-for="field in fields" class="form_field">
                                <label :for="field.name" class="form_label">{{ field.label }}</label>
                                <input :type="field.type" :name="field.name" class="form_input" :id="field.name">
                            </div>
                        </div>
                        <div class="form_buttons d-flex justify-content-between">
                            <button type="submit" class="button_accent form_button">
                                {{ submitButtonText }}
                            </button>
                            <button class="button_accent form_button">Google Account</button>
                            <button class="button_accent form_button" @click="showPopup = true">Show PopUp</button>
                        </div>
                        <div class="form_switch">Switch to <NuxtLink :to="switchLink">{{ switchText }}</NuxtLink>
                        </div>
                    </form>
                </section>
            </b-col>
        </b-row>
    </b-container>
</template>

<style scoped>
.row {
    margin-inline: 0px !important;
}

.container-fluid {
    padding: 0;
}

.form {
    padding: 25px;
    margin-top: 15px;
}

.form_title {
    font-size: 36px;
    color: #fff;
    margin-bottom: 55px;
}

.form_name {
    font-size: 64px;
    font-weight: 700;
}

.form_button {
    width: 100%;
    margin-inline: 3px;
}

.form_switch {
    text-align: center;
    color: #FE9F00;
    text-decoration: underline;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    margin-top: 20px;
}

.form_image {
    width: 100%;
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
</style>