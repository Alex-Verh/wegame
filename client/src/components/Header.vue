<script setup>
defineProps(['text', "image", "showStatistics"])
</script>

<template>
    <header class="header">
        <b-row>
            <b-col cols="6">
                <div class="header_text">
                    <span v-html="text"></span>
                </div>
            </b-col>
            <b-col cols="6" class="d-flex justify-content-center">
                <img :src="image" alt="Friends" class="header_image">
            </b-col>
        </b-row>
        <div class="statistics" v-if="showStatistics">
            <div class="statistics_item">
                <div class="item_value">551</div>
                <div class="item_text">parties</div>
            </div>
            <div class="statistics_item">
                <div class="item_value">132</div>
                <div class="item_text">games</div>
            </div>

            <div class="statistics_item">
                <div class="item_value">1232</div>
                <div class="item_text">players</div>
            </div>

        </div>
    </header>
</template>

<style scoped>
.header {
    margin-top: 100px;
}

.header_text {
    font-size: 64px;
    color: #fff;
}

.header_image {
    width: 80%;
}
</style>