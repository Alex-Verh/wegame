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
    locales: [
      { code: 'en', iso: 'en-US', file: 'en.ts' },
      { code: 'ro', iso: 'ro-RO', file: 'ro.ts' },
      { code: 'ru', iso: 'ru-RU', file: 'ru.ts' }
    ],
    lazy: true,
    defaultLocale: 'en'
  },
  css: ["~/assets/styles/base.css"],
});
