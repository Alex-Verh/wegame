<script setup lang="ts">
const { party } = defineProps<{
  party?: Party;
}>();
const emit = defineEmits();

const { data: platforms } = usePlatforms();
const { searchQuery: gameSearchQ, games } = useGameSearch();

const { loggedIn, user } = useUserSession();

const partyTitle = ref(party?.title || "");
const partyDescription = ref(party?.description || "");
const partyDiscordLink = ref(party?.discordLink || "");
const partyGame = ref(party?.gameId || 0);
const partyPlatform = ref(party?.platformId || 0);
const partyMinAge = ref(party?.minAge || 0);
const partyMaxAge = ref(party?.maxAge || 100);
const partyMemberNr = ref(party?.membersLimit || 5);

const queryCache = useQueryCache();

interface PartyCreate {
  title: string;
  description: string;
  gameId: number;
  platformId: number;
  minAge: number;
  maxAge: number;
  membersLimit: number;
  discordLink: string;
}
interface PartyUpdate extends PartyCreate {
  id: number;
}

const { mutate: createParty } = useMutation({
  mutation: (party: PartyCreate) => {
    if (!loggedIn) throw new Error("Login required");
    if (!party.title.trim()) throw new Error("Title is required");
    if (!party.gameId) throw new Error("Game is required");
    if (!party.platformId) throw new Error("Platform is required");
    return $fetch("/api/parties", {
      method: "POST",
      body: {
        ...party,
      },
    });
  },

  onSuccess: async (party) => {
    await queryCache.invalidateQueries({
      key: ["users", party.leaderId, "parties", "own"],
    });
    partyTitle.value = "";
    partyDescription.value = "";
    partyGame.value = 0;
    partyPlatform.value = 0;
    partyMinAge.value = 0;
    partyMaxAge.value = 100;
    partyMemberNr.value = 5;
    useToast(`Party "${party.title}" created.`, "success");
    emit("close");
  },

  onError: (err) => {
    useToast(err.message, "danger");
  },
});
const { mutate: updateParty } = useMutation({
  mutation: (party: PartyUpdate) => {
    if (!loggedIn) throw new Error("Login required");
    if (!party.id) throw new Error("There is no existing party");
    if (!party.title.trim()) throw new Error("Title is required");
    if (!party.gameId) throw new Error("Game is required");
    if (!party.platformId) throw new Error("Platform is required");
    const { id, ...body } = party;
    return $fetch(`/api/parties/${id}`, {
      method: "PATCH",
      body,
    });
  },

  onSuccess: async (party) => {
    await queryCache.invalidateQueries({
      key: ["users", party.leaderId, "parties", "own"],
    });
    useToast(`Party "${party.title}" updated.`, "success");
    emit("close");
  },
  onError: (err) => {
    useToast(err.message, "danger");
  },
});

const { mutate: deleteParty } = useMutation({
  mutation: (partyId: number) => {
    if (!loggedIn) throw new Error("Login required");
    if (!partyId) throw new Error("There is no existing party");
    return $fetch(`/api/parties/${partyId}`, {
      method: "DELETE",
    });
  },
  onSuccess: async (party) => {
    await queryCache.invalidateQueries({
      key: ["users", party.leaderId, "parties"],
    });
    useToast(`Party "${party.title}" deleted.`, "success");
    emit("close");
  },
  onError: (err) => {
    useToast(err.message, "danger");
  },
});
const membersPopup = usePopup("partyMembers");
</script>

