<script setup>
</script>

<template>
    <section class="section">
        <div class="section_title">Applications - Find One</div>

        <div class="search_bar">
            <b-row class="g-3">
                <b-col cols="4">
                    <input type="text" name="find_player" placeholder="Find by name" class="search_field" />
                </b-col>
                <b-col cols="4">
                    <div class="search_filter">Filter by platform</div>
                </b-col>
                <b-col cols="4">
                    <div class="search_filter">Filter by language</div>
                </b-col>
                <b-col cols="4">
                    <div class="search_filter">Filter by game</div>
                </b-col>
                <b-col cols="3">
                    <div class="search_filter">Filter by age</div>
                </b-col>
                <b-col cols="5">
                    <div class="search_filter">Filter by ranking</div>
                </b-col>
            </b-row>
        </div>

        <div class="applications">
            <div class="application">
                <img src="" alt="" class="application_img">
                <div class="applicator_info">
                    <div class="applicator_name">xxx_destroyer_x89</div>
                    <div class="applicator_age">21 years old</div>
                    <div class="applicator_location">Russian, English</div>
                </div>
                <div class="application_text">Looking for a cool CS 2 player, preferably higher than gold nova 1 and
                    know russian.</div>
                <img src="" alt="" class="application_game">
            </div>
        </div>
    </section>
</template>

<style scoped>
.games_section {
    margin-top: 120px;
}

.section_title {
    color: #fff;
    font-size: 32px;
    font-weight: 700;
}

.search_bar {
    margin-top: 40px;
    background-color: #201F30;
    padding: 25px;
}

.search_filter, .search_field {
    border: 1px solid #FE9F00;/* Change border color */
    border-radius: 5px; /* Optional: rounded corners */
    padding: 10px; /* Add some padding */
    width: 100%; /* Optional: make it full width */
    color: #FE9F00;
    cursor: pointer;
}

.search_field  {
  background: transparent; /* Remove background */
  font-size: 16px; /* Adjust font size */
  color: #fff; /* Text color */
}

/* Placeholder styling */
.search_field::placeholder {
  color: #FE9F00; /* Placeholder text color */
  opacity: 1; /* Ensure the color is fully opaque */
}

.search_field:focus {
  outline: none; /* Remove default outline */
  box-shadow: 0 0 5px #fea100a5; /* Optional: add a shadow */
}
</style>