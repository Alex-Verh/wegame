<script setup lang="ts">
import { VueFinalModal } from 'vue-final-modal';

const { width = 1000 } = defineProps<{
  width?: number,
}>()

const emit = defineEmits<{ close: [] }>();


</script>

<template>
  <VueFinalModal clickToClose escToClose class="popup_overlay" contentClass="popup"
    :contentStyle="{ width: width + 'px' }">
    <img class="popup_close" src="~/assets/icons/close.svg" alt="Close Popup" @click.self="emit('close')" />
    <slot></slot>
  </VueFinalModal>
</template>



<style>
.popup_overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup {
  background: #0E0D18;
  border: 1px solid #FE9F00;
  color: #fff;
  padding: 25px 35px;
  position: relative;
  z-index: 1000;
}

.popup_close {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 15px;
  height: 15px;
  cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}
</style>
