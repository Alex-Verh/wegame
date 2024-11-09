<script lang="ts" setup>
definePageMeta({
    middleware: "unauthorized"
})
</script>

<template>
    <AuthForm type="Sign In" submitUrl="/api/auth/sign-in" typeSwitchText="Sign Up" typeSwitchLink="/sign-up" :fields="{
        email: {
            type: 'email',
            label: 'Email',
            validator: (value: String) => value.includes('@')
        },
        password: {
            type: 'password',
            label: 'Password',
            validator: (value: String) => !!value
        },
    }" />
</template>

<style scoped></style>