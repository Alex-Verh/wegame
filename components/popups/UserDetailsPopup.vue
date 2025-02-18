<script setup lang="ts">
const { user } = defineProps<{
    user: User,
}>()

const emit = defineEmits()

const router = useRouter();
const localePath = useLocalePath();

const userLanguages = computed<{ [id: number]: boolean }>(() =>
    user.languages ? user.languages.reduce((acc, curr) => ({ ...acc, [curr.id]: true }), {}) : {}
)
const userAge = ref(user.age as number)
const userEmail = ref(user.email)
const userPassword = ref("")

const loading = ref(false);

const { clear } = useUserSession()

const { data: languages } = useLanguages()

const langSearch = ref("")
const showedLanguages = computed(() => {
    if (languages.value)
        return langSearch.value ? languages.value.filter((language) => language.title.toLowerCase().includes(langSearch.value.toLowerCase())) : languages.value
    return []
})

const queryCache = useQueryCache()

const { mutate: toggleLanguage } = useMutation({
    mutation: (languageId: number) => {
        return $fetch(`/api/users/${user.id}`, {
            method: "PATCH",
            body: {
                languages: {
                    [languageId]: !userLanguages.value[languageId]
                }
            }
        })
    },

    onSuccess: async () => {
        await queryCache.invalidateQueries({ key: ['users', user.id], exact: true })
    },

    onError: (err) => {
        useToast(err.message)
    }

})
const { mutate: updateAge } = useMutation({
    mutation: (age: number) => {
        return $fetch(`/api/users/${user.id}`, {
            method: "PATCH",
            body: {
                age
            }
        })
    },
    onSuccess: async () => {
        await queryCache.invalidateQueries({ key: ['users', user.id], exact: true })
        useToast("Age updated")
    },
    onError: (err) => {
        useToast(err.message)
    }
})

const { mutate: updateEmail } = useMutation({
    mutation: (email: string) => {
        return $fetch(`/api/users/${user.id}`, {
            method: "PATCH",
            body: {
                email
            }
        })
    },
    onSuccess: async () => {
        await queryCache.invalidateQueries({ key: ['users', user.id], exact: true })
        useToast("Email confirmation link sent")
    },
    onError: (err) => {
        useToast(err.message)
    }
})

// TODO: password update
const { mutate: updatePassword } = useMutation({
    mutation: (password: string) => {
        return $fetch(`/api/users/${user.id}`, {
            method: "PATCH",
            body: {
                password
            }
        })
    },
    onSuccess: async () => {
        await queryCache.invalidateQueries({ key: ['users', user.id], exact: true })
        useToast("Password updated")
    },
    onError: (err) => {
        useToast(err.message)
    }
})

const logout = async () => {
    loading.value = true;
    await clear();
    loading.value = false;
    emit("close");
    router.push(localePath('sign-in'));
}

</script>

<template>
    <Popup :width="700" class="languagespop">
        <Container>
            <div class="languages_title">Select Languages</div>

            <div class="languages_section">

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input v-model="langSearch" class="languages_input" type="text" name="language_search"
                        id="language_search" :placeholder="$t('searchLanguage')" />
                    <div class="button_accent">{{ $t('search') }}</div>
                </div>

                <Row class="g-1">
                    <Col v-for="language in showedLanguages" :key="language.id" @click="toggleLanguage(language.id)"
                        col="6">
                    <div :class="{ language_selected: userLanguages[language.id] }" class="language">{{
                        language.title }}
                    </div>
                    </Col>
                </Row>

                <div class="button_accent">Save Languages (todo)</div>

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input @keyup.enter="updateAge(userAge)" v-model="userAge" class="languages_input" type="text"
                        name="user_age" id="user_age" placeholder="Enter your age number" />
                    <div @click="updateAge(userAge)" class="button_accent">{{ $t('enter') }}</div>
                </div>

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input @keyup.enter="updateEmail(userEmail)" v-model="userEmail" class="languages_input"
                        type="email" name="user_email" id="user_email" placeholder="New email address" />
                    <div @click="updateEmail(userEmail)" class="button_accent">{{ $t('change') }}</div>
                </div>

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input @keyup.enter="updatePassword(userPassword)" v-model="userPassword" class="languages_input"
                        type="password" name="user_password" id="user_password" placeholder="New user password" />
                    <div @click="updatePassword(userPassword)" class="button_accent">{{ $t('change') }}</div>
                </div>

                <button @click="logout" class="button_accent button_pop">{{ loading ? $t('loading') + '...' : $t('logout')
                    }}</button>
            </div>
        </Container>
    </Popup>
</template>

<style scoped>
.languages_title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 30px;
}

.languages_field {
    height: 55px;
    margin-bottom: 15px;
}

.languages_field .button_accent {
    background-color: #fff !important;
    height: 100%;
    margin: 0 !important;
}

.languages_input {
    border: 1px solid #444259;
    outline: none;
    background: none;
    font-size: 24px;
    width: 100%;
    color: #fff;
    height: 100%;
    padding-inline: 10px;
}

.language {
    border: 1px solid #444259;
    text-align: center;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    padding: 5px 0;
    font-size: 20px;
}

.language_selected {
    border: 1px solid #FE9F00;
    color: #FE9F00;
    background-color: #201F30;
}

.languages_section .button_accent {
    width: 175px;
    margin: 25px auto;
}
</style>