<script lang="ts" setup>
const { fields, submitUrl } = defineProps<{
  type: string;
  typeSwitchText: string;
  typeSwitchLink: string;
  submitUrl: string;
  fields: {
    [key: string]: {
      label: string;
      type: string;
      validator?: (value: any) => boolean;
    };
  };
}>();

defineEmits<{ submit: [] }>();

const loading = ref(false);
const error = ref("");

const { fetch, loggedIn } = useUserSession();

watchEffect(() => {
  if (loggedIn.value) {
    navigateTo("/");
  }
});
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
    const body: { [key: string]: any } = {};
    for (const [key, value] of formData) {
      body[key] = value;
    }
    await $fetch(submitUrl as string, {
      method: "POST",
      body,
    });
    await fetch();
    useToast("Logged in successfully", "success");
  } catch (err) {
    if (err instanceof Error) {
      useToast(err.message, "danger");
    }
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="container-fluid">
    <Row class="g-1">
      <Col col="12" class="col-lg-8">
        <Carousel
          id="form_carousel"
          class="form_carousel"
          indicators
          fade
          touch
          :interval="4500"
        >
          <CarouselItem>
            <img
              src="/images/register_image_1.jpg"
              class="d-block w-100"
              alt="Friends Gaming"
            />
          </CarouselItem>
          <CarouselItem>
            <img
              src="/images/register_image_2.jpg"
              class="d-block w-100"
              alt="Friends Gaming"
            />
          </CarouselItem>
          <CarouselItem>
            <img
              src="/images/register_image_3.jpg"
              class="d-block w-100"
              alt="Friends Gaming"
            />
          </CarouselItem>
        </Carousel>
      </Col>

      <Col col="12" class="col-lg-4">
        <section>
          <form action="" class="form" @submit.prevent="onSubmit">
            <div class="form_title">
              <span class="form_name accent">{{ type }}</span>
              {{
                type == $t("signup") ? $t("signupHeader") : $t("signinHeader")
              }}
            </div>
            <div class="form_fields">
              <div
                v-for="(field, name) in fields"
                :key="name"
                class="form_field"
              >
                <label :for="name as string" class="form_label">{{
                  field.label
                }}</label>
                <input
                  :type="field.type"
                  :name="name as string"
                  :id="name as string"
                  class="form_input"
                />
              </div>
            </div>
            <div class="form_buttons d-flex justify-content-between">
              <button
                :disabled="loading"
                type="submit"
                class="button_accent form_button"
              >
                {{ loading ? $t("loading") + "..." : type }}
              </button>
              <NuxtLink
                external
                to="/api/auth/google"
                class="button_accent form_button"
              >
                {{ $t("googleAccount") }}
              </NuxtLink>
            </div>
            <NuxtLinkLocale :to="typeSwitchLink" class="form_switch"
              >{{ $t("switchTo") }} {{ typeSwitchText }}
            </NuxtLinkLocale>
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

.form_carousel {
  width: 100%;
  height: 100%;
}

.container-fluid {
  padding: 0;
}

.form {
  padding: 25px;
  margin-top: 15px;
  @media screen and (max-width: 991px) {
    padding: 25px 155px;
  }
  @media screen and (max-width: 720px) {
    padding: 25px;
  }
}

.form_title {
  font-size: 32px;
  color: #fff;
  margin-bottom: 55px;

  @media screen and (max-width: 1350px) {
    font-size: 25px;
  }

  @media screen and (max-width: 1150px) {
    margin-bottom: 35px;
    font-size: 20px;
  }

  @media screen and (max-width: 955px) {
    margin-bottom: 15px;
    font-size: 18px;
  }
  @media screen and (max-width: 991px) {
    margin-bottom: 55px;
    font-size: 32px;
  }

  @media screen and (max-width: 720px) {
    margin-bottom: 15px;
    font-size: 18px;
  }
}

.form_name {
  font-size: 60px;
  font-weight: 700;

  @media screen and (max-width: 1350px) {
    font-size: 48px;
  }
  @media screen and (max-width: 1150px) {
    font-size: 32px;
  }

  @media screen and (max-width: 955px) {
    font-size: 20px;
  }

  @media screen and (max-width: 991px) {
    font-size: 60px;
  }
  @media screen and (max-width: 720px) {
    font-size: 20px;
  }
}

.form_button {
  width: 100%;
  margin-inline: 3px;

  @media screen and (max-width: 1350px) {
    font-size: 14px;
  }
  @media screen and (max-width: 1150px) {
    font-size: 12px;
  }

  @media screen and (max-width: 1020px) {
    font-size: 8px;
  }

  @media screen and (max-width: 991px) {
    font-size: 16px;
  }
  @media screen and (max-width: 720px) {
    font-size: 12px;
  }
}

.form_switch {
  display: block;
  text-align: center;
  color: #fe9f00;
  text-decoration: underline;
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;
  margin-top: 20px;

  @media screen and (max-width: 1020px) {
    font-size: 10px;
    margin-top: 10px;
  }

  @media screen and (max-width: 991px) {
    margin-top: 20px;
    font-size: 16px;
  }
  @media screen and (max-width: 720px) {
    font-size: 12px;
  }
}

.form_field {
  width: 100%;
  margin-bottom: 15px;
  font-size: 16px;

  @media screen and (max-width: 1350px) {
    font-size: 14px;
  }

  @media screen and (max-width: 991px) {
    font-size: 16px;
  }
  @media screen and (max-width: 720px) {
    font-size: 14px;
  }
}

.form_label {
  color: #fe9f00;
  display: block;
  font-weight: 600;
  margin-bottom: 8px;
  @media screen and (max-width: 720px) {
    font-size: 12px;
  }
}

.form_input {
  border: 1px solid #444259;
  outline: none;
  background: none;
  width: 100%;
  padding: 10px 15px;
  color: #fff;

  @media screen and (max-width: 955px) {
    font-size: 14px;
    padding: 7px 8px;
  }
}
</style>
