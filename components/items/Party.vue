<script setup lang="ts">
import PartyMembersPopup from '../popups/PartyMembersPopup.vue';

const { id, members, leaderId } = defineProps<{
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
        status: "pending" | "accepted";
    }[]
}>()


const { user } = useUserSession()

const userCanJoin = computed(() => !members.find((member) => member.userId === user.value?.id) && leaderId !== user.value?.id)
const memberCount = computed(() => members.filter((member) => member.status === 'accepted').length)

const queryCache = useQueryCache()
const { mutate: joinParty } = useMutation({
    mutation: (userId: number) => {
        return $fetch(`/api/parties/${id}`, {
            method: "PATCH",
            body: { members: { [userId]: "pending" } }
        })
    },
    onSuccess: async () => {
        useToast('Join request sent')
    },
    onError: (err) => {
        useToast(err.message)
    }
})

const membersPopup = usePopup("partyMembers")

</script>

<template>
    <div class="party">
        <PartyMembersPopup v-if="members" :modalId="membersPopup.modalId" :members="members" :leaderId="leaderId"
            :partyId="id" @close="membersPopup.close" />
        <div class="party_main">
            <Row>
                <Col col="10">
                <div class="party_name"> {{ title }} </div>
                <div class="party_description"> {{ description }} </div>
                </Col>
                <Col col="2">
                <img :src="game.icon" :alt="game.title" class="party_icon">
                <button :disabled="!userCanJoin || !user" @click="joinParty(user!.id)" class="button_accent">{{
                    $t('join') }} </button>
                </Col>
            </Row>
        </div>
        <div class="party_bottom d-flex justify-content-between">
            <div class="party_platform">{{ platform.title }}</div>
            <div class="party_players" @click="membersPopup.open">{{ $t('seePlayers') }}</div>
            <div class="party_players_amount">{{ memberCount }} {{
                $t('out') }} {{ membersLimit }} {{ $t('people')
                }}</div>
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