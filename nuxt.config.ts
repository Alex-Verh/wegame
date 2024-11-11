// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  runtimeConfig: {
    databaseUrl: "",
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
  devtools: { enabled: true },
  components: [
    {
      path: "~/components",
      pathPrefix: false,
    },
  ],
  css: ["~/assets/styles/base.css"],
  modules: ["usebootstrap", "nuxt-auth-utils"],
});
