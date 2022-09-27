<template>
  <div style="background-color: #f8f9ff">
    <VCard class="ma-4 d-flex" outlined>
      <VCol>Accès DB : </VCol>
      <VCol cols="3">{{ db }}</VCol>
    </VCard>
    <VCard class="ma-4 d-flex" outlined>
      <VCol>MediaManager : </VCol>
      <VCol cols="3">{{ media }}</VCol>
    </VCard>
    <VCard class="ma-4 d-flex" outlined>
      <VCol>CareerManager : </VCol>
      <VCol cols="3">{{ career }}</VCol>
    </VCard>
    <VCard class="ma-4 d-flex" outlined>
      <VCol>RentManager : </VCol>
      <VCol cols="3">{{ rent }}</VCol>
    </VCard>
    <VCard class="ma-4 d-flex" outlined>
      <VCol>Connexion internet : </VCol>
      <VCol cols="3">{{ web }}</VCol>
    </VCard>
  </div>
</template>

<script>
import axios from "axios";
import instance from "../plugins/axios";

export default {
  name: "AboutComponent",
  data() {
    return {
      db: "Déconnecté",
      media: "Déconnecté",
      career: "Déconnecté",
      rent: "Déconnecté",
      web: "Déconnecté",
    };
  },
  methods: {
    async version() {
      this.db = "Déconnecté";
      this.media = "Déconnecté";
      this.career = "Déconnecté";
      this.rent = "Déconnecté";
      this.web = "Déconnecté";
      this.diagDb();
      this.diagMedia();
      this.diagCareer();
      this.diagRent();
      this.diagWeb();
    },
    async diagDb() {
      let db = await instance.get();
      if (db.status == 200) {
        this.db = "Connecté";
      } else {
        this.db = "Déconnecté";
      }
    },
    async diagMedia() {
      let media = await instance.get("/medias/");
      if (media.status == 200) {
        this.media = "Connecté";
      } else {
        this.media = "Déconnecté";
      }
    },
    async diagCareer() {
      let career = await instance.get("/career/");
      if (career.status == 200) {
        this.career = "Connecté";
      } else {
        this.career = "Déconnecté";
      }
    },
    async diagRent() {
      let rent = await instance.get("/rent/");
      if (rent.status == 200) {
        this.rent = "Connecté";
      } else {
        this.rent = "Déconnecté";
      }
    },
    async diagWeb() {
      let web = await axios.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json"
      );
      if (web) {
        this.web = "Connecté";
      } else {
        this.web = "Déconnecté";
      }
    },
  },
  async created() {
    this.version();
  },
};
</script>

<style>
</style>