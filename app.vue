<script lang="ts" setup>
import { ModalsContainer } from 'vue-final-modal';

const toasts = useState<Toast[]>("toasts", () => []);

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
  <ModalsContainer />
  <NavBar />
  <main>
    <NuxtPage />
  </main>
  <FootBar />
</template>
