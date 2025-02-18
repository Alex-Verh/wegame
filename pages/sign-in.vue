<script lang="ts" setup>
definePageMeta({
    middleware: "unauthorized"
})
</script>

<template>
    <AuthForm :type="$t('signin')" submitUrl="/api/auth/sign-in" :typeSwitchText="$t('signup')" typeSwitchLink="/sign-up" :fields="{
        email: {
            type: 'email',
            label: $t('email'),
            validator: (value: String) => value.includes('@')
        },
        password: {
            type: 'password',
            label: $t('password'),
            validator: (value: String) => !!value
        },
    }" />
</template>

<style scoped></style>