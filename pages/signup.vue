<template>
    <main>
        <AuthForm title="<span class='form_name accent'>Sign Up</span> to continue your journey with us"
            submit-button-text="Sign Up" :fields="[
                {
                    name: 'nickname',
                    type: 'text',
                    label: 'Nickname',
                },
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
            ]" switch-text="Sign In" switch-link="/signin" />
    </main>
</template>

<style scoped></style>