<script setup>
</script>

<template>
    <section class="section">
        <div class="section_title">Parties - Find your brothers from another mother</div>

        <SearchBar />

        <div class="parties">
            <Row class="g-5">
                <Col col="6">
                    <Party />
                </Col>
                <Col col="6">
                    <Party />
                </Col>
                <Col col="6">
                    <Party />
                </Col>
                <Col col="6">
                    <Party />
                </Col>
            </Row>
        </div>
    </section>
</template>

<style scoped>
.parties {
    margin-top: 40px;
    margin-bottom: 100px;
}
</style>