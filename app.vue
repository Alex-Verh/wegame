<script lang="ts" setup>
interface User {
  id: number;
  nickname: string;
  email: string;
  profilePic: string;
  languages: Array<{ languageId: number }>;
  platforms: Array<{ platformId: number, link: string }>
  applications: Array<any>,
  parties: Array<any>
}
const userData = ref({});

const { user } = useUserSession();

watchEffect(async () => {
  if (user.value)
    userData.value = await $fetch(`/api/users/${user.value.id}`);
  else
    userData.value = {};
})

provide("userData", userData);
</script>


<template>
  <Popups />
  <NavBar />
  <main>
    <NuxtPage />
  </main>
  <FootBar />
</template>
