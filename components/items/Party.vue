<script setup>
</script>

<template>
    <div class="party">
        <div class="party_main">
            <b-row>
                <b-col cols="10">
                    <div class="party_name">Fancy Idiots </div>
                    <div class="party_description">Accept friendly people to play on Mirage and Dust II on gold nova
                        ranks during the gameplay we will be hosting a server on RUST. Accept friendly people to play on
                        Mirage and Dust II on gold nova
                        ranks during the gameplay we will be hosting a server on RUST.
                    </div>
                </b-col>
                <b-col cols="2">
                    <img src="/images/cs_logo.jpg" alt="Counter Strike 2" class="party_icon">
                    <div class="button_accent">Join</div>
                </b-col>
            </b-row>
        </div>
        <div class="party_bottom d-flex justify-content-between">
            <div class="party_location">Russian, French</div>
            <div class="party_players">See players</div>
            <div class="party_players_amount">4 out 5 people</div>
        </div>
    </div>
</template>

<style scoped>
.party {
    background-color: #201F30;
    color: #757575;
    padding: 15px 20px;
}

.party_name {
    color: #FE9F00;
    font-weight: 600;
    font-size: 24px;
    margin-bottom: 25px;
}

.party_icon {
    width: 100%;
    margin-bottom: 25px;
}

.party_bottom {
    margin-top: 20px;
}

.party_players {
    color: #fff;
    text-decoration: underline;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}
</style>