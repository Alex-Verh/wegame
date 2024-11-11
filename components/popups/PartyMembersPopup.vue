<script setup>
const { visible, close } = usePartyMembersPopup()
</script>

<template>
    <Popup :visible @close="close" :width="700" class="members">
        <b-container>
            <div class="members_title">Party Members</div>

            <div class="members_section">
                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>

                <div class="members_member d-flex align-items-center justify-content-between">
                    <span class="members_name">
                        @alllexlelfef
                    </span>
                    <div>
                        <div class="button_accent">See User</div>
                        <div class="button_accent">Kick</div>
                    </div>
                </div>
            </div>


            <div class="button_accent">Kick All</div>
        </b-container>
    </Popup>
</template>

<style scoped>
.members_title {
    text-align: center;
    font-size: 28px;
    margin-bottom: 30px;
}

.members_section {
    height: 300px;
    overflow-y: auto;
    margin-bottom: 30px;
}

.members_member {
    border: 1px solid #444259;
    padding: 0 0 0 15px;
    margin-bottom: 20px;
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
    background-color: #fff;
}

.members_member .button_accent:last-of-type {
    background-color: #CF1E1E;
}

.members .button_accent {
    width: 175px;
    margin: 15px auto;
}
</style>