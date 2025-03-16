<script setup lang="ts">
const { application } = defineProps<{
  application?: Application;
}>();

const emit = defineEmits();

const { loggedIn, user } = useUserSession();

const { data: platforms } = usePlatforms();

const { searchQuery: gameSearchQ, games } = useGameSearch();

const appText = ref(application?.text || "");
const appRank = ref(application?.ranking || "");
const appGame = ref(application?.gameId || 0);
const appPlatform = ref(application?.platformId || 0);

const queryCache = useQueryCache();

interface ApplicationCreate {
  text: string;
  ranking: string;
  gameId: number;
  platformId: number;
}
interface ApplicationUpdate extends ApplicationCreate {
  id: number;
}

const { mutate: createApplication } = useMutation({
  mutation: (app: ApplicationCreate) => {
    if (!loggedIn) throw new Error("Login required");
    if (!app.text.trim()) throw new Error("Title is required");
    if (!app.gameId) throw new Error("Game is required");
    if (!app.platformId) throw new Error("Platform is required");
    return $fetch("/api/applications", {
      method: "POST",
      body: {
        ...app,
      },
    });
  },

  onSuccess: async (application) => {
    await queryCache.invalidateQueries({
      key: ["users", application.authorId, "applications"],
    });
    appText.value = "";
    appRank.value = "";
    appGame.value = 0;
    appPlatform.value = 0;
    useToast(`Application "${application.text}" created.`);
    emit("close");
  },

  onError: (err) => {
    useToast(err.message);
  },
});

const { mutate: updateApplication } = useMutation({
  mutation: (app: ApplicationUpdate) => {
    if (!loggedIn) throw new Error("Login required");
    if (!app.id) throw new Error("There is no existing application");
    if (!app.text.trim()) throw new Error("Title is required");
    if (!app.gameId) throw new Error("Game is required");
    if (!app.platformId) throw new Error("Platform is required");
    const { id, ...body } = app;
    return $fetch(`/api/applications/${id}`, {
      method: "PATCH",
      body,
    });
  },
  onSuccess: async (application) => {
    await queryCache.invalidateQueries({
      key: ["users", application.authorId, "applications"],
    });
    useToast(`Application "${application.text}" updated.`);
    emit("close");
  },
  onError: (err) => {
    useToast(err.message);
  },
});

const { mutate: deleteApplication } = useMutation({
  mutation: (appId: number) => {
    if (!loggedIn) throw new Error("Login required");
    if (!appId) throw new Error("There is no application");
    return $fetch(`/api/applications/${appId}`, {
      method: "DELETE",
    });
  },
  onSuccess: async (application) => {
    await queryCache.invalidateQueries({
      key: ["users", application.authorId, "applications"],
    });
    useToast(`Application "${application?.text}" deleted.`);
    emit("close");
  },
  onError: (err) => {
    useToast(err.message);
  },
});
</script>

