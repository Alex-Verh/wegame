<script setup>
import SignForm from '../components/SignForm.vue'
</script>

<template>
    <main>
        <b-container fluid>
            <b-row class="g-1">
                <b-col cols="8">
                    <img src="../assets/register_image_1.jpg" alt="Friends Gaming" class="form_image">
                </b-col>
                <b-col cols="4">
                    <SignForm title="<span class='form_name accent'>Sign In</span> to continue your journey with us" />
                </b-col>
            </b-row>
        </b-container>
    </main>
</template>

<style scoped>
.form_image {
    width: 100%;
}

.container-fluid {
    padding:0;
}
</style>