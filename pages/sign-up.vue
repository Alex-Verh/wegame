<script lang="ts" setup>
definePageMeta({
    middleware: "unauthorized"
})

const { fetch, loggedIn } = useUserSession()

watchEffect(() => {
    if (loggedIn.value) {
        navigateTo("/")
    }
})

const signUp = async (formData: FormData) => {

    await $fetch('/api/auth/sign-up', {
        method: 'POST',
        body: {
            nickname: formData.get('nickname'),
            email: formData.get('email'),
            password: formData.get('password'),
        },
    }).then(() => {
        fetch()
        console.log('User registered successfully')
    }).catch((err) => {
        console.log(err)
    })
}
</script>

<template>
    <AuthForm type="Sign Up" typeSwitchText="Sign In" typeSwitchLink="/sign-in" :fields="{
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
    }" @submit="signUp" />
</template>

<style scoped></style>