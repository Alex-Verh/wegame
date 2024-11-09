<script lang="ts" setup>
definePageMeta({
    middleware: "unauthorized"
})

</script>

<template>
    <AuthForm type="Sign Up" submitUrl="/api/auth/sign-up" typeSwitchText="Sign In" typeSwitchLink="/sign-in" :fields="{
        nickname: {
            type: 'text',
            label: 'Nickname',
            validator: (value: String) => value.length >= 3
        },
        email: {
            type: 'email',
            label: 'Email',
            validator: (value: String) => value.includes('@')
        },
        password: {
            type: 'password',
            label: 'Password',
            validator: (value: String) => value.length >= 8
        },
    }" />
</template>

<style scoped></style>