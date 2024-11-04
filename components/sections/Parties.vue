<script setup>
</script>

<template>
    <section class="section">
        <div class="section_title">Parties - Find your brothers from another mother</div>

        <SearchBar />

        <div class="parties">
            <b-row class="g-5">
                <b-col cols="6">
                    <Party />
                </b-col>
                <b-col cols="6">
                    <Party />
                </b-col>
                <b-col cols="6">
                    <Party />
                </b-col>
                <b-col cols="6">
                    <Party />
                </b-col>
            </b-row>
        </div>
    </section>
</template>

<style scoped>
.parties {
    margin-top: 40px;
    margin-bottom: 100px;
}
</style>