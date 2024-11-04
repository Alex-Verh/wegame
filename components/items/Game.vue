<script setup>
</script>

<template>
  <div class="game">
    <img src="/images/csgo.jpg" alt="GameName" class="game_image">
    <div class="game_title">Counter Strike 2</div>
  </div>
</template>

<style scoped>
.game {
  position: relative;
  /* Position for the content */
  overflow: hidden;
  /* Hide overflow to ensure neat appearance */
  border: 1px solid #FE9F00;
  cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
  font-size: 18px;
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

.game:hover .game_image {
  transform: scale(1.1);
  /* Scale up the image wrapper */
}

.game_title {
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
}

.game:hover .game_title {
  opacity: 1;
  /* Show the content on hover */
}
</style>