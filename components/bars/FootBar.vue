<script setup lang="ts">
const { setLocale } = useI18n();

</script>

<template>
    <footer class="footer">
        <Container>
            <Row>
                <Col col="3" class="d-flex justify-content-center">
                    <div>
                        <div class="link_column_header">Website Links</div>
                        <div class="links">
                            <NuxtLinkLocale to="/" class="link">Home Page</NuxtLinkLocale>
                            <NuxtLinkLocale to="parties" class="link">Parties & Lobbies</NuxtLinkLocale>
                            <NuxtLinkLocale to="sign-up" class="link">Registration</NuxtLinkLocale>
                            <NuxtLinkLocale to="/" class="link">Support & FAQ</NuxtLinkLocale>
                        </div>
                    </div>
                </Col>
                <Col col="3" class="d-flex justify-content-center">
                    <div>
                        <div class="link_column_header">About Us</div>
                        <div class="links">
                            <a href="#" class="link">Instagram</a>
                            <a href="#" class="link">Steam</a>
                            <a href="#" class="link">GitHub</a>
                        </div>
                    </div>
                </Col>
                <Col col="3" class="d-flex justify-content-center">
                    <div>
                        <div class="link_column_header">Other Projects</div>
                        <div class="links">
                            <a href="#" class="link">Flashy</a>
                            <a href="#" class="link">Coworkers</a>
                        </div>
                    </div>
                </Col>
                <Col col="3" class="d-flex justify-content-center">
                    <div>
                        <div class="link_column_header">Language</div>
                        <div class="links">
                            <button class="link" @click="setLocale('ru')">Русский</button>
                            <button class="link" @click="setLocale('en')">English</button>
                            <button class="link" @click="setLocale('ro')">Română</button>
                        </div>
                    </div>
                </Col>
            </Row>

            <div class="footer_line"></div>

            <div class="information">
                <Row>
                    <Col col="9">
                        <div class="text d-flex align-items-center">WeGame - a brand owned by Alexandru Denis Ltd,
                            located at 13 Kypranoros Str., Evi
                            Building, 1st Floor, Office 102, 1061 Chisinau, Moldova.
                            <br />Beware of false accounts and fraudsters who may
                            attempt to trade and scam users on any game platforms.
                        </div>
                    </Col>
                    <Col col="3">
                        <div class="logo d-flex align-items-center justify-content-center">
                            <img src="/images/logo.png" alt="Logo" class="logo_icon">
                            <NuxtLinkLocale to="/" class="logo_text">
                                WE<span class="accent">GAME</span>
                            </NuxtLinkLocale>
                        </div>
                    </Col>
                </Row>
            </div>
        </Container>
    </footer>
</template>

<style scoped>
.footer {
    background-color: #0E0D18;
    font-size: 14px;
    padding: 35px 0;
}

.columns {
    padding-top: 30px;
    width: 100%;
}

.link_column_header {
    color: #fff;
    font-size: 16px;
    margin-bottom: 20px;
}

.links {
    color: #757575;
    cursor: url('~/assets/icons/cursor-pointer.svg'), pointer;
}

.link {
    display: block;
    border: none;
    background-color: transparent;
    text-decoration: none;
    color: inherit;
    margin-bottom: 10px;
}

.link:hover {
    color: #FE9F00;
}

.footer_line {
    margin: 35px 0;
    background-color: #3F3E3E;
    height: 1px;
}

.information .text {
    color: #B9B8B8;
    height: 100%;
}
</style>