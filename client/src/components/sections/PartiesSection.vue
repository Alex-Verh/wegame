<script setup>
import SearchBar from '../bars/SearchBar.vue'
</script>

<template>
    <section class="section">
        <div class="section_title">Parties - Find your brothers from another mother</div>

        <SearchBar />

        <div class="parties">
            <div class="party">
                <div class="party_main">
                    <div class="party_name">Fancy Idiots </div>
                    <div class="party_description">Accept friendly people to play on Mirage and Dust II on gold nova
                        ranks during the gameplay we will be hosting a server on RUST. </div>
                    <img src="" alt="" class="party_icon">
                    <button class="join_button">Join</button>
                </div>
                <div class="party_bottom">
                    <div class="party_location">Russian, French</div>
                    <div class="party_players">See players</div>
                    <div class="party_players_amount">4 out 5 people</div>
                </div>
            </div>
        </div>
    </section>
</template>