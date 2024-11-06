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

const signIn = async (formData: FormData) => {

    await $fetch('/api/auth/sign-in', {
        method: 'POST',
        body: {
            email: formData.get('email'),
            password: formData.get('password'),
        },
    }).then(() => {
        fetch()
        console.log('User logged in successfully')

    }).catch((err) => {
        console.log(err)
    })
}

</script>

<template>
    <AuthForm type="Sign In" typeSwitchText="Sign Up" typeSwitchLink="/sign-up" :fields="{
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
    }" @submit="signIn" />
</template>

<style scoped></style>