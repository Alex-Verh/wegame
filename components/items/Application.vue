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
}>();

const { data: author } = useQuery({
  key: () => ["users", authorId],
  query: () => useRequestFetch()(`/api/users/${authorId}`) as Promise<User>,
});

const profilePopup = usePopup("userProfile");
</script>

<template>
  <div class="application" @click="profilePopup.open">
    <ProfilePopup
      v-if="author"
      :modalId="profilePopup.modalId"
      :user="author"
      @close="profilePopup.close"
    />
    <Row>
      <Col col="1">
        <img
          :src="author?.profilePic as string"
          alt=""
          class="application_img"
        />
      </Col>
      <Col col="2">
        <div class="applicator_info">
          <div class="applicator_name accent">
            {{ author ? author.nickname : "loading..." }}
          </div>
          <div class="applicator_age">
            {{ author ? author.age + " years old" : "loading..." }}
          </div>
          <div class="applicator_language">
            {{
              author
                ? author.languages.map((language) => language.title).join(", ")
                : "loading..."
            }}
          </div>
        </div>
      </Col>
      <Col col="8">
        <div class="application_text d-flex align-items-center">
          {{ text }}
        </div>
      </Col>
      <Col col="1">
        <img :src="game.icon" alt="Counter Strike 2" class="application_game" />
      </Col>
    </Row>
  </div>
</template>

<style scoped>
.application {
  background-color: #201f30;
  margin-bottom: 20px;
  padding: 15px;
  color: #fff;
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;
}

.application_img {
  width: 80px;
  height: 80px;
  @media screen and (max-width: 1200px) {
    width: 60px;
    height: 60px;
  }
  @media screen and (max-width: 995px) {
    width: 40px;
    height: 40px;
  }
  @media screen and (max-width: 560px) {
    width: 20px;
    height: 20px;
  }
}

.applicator_info {
  font-size: 13px;

  @media screen and (max-width: 1200px) {
    font-size: 10px;
  }
  @media screen and (max-width: 560px) {
    font-size: 6px;
  }
}

.applicator_name {
  font-size: 20px;
  @media screen and (max-width: 1200px) {
    font-size: 16px;
  }
  @media screen and (max-width: 995px) {
    font-size: 12px;
  }
  @media screen and (max-width: 560px) {
    font-size: 8px;
  }
}

.applicator_language {
  @media screen and (max-width: 995px) {
    display: none;
  }
}

.application_text {
  font-size: 20px;
  height: 100%;
  @media screen and (max-width: 1200px) {
    font-size: 14px;
  }
  @media screen and (max-width: 995px) {
    font-size: 12px;
  }
  @media screen and (max-width: 560px) {
    font-size: 8px;
  }
}

.application_game {
  width: 100%;
  @media screen and (max-width: 460px) {
    display: none;
  }
}
</style>
