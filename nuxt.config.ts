// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  modules: [
    "@vue-final-modal/nuxt",
    "usebootstrap",
    "nuxt-auth-utils",
    "nuxt-nodemailer",
    "@scalar/nuxt",
    "@pinia/colada-nuxt",
    "@pinia/nuxt",
    "@nuxtjs/i18n",
  ],
  runtimeConfig: {
    databaseUrl: "",
    secretKey: "",
    oauth: {
      google: {
        clientId: "",
        clientSecret: "",
      },
      discord: {
        clientId: "",
        clientSecret: "",
      },
    },
  },
  nodemailer: {
    from: '"Wegame" <wegame@mail.com>',
    host: "smtp.gmail.com",
    port: 587,
    auth: {
      user: "",
      pass: "",
    },
  },
  devtools: { enabled: true },
  components: [
    {
      path: "~/components",
      pathPrefix: false,
    },
  ],
  nitro: {
    experimental: {
      openAPI: true,
    },
  },
  i18n: {
    strategy: 'prefix',
    locales: [
      { code: 'en', iso: 'en-US', file: 'en.ts' },
      { code: 'ro', iso: 'ro-RO', file: 'ro.ts' },
      { code: 'ru', iso: 'ru-RU', file: 'ru.ts' }
    ],
    lazy: true,
    defaultLocale: 'en',
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_redirected',
      redirectOn: 'root'
    },
    customRoutes: 'config',
    pages: {
      "sign-up": {
        en: '/sign-up', 
        ru: '/регистрация',
        ro: '/inregistrare'
      },
      "sign-in": {
        en: '/sign-in', 
        ru: '/вход',
        ro: '/logare'
      },
      "parties": {
        en: '/parties', 
        ru: '/команды',
        ro: '/echipe'
      }
    }
  },
  css: ["~/assets/styles/base.css"],
});
