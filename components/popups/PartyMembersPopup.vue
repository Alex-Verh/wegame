<script setup lang="ts">
defineProps<{ members: User[] }>()
defineEmits()
</script>

<template>
    <Popup :width="700" class="members">
        <Container>
            <div class="members_title">Party Requests</div>

            <div class="members_section">
                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">Accept</button>
                        <button class="button_accent">Deny</button>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">Accept</button>
                        <button class="button_accent">Deny</button>
                    </div>
                </div>

            </div>

            <button class="button_accent">Accept Everyone</button>


            <div class="members_title">Party Members</div>

            <div class="members_section">
                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">See User</button>
                        <button class="button_accent">Kick</button>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">See User</button>
                        <button class="button_accent">Kick</button>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">See User</button>
                        <button class="button_accent">Kick</button>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">See User</button>
                        <button class="button_accent">Kick</button>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">See User</button>
                        <button class="button_accent">Kick</button>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <button class="button_accent">See User</button>
                        <button class="button_accent">Kick</button>
                    </div>
                </div>
            </div>

            <div class="members_title">Discord Server URL</div>
            <div class="members_member d-flex align-items-center justify-content-between">
                <span class="members_name">
                    https://discord.com/invite/ID
                </span>
                <div>
                    <button class="button_accent">Navigate</button>
                </div>
            </div>
        </Container>
    </Popup>
</template>

<style scoped>
.members_title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 30px;
}

.members_section {
    max-height: 250px;
    overflow-y: auto;
    scroll-snap-type: y mandatory;
}

.members_member {
    border: 1px solid #444259;
    padding: 0 0 0 15px;
    margin-bottom: 20px;
    scroll-snap-align: start;
}

.members_member:last-of-type {
    margin-bottom: 0px;
}

.members_name {
    font-size: 26px;
    color: #FE9F00;
}

.members_member .button_accent {
    margin: 0 auto 0 0 !important;
    display: inline-flex;
    width: 100px !important;
}

.members_member .button_accent:first-of-type {
    background-color: #fff !important;
}

.members_member .button_accent:last-of-type {
    background-color: #CF1E1E;
}

.members .button_accent {
    width: 175px;
    margin: 15px auto;
}
</style>