<script setup lang="ts">
defineProps<{
    id: number;
    title: string;
    gameId: number;
    platformId: number;
    leaderId: number;
    description: string | null;
    minAge: number;
    maxAge: number;
    membersLimit: number;
    game: Game;
    platform: Platform;
    members: {
        userId: number;
    }[]
}>()

const partyMembersPopup = usePopup()
</script>

<template>
    <PartyMembersPopup :isOpen="partyMembersPopup.isOpen.value" @close="partyMembersPopup.close" />
    <div class="party">
        <div class="party_main">
            <Row>
                <Col col="10">
                <div class="party_name"> {{ title }} </div>
                <div class="party_description"> {{ description }} </div>
                </Col>
                <Col col="2">
                <img :src="game.icon" :alt="game.title" class="party_icon">
                <div class="button_accent">Join</div>
                </Col>
            </Row>
        </div>
        <div class="party_bottom d-flex justify-content-between">
            <div class="party_platform">{{ platform.title }}</div>
            <div class="party_players" @click="partyMembersPopup.open">See players</div>
            <div class="party_players_amount">{{ members?.length + 1 }} out {{ membersLimit }} people</div>
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

.party_platform,
.party_players,
.party_players_amount {
    flex: 1;
}

.party_players {
    color: #fff;
    text-decoration: underline;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
    text-align: center;
}

.party_players_amount {
    text-align: right;
}
</style>