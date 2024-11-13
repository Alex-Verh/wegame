<script lang="ts" setup>
const { fields, submitUrl } = defineProps({
    type: String,
    typeSwitchText: String,
    typeSwitchLink: String,
    submitUrl: String,
    fields: Object,
});

const emit = defineEmits(["submit"]);

const loading = ref(false);
const error = ref("");


const { fetch, loggedIn } = useUserSession()

watchEffect(() => {
    if (loggedIn.value) {
        navigateTo("/")
    }
})
const onSubmit = async (event: Event) => {
    const formData = new FormData(event.target as HTMLFormElement);
    for (const fieldName in fields) {
        const validator = fields[fieldName].validator;
        if (validator && !validator(formData.get(fieldName))) {
            console.log(`Field ${fieldName} is invalid`);
            return;
        }
    }
    try {
        loading.value = true;
        const body: { [key: string]: any } = {}
        for (const [key, value] of formData) {
            body[key] = value
        }
        await $fetch(submitUrl as string, {
            method: 'POST',
            body,
        });
        await fetch();
        console.log('User signed up successfully')
    }
    catch (err) {
        if (err instanceof Error)
            error.value = err.message
    }
    finally {
        loading.value = false;
    }
}

</script>

<template>
    <div class="container-fluid">
        <Row class="g-1">
            <Col col="8">
                <img src="/images/register_image_1.jpg" alt="Friends Gaming" class="form_image">
            </Col>
            <Col col="4">
                <section>
                    <form action="" class="form" @submit.prevent="onSubmit">
                        <div class="form_title">
                            <span class='form_name accent'>{{ type }}</span> to enhance gaming experience
                        </div>
                        <div class="form_fields">
                            <div v-for="(field, name) in fields" :key="name" class="form_field">
                                <label :for="name" class="form_label">{{ field.label }}</label>
                                <input :type="field.type" :name="name" :id="name" class="form_input">
                            </div>
                        </div>
                        <div class="form_buttons d-flex justify-content-between">
                            <button :disabled="loading" type="submit" class="button_accent form_button">
                                {{ loading ? 'Loading...' : type }}
                            </button>
                            <NuxtLink to="/api/auth/google" class="button_accent form_button">
                                Google Account
                            </NuxtLink>
                        </div>
                        <NuxtLink :to="typeSwitchLink" class="form_switch">Switch to {{ typeSwitchText }}
                        </NuxtLink>
                        <div>{{ error }}</div>
                    </form>
                </section>
            </Col>
        </Row>
    </div>
</template>

<style scoped>
.row {
    margin-inline: 0px !important;
}

.container-fluid {
    padding: 0;
}

.form {
    padding: 25px;
    margin-top: 15px;
}

.form_title {
    font-size: 32px;
    color: #fff;
    margin-bottom: 55px;
}

.form_name {
    font-size: 60px;
    font-weight: 700;
}

.form_button {
    width: 100%;
    margin-inline: 3px;
}

.form_switch {
    display: block;
    text-align: center;
    color: #FE9F00;
    text-decoration: underline;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    margin-top: 20px;
}

.form_image {
    width: 100%;
}

.form_field {
    width: 100%;
    margin-bottom: 15px;
    font-size: 16px;
}

.form_label {
    color: #FE9F00;
    display: block;
    font-weight: 600;
    margin-bottom: 8px;
}


.form_input {
    border: 1px solid #444259;
    outline: none;
    background: none;
    width: 100%;
    padding: 10px 15px;
    color: #fff;
}
</style>