<script setup lang="ts">
const { loggedIn } = useUserSession()

</script>

<template>
    <ApplicationPopup v-if="loggedIn" />
    <PartyPopup v-if="loggedIn" />
    <UserDetailsPopup />
    <PartyMembersPopup />
    <UserLinksPopup />
    <ProfilePopup />
</template>