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


const toasts = ref<Array<{ id: number; content: string; variant: string }>>([]);

function createToast(content: string, variant: string = 'primary') {
  const id = Date.now();
  console.log("chinazes")
  toasts.value.push({ id, content, variant });

  setTimeout(() => {
    toasts.value = toasts.value.filter((toast) => toast.id !== id);
  }, 5000);
}
</script>


<template>
  <ToastContainer padding="3" bottom="0" end="0" position="fixed" >
      <Toast
        v-for="toast in toasts"
        :key="toast.id"
        :text-color="'white'"
        :background-color="toast.variant"
        :border="0"
        show
        style="margin: 0.7rem;"
      >
        <b-div flex>
          <ToastBody>{{ toast.content }}</ToastBody>
          <CloseButton
            dismiss="toast"
            margin="e-3 auto"
            @click="toasts = toasts.filter((t) => t.id !== toast.id)"
          />
        </b-div>
      </Toast>
  </ToastContainer>
  <NavBar />
  <main>
    <NuxtPage />
  </main>
  <FootBar />
</template>
