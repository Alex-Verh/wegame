<script lang="ts" setup>
const isOpen = ref(false)

const { fetch } = useUserSession()

async function signin(event: SubmitEvent) {
    const target = event.target as HTMLFormElement

    await $fetch('/api/login', {
        method: 'POST',
        body: {
            email: target.email.value,
            password: target.password.value,
        },
    }).then(() => {
        fetch()
        isOpen.value = false
        console.log('User logged in successfully')

    }).catch((err) => {
        console.log(err)
    })
}
</script>

<template>
    <main>
        <AuthForm title="<span class='form_name accent'>Sign In</span> to continue your journey with us"
            submit-button-text="Sign In" :fields="[
                {
                    name: 'email',
                    type: 'email',
                    label: 'Email',
                },
                {
                    name: 'password',
                    type: 'password',
                    label: 'Password',
                },
            ]" switch-text="Sign Up" switch-link="/signup" :on-submit="signin" />
    </main>
</template>

<style scoped></style>