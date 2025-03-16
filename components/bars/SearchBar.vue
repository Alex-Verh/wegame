<script setup lang="ts">
defineProps<{
  isAppSearch: boolean;
}>();

const title = defineModel<string>("title");
const platformId = defineModel<number>("platform");
const languageId = defineModel<number>("language");
const gameId = defineModel<number>("game");
const age = defineModel<number>("age");
const membersLimit = defineModel<number>("members");
const ranking = defineModel<string>("ranking");

const { data: games } = useGames();
const { data: platforms } = usePlatforms();
const { data: languages } = useLanguages();
</script>

<template>
  <div class="search_bar">
    <Row class="g-3">
      <Col col="12" class="col-sm-4">
        <input
          v-model.lazy="title"
          type="text"
          name="find_by_title"
          :placeholder="$t('findName')"
          class="search_field"
        />
      </Col>
      <template v-if="isAppSearch">
        <Col col="12" class="col-sm-4">
          <select v-model="platformId" class="search_filter accent">
            <option :value="0" class="search_result">
              {{ $t("filterPlatform") }}
            </option>
            <option
              v-for="platform in platforms"
              class="search_result"
              :key="platform.id"
              :value="platform.id"
            >
              {{ platform.title }}
            </option>
          </select>
        </Col>
        <Col col="12" class="col-sm-4">
          <select v-model="languageId" class="search_filter accent">
            <option :value="0" class="search_result">
              {{ $t("filterLanguage") }}
            </option>
            <option
              v-for="language in languages"
              class="search_result"
              :key="language.id"
              :value="language.id"
            >
              {{ language.title }}
            </option>
          </select>
        </Col>
        <Col col="12" class="col-sm-4">
          <select v-model="gameId" class="search_filter accent">
            <option :value="0" class="search_result">
              {{ $t("filterGame") }}
            </option>
            <option
              v-for="game in games"
              class="search_result"
              :key="game.id"
              :value="game.id"
            >
              {{ game.title }}
            </option>
          </select>
        </Col>
        <Col col="12" class="col-sm-3">
          <input
            v-model.lazy="age"
            type="number"
            name="find_by_age"
            :placeholder="$t('filterAge')"
            class="search_field"
          />
        </Col>
        <Col col="12" class="col-sm-5">
          <input
            v-model.lazy="ranking"
            type="text"
            name="find_by_ranking"
            :placeholder="$t('findRank')"
            class="search_field"
          />
        </Col>
      </template>
      <template v-else="isAppSearch">
        <Col col="12" class="col-sm-3">
          <select v-model="platformId" class="search_filter accent">
            <option :value="0" class="search_result">
              {{ $t("filterPlatform") }}
            </option>
            <option
              v-for="platform in platforms"
              class="search_result"
              :key="platform.id"
              :value="platform.id"
            >
              {{ platform.title }}
            </option>
          </select>
        </Col>
        <Col col="12" class="col-sm-3">
          <select v-model="gameId" class="search_filter accent">
            <option :value="0" class="search_result">
              {{ $t("filterGame") }}
            </option>
            <option
              v-for="game in games"
              class="search_result"
              :key="game.id"
              :value="game.id"
            >
              {{ game.title }}
            </option>
          </select>
        </Col>
        <Col col="12" class="col-sm-2">
          <input
            v-model.lazy="membersLimit"
            type="number"
            name="find_by_memberslimit"
            :placeholder="$t('filterPeopleNr')"
            class="search_field"
          />
        </Col>
      </template>
    </Row>
  </div>
</template>

<style scoped>
.search_bar {
  margin-top: 40px;
  background-color: #201f30;
  padding: 25px;
}

.search_filter,
.search_field {
  border: 1px solid #fe9f00;
  /* Change border color */
  border-radius: 5px;
  /* Optional: rounded corners */
  padding: 10px;
  /* Add some padding */
  width: 100%;
  /* Optional: make it full width */
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;

  @media screen and (max-width: 800px) {
    padding: 5px;
  }
}

.search_filter {
  -webkit-appearance: none;
  appearance: none;
  background-image: url("~/assets/icons/expand.svg") !important;
  background-repeat: no-repeat !important;
  background-position: calc(100% - 12px) center !important;
  background: transparent;
  @media screen and (max-width: 800px) {
    font-size: 12px;
    background-image: none !important;
  }

  @media screen and (max-width: 500px) {
    font-size: 8px;
  }
}

.search_result {
  background-color: #201f30;
}

.search_result:checked {
  background-color: #fe9f00 !important;
  color: #201f30 !important;
}

.search_field {
  background: transparent;
  font-size: 16px;
  color: #fff;

  @media screen and (max-width: 800px) {
    font-size: 12px;
  }

  @media screen and (max-width: 500px) {
    font-size: 8px;
  }
}

/* Placeholder styling */
.search_field::placeholder {
  color: #fe9f00;
  /* Placeholder text color */
  opacity: 1;
  /* Ensure the color is fully opaque */
}

.search_field:focus,
.search_filter:focus {
  outline: none !important;
  /* Remove default outline */
  box-shadow: 0 0 5px #fea100a5;
  /* Optional: add a shadow */
}
</style>
