<script lang="ts" setup>
definePageMeta({
    middleware: "unauthorized"
})

</script>

<template>
    <AuthForm :type="$t('signup')" submitUrl="/api/auth/sign-up" :typeSwitchText="$t('signin')" typeSwitchLink="sign-in" :fields="{
        nickname: {
            type: 'text',
            label: $t('username'),
            validator: (value: String) => value.length >= 3
        },
        email: {
            type: 'email',
            label: $t('email'),
            validator: (value: String) => value.includes('@')
        },
        password: {
            type: 'password',
            label: $t('password'),
            validator: (value: String) => value.length >= 8
        },
    }" />
</template>

<style scoped></style>