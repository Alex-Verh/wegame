<script>
export default {
  name: 'PopupWrapper',
  props: {
    visible: {
      type: Boolean,
      default: false,
    }
  },
  watch: {
    visible(val) {
      if (val) {
        document.body.classList.add('no-scroll');
      } else {
        document.body.classList.remove('no-scroll');
      }
    }
  },
  methods: {
    close() {
      this.$emit('close');
    }
  }
}
</script>

<template>
<div class="popup_overlay" v-if="visible" @click.self="close">
    <div class="popup">
    <img class="popup_close" src="../assets/close.svg" alt="Close PopUp" @click.self="close" />
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
    cursor: url('../assets/cursor-pointer.svg'), pointer;
}
</style>
