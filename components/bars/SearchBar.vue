<template>
    <div class="search_bar">
        <Row class="g-3">
            <Col col="4">
                <input type="text" name="find_player" placeholder="Find by name" class="search_field" />
            </Col>
            <Col col="4">
                <div class="search_filter accent">Filter by platform</div>
            </Col>
            <Col col="4">
                <div class="search_filter accent">Filter by language</div>
            </Col>
            <Col col="4">
                <div class="search_filter accent">Filter by game</div>
            </Col>
            <Col col="3">
                <div class="search_filter accent">Filter by age</div>
            </Col>
            <Col col="5">
                <div class="search_filter accent">Filter by ranking</div>
            </Col>
        </Row>
    </div>
</template>

<style scoped>
.games_section {
    margin-top: 120px;
}

.section_title {
    color: #fff;
    font-size: 32px;
    font-weight: 700;
}

.search_bar {
    margin-top: 40px;
    background-color: #201F30;
    padding: 25px;
}

.search_filter,
.search_field {
    border: 1px solid #FE9F00;
    /* Change border color */
    border-radius: 5px;
    /* Optional: rounded corners */
    padding: 10px;
    /* Add some padding */
    width: 100%;
    /* Optional: make it full width */
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.search_field {
    background: transparent;
    /* Remove background */
    font-size: 16px;
    /* Adjust font size */
    color: #fff;
    /* Text color */
}

/* Placeholder styling */
.search_field::placeholder {
    color: #FE9F00;
    /* Placeholder text color */
    opacity: 1;
    /* Ensure the color is fully opaque */
}

.search_field:focus {
    outline: none;
    /* Remove default outline */
    box-shadow: 0 0 5px #fea100a5;
    /* Optional: add a shadow */
}
</style>