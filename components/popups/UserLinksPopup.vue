<script setup lang="ts">
import { useToast } from '~/composables/toasts';

defineProps<{
    isOpen: boolean,
    isEditable: boolean
}>()
const user = inject<Ref<UserT>>("user");

const userLinks = computed(() => user?.value.platforms ? user?.value.platforms.reduce((acc: any, curr: any) => ({ ...acc, [curr.platformId]: curr.link }), {}) : {})
const isSaved = ref(true)

const platforms = inject<PlatformT[]>("platforms")
const updatePlatformLink = async (platformId, link) => {
    const { updatedFields } = await $fetch(`/api/users/${user?.value.id}`, {
        method: "PATCH",
        body: {
            platforms: {
                [platformId]: link
            }
        }
    })
    if (updatedFields?.platforms)
        user.value.platforms = updatedFields.platforms

    useToast("Links updated successfully", "success")
}
</script>

<template>
    <Popup :visible="isOpen" :width="500" class="links">
        <Container>
            <div class="links_title">User Links</div>
            <template v-for="platform in platforms">
                <label :for="`platform_${platform.id}_url`" class="links_subtitle">{{ platform.title }} Profile</label>
                <input :readonly="!isEditable" :value="userLinks[platform.id]"
                    @change="updatePlatformLink(platform.id, $event.target.value)" type="text" @input="isSaved = false"
                    :name="`platform_${platform.id}_url`" :id="`platform_${platform.id}_url`" class="links_field" />
            </template>
        </Container>
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