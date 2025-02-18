<script setup lang="ts">
defineProps<{
    text: string, image: string, showStatistics: boolean
}>()

// TODO FETCH STATS
</script>

<template>
    <header class="header">
        <Row>
            <Col col="6">
            <div class="header_text">
                <span v-html="text"></span>
            </div>
            </Col>
            <Col col="6" class="d-flex justify-content-center">
            <img :src="image" alt="Friends" class="header_image">
            </Col>
        </Row>
        <div class="statistics" v-if="showStatistics">
            <Row>
                <Col col="4" class="d-flex align-items-center justify-content-center">
                <div class="statistics_item">
                    <div class="item_value">551</div>
                    <div class="item_text">{{ $t('parties') }}</div>
                </div>
                </Col>
                <Col col="4" class="d-flex align-items-center justify-content-center">
                <div class="statistics_item">
                    <div class="item_value">132</div>
                    <div class="item_text">{{ $t('games') }}</div>
                </div>
                </Col>
                <Col col="4" class="d-flex align-items-center justify-content-center">
                <div class="statistics_item">
                    <div class="item_value">1232</div>
                    <div class="item_text">{{ $t('players') }}</div>
                </div>
                </Col>
            </Row>
        </div>
    </header>
</template>

<style scoped>
.header {
    margin-top: 100px;
}

.header_text {
    font-size: 58px;
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