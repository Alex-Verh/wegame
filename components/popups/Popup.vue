<script setup lang="ts">
import { VueFinalModal } from "vue-final-modal";

const emit = defineEmits<{ close: [] }>();

const { class: cls } = defineProps<{ class: string }>();
</script>

<template>
  <VueFinalModal
    clickToClose
    escToClose
    class="popup_overlay"
    :contentClass="['popup', cls]"
  >
    <img
      class="popup_close"
      src="~/assets/icons/close.svg"
      alt="Close Popup"
      @click.self="emit('close')"
    />
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
  background: #0e0d18;
  border: 1px solid #fe9f00;
  color: #fff;
  padding: 25px 35px;
  position: relative;
  z-index: 1000;
  width: 1000px;

  @media screen and (max-width: 1000px) {
    width: 800px;
  }

  @media screen and (max-width: 860px) {
    padding: 15px 20px;
  }

  @media screen and (max-width: 580px) {
    width: 400px;
  }

  @media screen and (max-width: 410px) {
    padding: 7px 10px;
    width: 250px;
  }
}

.popup_close {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 15px;
  height: 15px;
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;

  @media screen and (max-width: 500px) {
    width: 8px;
    height: 8px;
  }
}

.user-links {
  width: 500px !important;
}

.members {
  width: 700px !important;
}
</style>
