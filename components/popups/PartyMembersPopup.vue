<script setup lang="ts">
import ProfilePopup from './ProfilePopup.vue';

const { members, leaderId, partyId } = defineProps<{ members: Party["members"], leaderId: number, partyId: number }>()
defineEmits()
const { user } = useUserSession()


const isMember = computed(() => members.find((member) => member.userId === user.value?.id))
const isLeader = computed(() => leaderId === user.value?.id)

const queryCache = useQueryCache()
const { mutate: acceptMember } = useMutation({
    mutation: (userId: number) => {
        return $fetch(`/api/parties/${partyId}`, {
            method: "PATCH",
            body: { members: { [userId]: "accepted" } }
        })
    },
    onSuccess: async () => {
        if (user.value?.id)
            await queryCache.invalidateQueries({ key: ['users', user.value.id, "parties", "own"] })
        useToast('Member accepted')
    },

    onError: (err) => {
        useToast(err.message)
    }
})

const { mutate: denyMember } = useMutation({
    mutation: (userId: number) => {
        return $fetch(`/api/parties/${partyId}`, {
            method: "PATCH",
            body: { members: { [userId]: "denied" } }
        })
    },
    onSuccess: async () => {
        if (user.value?.id)
            await queryCache.invalidateQueries({ key: ['users', user.value.id, "parties", "own"] })
        useToast('member denied')
    },
    onError: (err) => {
        useToast(err.message)
    }
})

const memberPopup = useModal({
    component: ProfilePopup,
    attrs: {
        onClose: () => {
            memberPopup.close()
        }
    }
})

const seeMember = (member: User) => {
    memberPopup.patchOptions({ attrs: { user: member } })
    memberPopup.open()
}


</script>

<template>
    <Popup :width="700" class="members">
        <Container>
            <template v-if="isLeader">
                <div class="members_title">{{ $t('partyRequests') }}</div>
                <div class="members_section">
                    <div v-for="member in members"
                        class="members_member d-flex align-items-center justify-content-between">
                        <template v-if="member.status === 'pending'">
                            <span class="members_name">
                                {{ member.user.nickname }}
                            </span>
                            <div>
                                <button @click="acceptMember(member.userId)" class="button_accent">{{ $t('accept')
                                    }}</button>
                                <button @click="denyMember(member.userId)" class="button_accent">{{ $t('deny')
                                    }}</button>
                            </div>
                        </template>
                    </div>
                </div>
                <button class="button_accent">Accept Everyone</button>
            </template>

            <div class="members_title">{{ $t('partyMembers') }}</div>
            <div class="members_section">
                <div v-for="member in members" class="members_member d-flex align-items-center justify-content-between">
                    <template v-if="member.status === 'accepted'">
                        <span class="members_name">
                            {{ member.user.nickname }}
                        </span>
                        <div>
                            <button @click="seeMember(member.user)" class="button_accent">See User</button>
                            <button v-if="isLeader" @click="denyMember(member.userId)" class="button_accent">{{
                                $t('kick') }}</button>
                        </div>
                    </template>
                </div>
            </div>
            <template v-if="isMember">
                <div class="members_title">{{ $t('discordUrl') }}</div>
                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        https://discord.com/invite/ID
                    </span>
                    <div>
                        <button class="button_accent">{{ $t('navigate') }}</button>
                    </div>
                </div>
            </template>
        </Container>
    </Popup>
</template>

<style scoped>
.members_title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 30px;
}

.members_section {
    max-height: 250px;
    overflow-y: auto;
    scroll-snap-type: y mandatory;
}

.members_member {
    border: 1px solid #444259;
    padding: 0 0 0 15px;
    margin-bottom: 20px;
    scroll-snap-align: start;
}

.members_member:last-of-type {
    margin-bottom: 0px;
}

.members_name {
    font-size: 26px;
    color: #FE9F00;
}

.members_member .button_accent {
    margin: 0 auto 0 0 !important;
    display: inline-flex;
    width: 100px !important;
}

.members_member .button_accent:first-of-type {
    background-color: #fff !important;
}

.members_member .button_accent:last-of-type {
    background-color: #CF1E1E;
}

.members .button_accent {
    width: 175px;
    margin: 15px auto;
}
</style>