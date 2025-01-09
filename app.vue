<script lang="ts" setup>

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