<template>
  <Popup>
    <Container>
      <div class="application_title">
        {{
          application && application.authorId === user?.id
            ? $t("editApplication")
            : $t("createApplication")
        }}
      </div>
      <div class="application_body">
        <label for="application_description" class="application_subtitle">{{
          $t("applicationMessage")
        }}</label>
        <textarea
          v-model="appText"
          name="application_description"
          id="application_description"
          class="application_field application_textarea"
          placeholder="I am looking for a friend.."
        ></textarea>

        <label for="application_rank" class="application_subtitle">{{
          $t("gameRank")
        }}</label>
        <input
          v-model="appRank"
          type="text"
          name="application_rank"
          id="application_rank"
          class="application_field"
          placeholder="Silver III"
        />

        <label for="application_platforms" class="application_subtitle">{{
          $t("gamePlatform")
        }}</label>
        <div class="application_platforms">
          <template v-for="platform in platforms" :key="platform.id">
            <input
              v-model="appPlatform"
              type="radio"
              :id="`${platform.title}+${platform.id}`"
              name="application_platform"
              :value="platform.id"
            />
            <label
              :for="`${platform.title}+${platform.id}`"
              class="application_platform"
              >{{ platform.title }}</label
            >
          </template>
        </div>

        <label for="games_search" class="application_subtitle">{{
          $t("selectGame")
        }}</label>
        <input
          v-model="gameSearchQ"
          type="text"
          name="games_search"
          id="games_search"
          class="application_field"
          :placeholder="$t('search') + '...'"
        />
        <div class="pop_section d-flex flex-row">
          <template v-for="game in games" :key="game.id">
            <input
              v-model="appGame"
              type="radio"
              :id="`${game.title}+${game.id}`"
              name="application_game"
              :value="game.id"
            />
            <label :for="`${game.title}+${game.id}`">
              <Game
                v-bind="game"
                class="game_pop"
                :isSelected="game.id === appGame"
              />
            </label>
          </template>
        </div>

        <div class="application_buttons d-flex justify-content-center">
          <template v-if="application && application.authorId === user?.id">
            <button
              @click="
                updateApplication({
                  text: appText,
                  ranking: appRank,
                  gameId: appGame,
                  platformId: appPlatform,
                  id: application.id,
                })
              "
              class="button_accent"
            >
              {{ $t("saveChanges") }}
            </button>
            <button
              @click="deleteApplication(application.id)"
              class="button_accent"
            >
              {{ $t("deleteApplication") }}
            </button>
          </template>
          <button
            v-else
            @click="
              createApplication({
                text: appText,
                ranking: appRank,
                gameId: appGame,
                platformId: appPlatform,
              })
            "
            class="button_accent"
          >
            {{ $t("saveChanges") }}
          </button>
        </div>
      </div>
    </Container>
  </Popup>
</template>

<style scoped>
.application_body {
  overflow-y: scroll;
  height: 500px;
  padding: 0 30px;

  @media screen and (max-width: 410px) {
    padding: 0 15px;
    height: 300px;
  }
}

.application_body::-webkit-scrollbar {
  width: 3px;
}

.application_title {
  text-align: center;
  font-size: 34px;

  @media screen and (max-width: 800px) {
    font-size: 20px;
  }

  @media screen and (max-width: 410px) {
    font-size: 14px;
  }
}

.application_subtitle {
  font-size: 18px;
  margin: 20px 0;
  display: block;

  @media screen and (max-width: 800px) {
    font-size: 14px;
  }

  @media screen and (max-width: 410px) {
    font-size: 12px;
  }
}

.application_field {
  background: none;
  border: 1px solid #444259;
  width: 100%;
  color: #fff;
  font-size: 20px;
  padding: 10px;

  @media screen and (max-width: 800px) {
    font-size: 12px;
  }

  @media screen and (max-width: 410px) {
    font-size: 10px;
  }
}

.application_textarea {
  resize: none;
  height: 100px;
}

.application_platforms {
  display: flex;
  justify-content: space-between;
  color: #444259;

  @media screen and (max-width: 580px) {
    font-size: 10px;
  }

  @media screen and (max-width: 410px) {
    font-size: 6px;
  }
}

.application_platforms input[type="radio"],
.pop_section input[type="radio"] {
  display: none;
}

.application_platforms input[type="radio"]:checked + .application_platform {
  color: #fe9f00;
}

.application_platform {
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;
}

.pop_section {
  margin-top: 20px;
  height: 130px;
  overflow-x: auto;
  overflow-y: hidden;
  @media screen and (max-width: 800px) {
    height: 90px;
  }
  @media screen and (max-width: 410px) {
    height: 60px;
  }
}

.pop_section label {
  display: block;
  margin-inline-end: 25px;

  @media screen and (max-width: 800px) {
    margin-inline-end: 15px;
  }
}

.pop_section label:last-of-type {
  margin-inline-end: 0px;
}

.game_pop {
  flex-shrink: 0;
  height: 100%;
  min-width: auto !important;
  font-size: 12px !important;
}

.application_buttons {
  margin-top: 20px;
}

.application_buttons .button_accent {
  width: 175px;
  margin-inline: 5px;
}

/* Scroll */
::-webkit-scrollbar {
  height: 3px;
}
</style>
