<script setup>
</script>

<template>
    <footer class="footer">
        <b-container>
        <b-row>
            <b-col cols="3" class="d-flex justify-content-center">
                <div>
                    <div class="link_column_header">Website Links</div>
                    <div class="links">
                        <div class="link">Home Page</div>
                        <div class="link">Parties & Lobbies</div>
                        <div class="link">Registration</div>
                        <div class="link">Support & FAQ</div>
                    </div>
                </div>
            </b-col>
            <b-col cols="3" class="d-flex justify-content-center">
                <div>
                    <div class="link_column_header">About Us</div>
                    <div class="links">
                        <div class="link">Instagram</div>
                        <div class="link">Steam</div>
                        <div class="link">GitHub</div>
                    </div>
                </div>
            </b-col>
            <b-col cols="3" class="d-flex justify-content-center">
                <div>
                    <div class="link_column_header">Other Projects</div>
                    <div class="links">
                        <div class="link">Flashy</div>
                        <div class="link">Coworkers</div>
                    </div>
                </div>
            </b-col>
            <b-col cols="3" class="d-flex justify-content-center">
                <div>
                    <div class="link_column_header">Language</div>
                    <div class="links">
                        <div class="link">Русский</div>
                        <div class="link">English</div>
                    </div>
                </div>
            </b-col>
        </b-row>

        <div class="footer_line"></div>

        <div class="information">
            <b-row>
                <b-col cols="9">
                    <div class="text d-flex align-items-center">WeGame - a brand owned by Alexandru Denis Ltd, located at 13 Kypranoros Str., Evi
                        Building, 1st Floor, Office 102, 1061 Chisinau, Moldova.
                        <br />Beware of false accounts and fraudsters who may
                        attempt to trade and scam users on any game platforms.
                    </div>
                </b-col>
                <b-col cols="3">
                    <div class="logo d-flex align-items-center justify-content-center">
                        <img src="../../assets/logo.png" alt="Logo" class="logo_icon">
                        <div class="logo_text">
                            WE<span class="accent">GAME</span>
                        </div>
                    </div>
                </b-col>
            </b-row>
        </div>
        </b-container>
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
    cursor: url('../../assets/cursor-pointer.svg'), pointer;
}

.link {
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