<script setup lang="ts">
defineProps<{
  text: string;
  image: string;
  stats?: { parties: number; games: number; players: number };
}>();
</script>

<template>
  <header class="header">
    <Row>
      <Col col="12" class="col-xl-6">
        <div class="header_text">
          <span v-html="text"></span>
        </div>
      </Col>
      <Col col="6" class="d-flex justify-content-center">
        <img :src="image" alt="Friends" class="header_image" />
      </Col>
    </Row>
    <div class="statistics" v-if="stats">
      <Row>
        <Col col="4" class="d-flex align-items-center justify-content-center">
          <div class="statistics_item">
            <div class="item_value">{{ stats.parties }}</div>
            <div class="item_text">{{ $t("parties") }}</div>
          </div>
        </Col>
        <Col col="4" class="d-flex align-items-center justify-content-center">
          <div class="statistics_item">
            <div class="item_value">{{ stats.games }}</div>
            <div class="item_text">{{ $t("games") }}</div>
          </div>
        </Col>
        <Col col="4" class="d-flex align-items-center justify-content-center">
          <div class="statistics_item">
            <div class="item_value">{{ stats.players }}</div>
            <div class="item_text">{{ $t("players") }}</div>
          </div>
        </Col>
      </Row>
    </div>
  </header>
</template>

<style scoped>
.header {
  margin-top: 100px;
  @media screen and (max-width: 400px) {
    margin-top: 50px;
  }
}

.header_text {
  font-size: 58px;
  color: #fff;

  @media screen and (max-width: 800px) {
    font-size: 32px;
    text-align: center;
  }

  @media screen and (max-width: 400px) {
    font-size: 20px;
  }
}

.header_image {
  width: 80%;

  @media screen and (max-width: 1200px) {
    display: none;
  }
}

.statistics {
  margin-top: 100px;
}

.statistics_item {
  font-weight: 700;
}

.item_value {
  color: #fff;
  font-size: 96px;

  @media screen and (max-width: 1200px) {
    font-size: 72px;
  }

  @media screen and (max-width: 500px) {
    font-size: 32px;
  }
}

.item_text {
  text-align: center;
  color: #fe9f00;
  font-size: 24px;

  @media screen and (max-width: 1200px) {
    font-size: 20px;
  }

  @media screen and (max-width: 500px) {
    font-size: 16px;
  }
}
</style>
