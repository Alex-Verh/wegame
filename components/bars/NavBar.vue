<script setup lang="ts">
import ApplicationPopup from "../popups/ApplicationPopup.vue";

const { loggedIn, clear } = useUserSession();

const { locale, setLocale } = useI18n();

const selectedLanguage = ref(locale.value || "en");

const { data: userData } = useCurrentUser();

const profilePopup = usePopup("myProfile");

const router = useRouter();
const localePath = useLocalePath();

const appPopup = useModal({
  component: ApplicationPopup,
  attrs: {
    onClose: () => {
      appPopup.close();
    },
  },
});

const logout = async () => {
  await clear();
  router.push(localePath("sign-in"));
};
</script>

<template>
  <nav class="navigation">
    <ProfilePopup
      v-if="userData"
      :modalId="profilePopup.modalId"
      :user="userData"
      @close="profilePopup.close"
    />
    <div class="container-fluid">
      <Row>
        <Col col="3">
          <div class="logo d-flex align-items-center justify-content-center">
            <img src="/images/logo.png" alt="Logo" class="logo_icon" />
            <NuxtLinkLocale to="/" class="logo_text">
              WE<span class="accent">GAME</span>
            </NuxtLinkLocale>
          </div>
        </Col>
        <Col col="7">
          <div class="links">
            <div
              class="links_row_accent d-flex align-items-center justify-content-left"
            >
              <NuxtLinkLocale to="/" class="link"
                ><span class="link_help">{{ $t("terms") }}</span>
              </NuxtLinkLocale>
              <NuxtLinkLocale to="/" class="link"
                ><span class="link_help">{{
                  $t("support")
                }}</span></NuxtLinkLocale
              >
              <NuxtLinkLocale to="/" class="link"
                ><span class="link_help">{{ $t("faq") }}</span></NuxtLinkLocale
              >
              <div
                class="language_dropdown d-flex justify-center align-items-center"
              >
                <label for="language_select">
                  <img
                    src="~/assets/icons/language.svg"
                    alt="Language"
                    class="language_icon"
                  />
                </label>
                <select
                  name="language_select"
                  id="language_select"
                  class="language_select"
                  v-model="selectedLanguage"
                  @change="setLocale($event.target?.value)"
                >
                  <option class="language_option" value="en">
                    English (US)
                  </option>
                  <option class="language_option" value="ru">
                    Русский (РУ)
                  </option>
                  <option class="language_option" value="ro">
                    Română (RO)
                  </option>
                </select>
              </div>
            </div>
            <div
              class="links_row d-flex align-items-center justify-content-around"
            >
              <NuxtLinkLocale
                to="/#applications"
                class="link d-flex align-items-center"
              >
                <img src="~/assets/icons/clock.svg" alt="" class="link_icon" />
                <span class="link_text">{{
                  $t("searchPlayers")
                }}</span></NuxtLinkLocale
              >
              <button
                @click="appPopup.open"
                class="link d-flex align-items-center"
              >
                <img
                  src="~/assets/icons/application.svg"
                  alt=""
                  class="link_icon"
                />
                <span class="link_text">{{ $t("application") }}</span>
              </button>
              <NuxtLinkLocale
                to="parties"
                class="link d-flex align-items-center"
              >
                <img src="~/assets/icons/party.svg" alt="" class="link_icon" />
                <span class="link_text">{{ $t("party") }}</span>
              </NuxtLinkLocale>
            </div>
          </div>
        </Col>
        <Col col="2">
          <div class="buttons">
            <NuxtLinkLocale v-if="!loggedIn" class="button" to="sign-up"
              >{{ $t("register") }}
            </NuxtLinkLocale>
            <button v-else @click="logout" class="button">
              {{ $t("logout") }}
            </button>
            <NuxtLinkLocale v-if="!loggedIn" class="button_accent" to="sign-in"
              >{{ $t("account") }}
            </NuxtLinkLocale>
            <button v-else @click="profilePopup.open" class="button_accent">
              {{ $t("view") }}
            </button>
          </div>
        </Col>
      </Row>
    </div>
  </nav>
</template>

<style scoped>
.navigation {
  color: #b9b8b8;
  background-color: #201f30;
  font-size: 16px;
  box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.25);

  @media screen and (max-width: 1200px) {
    font-size: 12px;
  }

  @media screen and (max-width: 900px) {
    font-size: 10px;
  }
}

.buttons {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.buttons .button,
.buttons .button_accent {
  flex: 1; /* Each box will take equal height */
  padding: none !important;
}

.navigation .col-2,
.navigation .col-7 {
  padding: 0 !important;
}

.links {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.links .links_row,
.links .links_row_accent {
  flex: 1;
  padding-inline: 20px;

  @media screen and (max-width: 900px) {
    padding-inline: 10px;
  }
}

.links_row_accent {
  background-color: #14131e;
}

.links_row_accent .link {
  margin-left: 35px;
  color: #5c5c5c;
}

.link {
  display: block;
  text-decoration: none;
  background-color: transparent;
  border: none;
  color: inherit;
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;
}

.link:hover {
  color: #fe9f00;
}

.link_text,
.language_select {
  @media screen and (max-width: 600px) {
    font-size: 8px;
  }
}

.link_icon,
.language_icon {
  margin-inline-end: 7px;
  @media screen and (max-width: 900px) {
    height: 10px;
  }
  @media screen and (max-width: 750px) {
    display: none;
  }
}

.link_help {
  @media screen and (max-width: 750px) {
    display: none;
  }
}

.language_dropdown {
  margin-left: auto;
  margin-right: 0;
}

.language_select {
  -webkit-appearance: none;
  appearance: none;
  background-color: transparent;
  border: none;
  color: inherit;
  padding: 0 8px;
  outline: none !important;
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer !important;
}

.language_option {
  background: #14131e;
  border: none;
  color: inherit;
}
</style>
