<template>
  <VContainer class="pa-6" fluid>
    <VCardText> Cliquez sur le tableau pour imprimer</VCardText>
    <div id="table" @click="print">
      <VDataTable
        sort-by="date_arrivee"
        class="px-6 py-0"
        :headers="headers"
        :search="search"
        :items="objects"
        :items-per-page="-1"
        hide-default-footer
      >
      </VDataTable>
    </div>
  </VContainer>
</template>

<script>
import instance from "@/plugins/axios";

export default {
  name: "RentPrintable",
  methods: {
    print() {
      this.$htmlToPaper("table");
    },
    async getObjects() {
      this.objects = [];
      instance
        .get("/rent/")
        .then((response) => response.data)
        .then((offers) => {
          this.objects = offers;
        });
    },
  },
  data() {
    return {
      search: "",
      headers: [
        { text: "Prénom", align: "start", value: "prenom" },
        { text: "Nom", align: "start", value: "nom" },
        { text: "Numéro de téléphone", align: "start", value: "telephone" },
        { text: "Nationalité", align: "start", value: "nationalite" },
        { text: "Date d'entrée", align: "start", value: "date_arrivee" },
        { text: "Date de sortie", align: "start", value: "date_depart" },
        { text: "Loyer", align: "start", value: "loyer" },
        { text: "Commentaires", align: "start", value: "commentaires" },
      ],
      objects: [],
    };
  },
  created() {
    document.title = "RentManager - MyManager";
    this.getObjects();
  },
};
</script>

<style>
</style>