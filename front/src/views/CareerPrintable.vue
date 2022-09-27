<template>
  <VContainer class="pa-6" fluid>
    <VCardText> Cliquez sur le tableau pour imprimer</VCardText>
    <div id="table" @click="print">
      <VDataTable
        sort-by="intitule"
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
  name: "CareerPage",
  methods: {
    print() {
      this.$htmlToPaper("table");
    },
    async getObjects() {
      this.objects = [];
      instance
        .get("/career/")
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
        { text: "Intitulé", align: "start", value: "intitule" },
        { text: "Type", align: "start", value: "type" },
        { text: "Entreprise", align: "start", value: "entreprise" },
        { text: "Adresse", align: "start", value: "adresse" },
        { text: "Etat", align: "start", value: "etat" },
      ],
      objects: [],
    };
  },
  created() {
    document.title = "CareerManager - MyManager";
    this.getObjects();
  },
};
</script>

<style>
</style>