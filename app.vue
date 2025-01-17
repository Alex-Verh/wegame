<script lang="ts" setup>

const userData = ref({});
const games = await useFetch('/api/games');
const platforms = await useFetch('/api/platforms');
const languages = await useFetch('/api/languages');

provide("user", userData);
provide("games", games);
provide("platforms", platforms);
provide("languages", languages);

const { user } = useUserSession();

watchEffect(async () => {
  if (user.value)
    userData.value = await $fetch(`/api/users/${user.value.id}`);
  else
    userData.value = {};
})


const toasts = useState("toasts", () => []);
</script>


<template>
  <ToastContainer padding="3" bottom="0" end="0" position="fixed">
    <Toast v-for="toast in toasts" :key="toast.id" :text-color="'white'" :background-color="toast.variant" :border="0"
      show style="margin: 0.7rem;">
      <b-div flex>
        <ToastBody>{{ toast.content }}</ToastBody>
        <CloseButton dismiss="toast" margin="e-3 auto" @click="toasts = toasts.filter((t) => t.id !== toast.id)" />
      </b-div>
    </Toast>
  </ToastContainer>
  <NavBar />
  <main>
    <NuxtPage />
  </main>
  <FootBar />
</template>
