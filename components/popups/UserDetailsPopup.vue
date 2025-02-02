<script setup lang="ts">
const { user } = defineProps<{
    user: User,
    isOpen: boolean,
}>()

const emit = defineEmits()


const userLanguages = computed<{ [id: number]: boolean }>(() =>
    user.languages ? user.languages.reduce((acc, curr) => ({ ...acc, [curr.id]: true }), {}) : {}
)
const userAge = ref(user.age as number)
const userEmail = ref(user.email)

const loading = ref(false);

const { clear } = useUserSession()

const { data: languages } = useLanguages()

const langSearch = ref("")
const showedLanguages = computed(() => {
    if (languages.value)
        return langSearch.value ? languages.value.filter((language) => language.title.toLowerCase().includes(langSearch.value.toLowerCase())) : languages.value
    return []
})

// TODO rewrite using pinia-colada mutations
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

})
const { mutate: updateAge } = useMutation({
    mutation: (age: number) => {
        return $fetch(`/api/users/${user.id}`, {
            method: "PATCH",
            body: {
                age
            }
        })
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
    }
})

const logout = async () => {
    loading.value = true;
    await clear();
    loading.value = false;
    emit("close");
    navigateTo("/sign-in");
}

</script>

<template>
    <Popup :visible="isOpen" :width="700" class="languagespop">
        <Container>
            <div class="languages_title">Select Languages</div>

            <div class="languages_section">

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input v-model="langSearch" class="languages_input" type="text" name="language_search"
                        id="language_search" placeholder="Search language" />
                    <div class="button_accent">Search</div>
                </div>

                <Row class="g-1">
                    <Col v-for="language in showedLanguages" :key="language.id" @click="toggleLanguage(language.id)"
                        col="6">
                    <div :class="{ language_selected: userLanguages[language.id] }" class="language">{{
                        language.title }}
                    </div>
                    </Col>
                </Row>

                <div class="button_accent">Save Languages</div>

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input @change="updateAge(userAge)" v-model="userAge" class="languages_input" type="text"
                        name="user_age" id="user_age" placeholder="Enter your age number" />
                    <div class="button_accent">Enter</div>
                </div>

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input @change="updateEmail(userEmail)" v-model="userEmail" class="languages_input" type="email"
                        name="user_email" id="user_email" placeholder="New email address" />
                    <div class="button_accent">Change</div>
                </div>

                <div class="languages_field d-flex align-items-center justify-content-between">
                    <input @change="updatePassword('')" class="languages_input" type="password" name="user_password"
                        id="user_password" placeholder="New user password" />
                    <div class="button_accent">Change</div>
                </div>

                <button @click="logout" class="button_accent button_pop">{{ loading ? 'Loading...' : 'Logout'
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