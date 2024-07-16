<script setup>
defineProps(["title"])
</script>

<template>
    <section>
        <img src="" alt="" class="form_image">
        <form action="" class="form">
            <div class="form_title" v-html="title"></div>
            <div class="form_fields">
                <label for="" class="form_field_label">Username</label>
                <input type="text" name="" class="form_field" id="">
                <label for="" class="form_field_label">Email</label>
                <input type="text" name="" class="form_field" id="">
                <label for="" class="form_field_label">Password</label>
                <input type="text" name="" class="form_field" id="">
            </div>
            <div class="form_buttons">
                <button class="form_button">Sign Up</button>
                <button class="form_button">Sign Up with Google</button>
            </div>
            <div class="form_switch">Switch to Sign In</div>
        </form>
    </section>
</template>