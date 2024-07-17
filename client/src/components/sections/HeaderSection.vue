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
            <b-row>
                <b-col cols="4" class="d-flex align-items-center justify-content-center">
                    <div class="statistics_item">
                        <div class="item_value">551</div>
                        <div class="item_text">parties</div>
                    </div>
                </b-col>
                <b-col cols="4" class="d-flex align-items-center justify-content-center">
                    <div class="statistics_item">
                        <div class="item_value">132</div>
                        <div class="item_text">games</div>
                    </div>
                </b-col>
                <b-col cols="4" class="d-flex align-items-center justify-content-center">
                    <div class="statistics_item">
                        <div class="item_value">1232</div>
                        <div class="item_text">players</div>
                    </div>
                </b-col>
            </b-row>
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

.statistics {
    margin-top: 100px;
}

.statistics_item {
    font-weight: 700;
}

.item_value {
    color: #fff;
    font-size: 96px;
}

.item_text {
    text-align: center;
    color: #FE9F00;
    font-size: 24px;
}
</style>