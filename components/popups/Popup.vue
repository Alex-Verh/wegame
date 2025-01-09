<script setup>
const { visible } = defineProps({
  visible: {
    type: Boolean,
    default: false,
  },
  width: {
    type: Number,
    default: 1000,
  }
})

const emit = defineEmits(['close']);

watchEffect(() => {
  if (!document) return;
  if (visible) {
    document.body.classList.add('no-scroll');
  } else {
    document.body.classList.remove('no-scroll');
  }
})
const close = () => {
  emit('close');
}
</script>

<template>
  <div class="popup_overlay" v-show="visible" @click.self="close">
    <div class="popup" :style="{ width: width + 'px' }">
      <img class="popup_close" src="~/assets/icons/close.svg" alt="Close Popup" @click.self="close" />
      <slot></slot>
    </div>
  </div>
</template>



<style scoped>
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
