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
              <NuxtLinkLocale to="parties" class="link"
                >Parties & Lobbies</NuxtLinkLocale
              >
              <NuxtLinkLocale to="sign-up" class="link"
                >Registration</NuxtLinkLocale
              >
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
            <div class="text d-flex align-items-center">
              WeGame - a brand owned by Alexandru Denis Ltd, located at 13
              Kypranoros Str., Evi Building, 1st Floor, Office 102, 1061
              Chisinau, Moldova. <br />Beware of false accounts and fraudsters
              who may attempt to trade and scam users on any game platforms.
            </div>
          </Col>
          <Col col="3">
            <div class="logo d-flex align-items-center justify-content-center">
              <img src="/images/logo.png" alt="Logo" class="logo_icon" />
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
  background-color: #0e0d18;
  font-size: 14px;
  padding: 35px 0;

  @media screen and (max-width: 768px) {
    font-size: 12px;
  }

  @media screen and (max-width: 510px) {
    font-size: 10px;
  }

  @media screen and (max-width: 420px) {
    font-size: 8px;
  }
}

.columns {
  padding-top: 30px;
  width: 100%;
}

.link_column_header {
  color: #fff;
  font-size: 16px;
  margin-bottom: 20px;

  @media screen and (max-width: 768px) {
    font-size: 14px;
  }

  @media screen and (max-width: 510px) {
    font-size: 12px;
  }
  @media screen and (max-width: 420px) {
    font-size: 10px;
  }
}

.links {
  color: #757575;
  cursor: url("~/assets/icons/cursor-pointer.svg"), pointer;
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
  color: #fe9f00;
}

.footer_line {
  margin: 35px 0;
  background-color: #3f3e3e;
  height: 1px;

  @media screen and (max-width: 510px) {
    margin: 15px 0;
  }
}

.information .text {
  color: #b9b8b8;
  height: 100%;
}
</style>
