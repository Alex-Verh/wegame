<script setup lang="ts">
const { authorId } = defineProps<{
    id: number;
    authorId: number;
    gameId: number;
    text: string;
    platformId: number;
    ranking: string | null;
    game: Game;
    platform: Platform;
}>()


const { data: author } = useQuery({
    key: () => ["users", authorId],
    query: () => useRequestFetch()(`/api/users/${authorId}`) as Promise<User>,
})


const profilePopup = usePopup("userProfile")

</script>

<template>
    <div class="application" @click="profilePopup.open">
        <ProfilePopup v-if="author" :modalId="profilePopup.modalId" :user="author" @close="profilePopup.close" />
        <Row>
            <Col col="1">
            <img :src="author?.profilePic as string" alt="Profile Picture" class="application_img">
            </Col>
            <Col col="2">
            <div class="applicator_info">
                <div class="applicator_name accent">{{ author ? author.nickname : "loading..." }}</div>
                <div class="applicator_age">{{ author ? author.age : "loading..." }}</div>
                <div class="applicator_location">{{ author ? author.languages.map(language =>
                    language.title).join(', ') : "loading..." }}</div>
            </div>
            </Col>
            <Col col="8">
            <div class="application_text d-flex align-items-center">
                {{ text }}
            </div>
            </Col>
            <Col col="1">
            <img :src="game.icon" alt="Counter Strike 2" class="application_game">
            </Col>
        </Row>
    </div>
</template>

<style scoped>
.application {
    background-color: #201F30;
    margin-bottom: 20px;
    padding: 15px;
    color: #fff;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.applicator_info {
    font-size: 13px;
}

.applicator_name {
    font-size: 20px;
}

.application_text {
    font-size: 20px;
    height: 100%;
}

.application_game {
    width: 100%;
}
</style>