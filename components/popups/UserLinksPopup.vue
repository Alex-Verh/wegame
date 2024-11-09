<script setup>
const userData = inject("userData");
const userLinks = computed(() => userData.value.platforms ? userData.value.platforms.reduce((acc, curr) => ({ ...acc, [curr.platformId]: curr.link }), {}) : {})
const { visible, close } = useUserLinksPopup()

const { data: platforms } = useFetch('/api/platforms')
</script>

<template>
    <Popup :visible @close="close" :width="500" class="links">
        <b-container>
            <div class="links_title">User Links</div>
            <template v-for="platform in platforms">
                <label :for="`platform_${platform.id}_url`" class="links_subtitle">{{ platform.title }} Profile</label>
                <input :value="userLinks[platform.id]" type="text" :name="`platform_${platform.id}_url`"
                    :id="`platform_${platform.id}_url`" class="links_field" />
            </template>
            <div class="button_accent">Save Changes</div>
        </b-container>
    </Popup>
</template>

<style scoped>
.links_title {
    text-align: center;
    font-size: 28px;
}

.links_subtitle {
    font-size: 18px;
    margin: 15px 0;
    display: block;
}

.links_field {
    background: none;
    border: 1px solid #444259;
    width: 100%;
    color: #FE9F00;
    resize: none;
    outline: none;
    font-size: 16px;
    padding: 10px;
}

.links .button_accent {
    width: 175px;
    margin: 15px auto;
}
</style>