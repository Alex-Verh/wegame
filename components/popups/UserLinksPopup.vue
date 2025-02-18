<script setup lang="ts">

const { user } = defineProps<{
    user: User,
}>()
defineEmits()

const userLinks = computed<{ [id: number]: string }>(() => user.platforms ? user.platforms.reduce((acc, curr) => ({ ...acc, [curr.platform.id]: curr.link }), {}) : {})

const { user: sessionUser } = useUserSession()

const { data: platforms } = usePlatforms()

const queryCache = useQueryCache()

interface PlatformLink {
    platformId: number,
    link: string
    linkPattern: string
}

const { mutate: updatePlatformLink } = useMutation({
    mutation: (platformLink: PlatformLink) => {
        if (!platformLink.link.trim) throw new Error('Link is required')
        if (!platformLink.link.includes(platformLink.linkPattern)) throw new Error('Link is not valid')
        return $fetch(`/api/users/${user.id}`, {
            method: "PATCH",
            body: {
                platforms: {
                    [platformLink.platformId]: platformLink.link
                }
            }
        })
    },
    onSuccess: async () => {
        await queryCache.invalidateQueries({ key: ['users', user.id], exact: true })
        useToast('Links updated')
    },
    onError: (err) => {
        useToast(err.message)
    }
})

</script>

<template>
    <Popup :width="500" class="links">
        <Container>
            <div class="links_title">{{ $t('userLinks') }}</div>
            <template v-for="platform in platforms">
                <label :for="`platform_${platform.id}_url`" class="links_subtitle">{{ platform.title }} Profile</label>
                <input :readonly="sessionUser?.id !== user.id" :value="userLinks[platform.id]"
                    @change="updatePlatformLink({ platformId: platform.id, link: ($event.target as HTMLInputElement).value, linkPattern: platform.urlPattern })"
                    type="text" :name="`platform_${platform.id}_url`" :id="`platform_${platform.id}_url`"
                    class="links_field" />
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