<template>
  <Popup>
    <PartyMembersPopup
      v-if="party"
      :modalId="membersPopup.modalId"
      :members="party.members"
      :leaderId="party.leaderId"
      :partyId="party.id"
      @close="membersPopup.close"
    />
    <Container>
      <div class="party_title">
        {{
          party && party.leaderId === user?.id
            ? $t("editParty")
            : $t("createParty")
        }}
      </div>

      <div class="party_body">
        <label for="party_name" class="party_subtitle">{{
          $t("partyName")
        }}</label>
        <input
          v-model="partyTitle"
          type="text"
          name="party_name"
          id="party_name"
          class="party_field"
          placeholder="Some cool name.."
        />

        <label for="party_description" class="party_subtitle">{{
          $t("partyDescription")
        }}</label>
        <textarea
          v-model="partyDescription"
          name="party_description"
          id="party_description"
          class="party_field party_textarea"
          placeholder="We will be playing on Faceit.."
        ></textarea>

        <Row>
          <Col col="12" class="col-sm-6">
            <label for="party_age" class="party_subtitle">{{
              $t("ageRange")
            }}</label>
            <div class="d-flex align-items-center party_numbers">
              <input
                v-model="partyMinAge"
                type="number"
                min="0"
                max="99"
                name="party_minage"
                id="party_minage"
                class="party_field party_minifield"
                placeholder="10"
              />
              <span> - </span>
              <input
                v-model="partyMaxAge"
                type="number"
                min="0"
                max="99"
                name="party_maxage"
                id="party_maxage"
                class="party_field party_minifield"
                placeholder="99"
              />
              <span>{{ $t("yearsOld") }}</span>
            </div>
          </Col>
          <Col col="12" class="col-sm-6">
            <label for="party_members" class="party_subtitle">{{
              $t("nrMembers")
            }}</label>
            <div class="d-flex align-items-center party_numbers">
              <input
                v-model="partyMemberNr"
                type="number"
                min="2"
                max="30"
                name="party_members"
                id="party_members"
                class="party_field party_minifield"
                placeholder="5"
              />
              <span>members</span>
            </div>
          </Col>
        </Row>

        <label for="party_discord_link" class="party_subtitle">{{
          $t("partyDiscord")
        }}</label>
        <input
          v-model="partyDiscordLink"
          type="text"
          name="party_discord_link"
          id="party_discord_link"
          class="party_field"
          placeholder="Your discord server url.."
        />

        <label for="party_platforms" class="party_subtitle">{{
          $t("gamePlatform")
        }}</label>
        <div class="party_platforms">
          <template v-for="platform in platforms" :key="platform.id">
            <input
              v-model="partyPlatform"
              type="radio"
              :id="`${platform.title}+${platform.id}`"
              name="party_platform"
              :value="platform.id"
            />
            <label
              :for="`${platform.title}+${platform.id}`"
              class="party_platform"
              >{{ platform.title }}</label
            >
          </template>
        </div>

        <label for="party_search" class="party_subtitle">{{
          $t("selectGame")
        }}</label>
        <input
          v-model="gameSearchQ"
          type="text"
          name="party_search"
          id="party_search"
          class="party_field"
          placeholder="Searching.."
        />
        <div class="pop_section d-flex flex-row">
          <template v-for="game in games" :key="game.id">
            <input
              v-model="partyGame"
              type="radio"
              :id="`${game.title}+${game.id}`"
              name="party_game"
              :value="game.id"
            />
            <label :for="`${game.title}+${game.id}`">
              <Game
                v-bind="game"
                class="game_pop"
                :isSelected="game.id === partyGame"
              />
            </label>
          </template>
        </div>

        <div class="party_buttons d-flex justify-content-center">
          <template v-if="party">
            <button
              @click="
                updateParty({
                  title: partyTitle,
                  description: partyDescription,
                  gameId: partyGame,
                  platformId: partyPlatform,
                  minAge: partyMinAge,
                  maxAge: partyMaxAge,
                  membersLimit: partyMemberNr,
                  id: party.id,
                })
              "
              class="button_accent"
            >
              {{ $t("saveChanges") }}
            </button>
            <button @click="membersPopup.open" class="button_accent">
              {{ $t("seeMembers") }}
            </button>
            <button @click="deleteParty(party.id)" class="button_accent">
              {{ $t("deleteParty") }}
            </button>
          </template>
          <button
            v-else
            @click="
              createParty({
                title: partyTitle,
                description: partyDescription,
                gameId: partyGame,
                platformId: partyPlatform,
                minAge: partyMinAge,
                maxAge: partyMaxAge,
                membersLimit: partyMemberNr,
                discordLink: partyDiscordLink,
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
.party {
  width: 1000px;
}

.party_body {
  overflow-y: scroll;
  height: 500px;
  padding: 0 30px;

  @media screen and (max-width: 800px) {
    font-size: 14px;
  }

  @media screen and (max-width: 410px) {
    font-size: 12px;
  }
}

.party_body::-webkit-scrollbar {
  width: 3px;
}

.party_title {
  text-align: center;
  font-size: 34px;

  @media screen and (max-width: 800px) {
    font-size: 20px;
  }

  @media screen and (max-width: 410px) {
    font-size: 14px;
  }
}

.party_subtitle {
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

.party_field {
  background: none;
  border: 1px solid #444259;
  width: 100%;
  color: #fff;
  resize: none;
  font-size: 20px;
  padding: 10px;
  outline: none;

  @media screen and (max-width: 800px) {
    font-size: 12px;
  }

  @media screen and (max-width: 410px) {
    font-size: 10px;
  }
}

.party_minifield {
  width: 70px !important;
  margin-inline-end: 20px;

  @media screen and (max-width: 580px) {
    width: 40px !important;
    margin-inline-end: 7px;
    padding: 5px;
  }
}

.party_minifield:nth-of-type(2) {
  margin-inline-start: 20px;
}

.party_textarea {
  resize: none;
  height: 100px;
}

.party_numbers {
  color: #444259;
}

.party_platforms {
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

.party_platforms input[type="radio"],
.pop_section input[type="radio"] {
  display: none;
}

.party_platforms input[type="radio"]:checked + .party_platform {
  color: #fe9f00;
}

.party_platform {
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
}

.pop_section label:last-of-type {
  margin-inline-end: 0px;
}

.game_pop {
  flex-shrink: 0;
  height: 100%;
  font-size: 12px !important;
  min-width: auto !important;
}

.party_buttons {
  margin-top: 20px;
}

.party_buttons .button_accent {
  width: 175px;
  margin-inline: 5px;

  @media screen and (max-width: 410px) {
    width: 135px;
    font-size: 8px;
  }
}

/* Scroll */
::-webkit-scrollbar {
  height: 3px;
}
</style>
