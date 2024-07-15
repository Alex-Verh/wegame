<script setup>
</script>

<template>
    <section class="section">
        <div class="section_title">
            Popular Games - Select One
        </div>
        <div class="games">
            <b-row class="g-5">
                <b-col cols="4" class="d-flex justify-content-center">
                    <div class="game">
                        <img src="../../assets/csgo.jpg" alt="GameName" class="game_image">
                        <div class="game_title">Counter Strike 2</div>
                    </div>
                </b-col>
                <b-col cols="4" class="d-flex justify-content-center">
                    <div class="game">
                        <img src="../../assets/csgo.jpg" alt="GameName" class="game_image">
                        <div class="game_title">Counter Strike 2</div>
                    </div>
                </b-col><b-col cols="4" class="d-flex justify-content-center">
                    <div class="game">
                        <img src="../../assets/csgo.jpg" alt="GameName" class="game_image">
                        <div class="game_title">Counter Strike 2</div>
                    </div>
                </b-col><b-col cols="4" class="d-flex justify-content-center">
                    <div class="game">
                        <img src="../../assets/csgo.jpg" alt="GameName" class="game_image">
                        <div class="game_title">Counter Strike 2</div>
                    </div>
                </b-col><b-col cols="4" class="d-flex justify-content-center">
                    <div class="game">
                        <img src="../../assets/csgo.jpg" alt="GameName" class="game_image">
                        <div class="game_title">Counter Strike 2</div>
                    </div>
                </b-col><b-col cols="4" class="d-flex justify-content-center">
                    <div class="game">
                        <img src="../../assets/csgo.jpg" alt="GameName" class="game_image">
                        <div class="game_title">Counter Strike 2</div>
                    </div>
                </b-col>
            </b-row>
        </div>
    </section>
</template>

<style scoped>

.games {
    margin-top: 30px;
}

.game {
  position: relative; /* Position for the content */
  overflow: hidden; /* Hide overflow to ensure neat appearance */
  border: 1px solid #FE9F00;
  cursor: pointer;
}

.game_image {
  width: 100%; /* Ensure the image takes up the full width of the column */
  transition: transform 0.3s ease; /* Smooth transition for image */
}

.game:hover .game_image {
  transform: scale(1.1); /* Scale up the image wrapper */
}

.game_title {
  position: absolute; /* Position the content over the image */
  top: 45%; /* Positioning it as needed */
  left: 50%; /* Center horizontally */
  transform: translateX(-50%); /* Centering adjustment */
  opacity: 0; /* Start hidden */
  font-size: 18px;
  transition: opacity 0.3s ease; /* Smooth transition for opacity */
  color: #fff;
}

.game:hover .game_title {
  opacity: 1; /* Show the content on hover */
}


</style>