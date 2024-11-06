<script lang="ts" setup>
const { fields } = defineProps({
    type: String,
    typeSwitchText: String,
    typeSwitchLink: String,
    fields: Object,
});

const emit = defineEmits(["submit"]);

const onSubmit = (event: Event) => {
    const formData = new FormData(event.target as HTMLFormElement);
    for (const fieldName in fields) {
        const validator = fields[fieldName].validator;
        if (validator && !validator(formData.get(fieldName))) {
            console.log(`Field ${fieldName} is invalid`);
            return;
        }
    }
    emit('submit', formData);

}

</script>

<template>
    <b-container fluid>
        <b-row class="g-1">
            <b-col cols="8">
                <img src="/images/register_image_1.jpg" alt="Friends Gaming" class="form_image">
            </b-col>
            <b-col cols="4">
                <section>
                    <form action="" class="form" @submit.prevent="onSubmit">
                        <div class="form_title">
                            <span class='form_name accent'>{{ type }}</span> to continue your journey with us
                        </div>
                        <div class="form_fields">
                            <div v-for="(field, name) in fields" :key="name" class="form_field">
                                <label :for="name" class="form_label">{{ field.label }}</label>
                                <input :type="field.type" :name="name" class="form_input" :id="name">
                            </div>
                        </div>
                        <div class="form_buttons d-flex justify-content-between">
                            <button type="submit" class="button_accent form_button">
                                {{ type }}
                            </button>
                            <div class="button_accent form_button">
                                <NuxtLink to="/api/auth/google">Google Account</NuxtLink>
                            </div>
                        </div>
                        <div class="form_switch">Switch to <NuxtLink :to="typeSwitchLink">{{ typeSwitchText }}
                            </NuxtLink>
                        </div>
                    </form>
                </section>
            </b-col>
        </b-row>
    </b-container>
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
    font-size: 36px;
    color: #fff;
    margin-bottom: 55px;
}

.form_name {
    font-size: 64px;
    font-weight: 700;
}

.form_button {
    width: 100%;
    margin-inline: 3px;
}

.form_switch {
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