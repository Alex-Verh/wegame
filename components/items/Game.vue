<script setup lang="ts">
defineProps<{
  id: number;
  title: string;
  image: string;
  isSelected?: boolean;
}>();
</script>

<template>
  <div
    class="game"
    :class="{ game_selected: isSelected }"
    @click="useToast(title)"
  >
    <img :src="image" alt="GameName" class="game_image" />
    <div class="game_title">{{ title }}</div>
    <img class="game_mark" src="~/assets/icons/mark.svg" alt="Selected" />
  </div>
</template>

<style scoped>
.game {
  position: relative;
  /* Position for the content */
  overflow: hidden;
  /* Hide overflow to ensure neat appearance */
  border: 1px solid #fe9f00;
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;
  font-size: 18px;
  min-width: 398px;
  aspect-ratio: 16 / 9;

  @media screen and (max-width: 1400px) {
    min-width: 298px;
  }

  @media screen and (max-width: 990px) {
    min-width: 200px;
  }

  @media screen and (max-width: 770px) {
    min-width: 150px;
  }

  @media screen and (max-width: 440px) {
    min-width: 100px;
  }
}

.game_selected {
  background-color: #14ff00;
}

.game:hover {
  box-shadow: 0 0 10px #fea100a5;
  /* Optional: add a shadow */
}

.game_image {
  width: 100%;
  /* Ensure the image takes up the full width of the column */
  height: 100%;
  transition: transform 0.3s ease;
  /* Smooth transition for image */
}

.game_selected .game_image {
  opacity: 40%;
}

.game:hover .game_image {
  transform: scale(1.1);
  opacity: 40%;
  /* Scale up the image wrapper */
}

.game_title,
.game_mark {
  position: absolute;
  /* Position the content over the image */
  top: 45%;
  /* Positioning it as needed */
  left: 50%;
  /* Center horizontally */
  transform: translateX(-50%);
  /* Centering adjustment */
  opacity: 0;
  /* Start hidden */
  transition: opacity 0.3s ease;
  /* Smooth transition for opacity */
  color: #fff;

  @media screen and (max-width: 990px) {
    font-size: 14px;
  }

  @media screen and (max-width: 770px) {
    font-size: 12px;
  }

  @media screen and (max-width: 440px) {
    font-size: 10px;
  }
}

.game_mark {
  width: 10%;
  height: 10%;
}

.game:hover .game_title {
  opacity: 1;
  /* Show the content on hover */
}

.game_selected:hover .game_title {
  opacity: 0 !important;
}

.game_selected .game_mark {
  opacity: 1;
}
</style>
