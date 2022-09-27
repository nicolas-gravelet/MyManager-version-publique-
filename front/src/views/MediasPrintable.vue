<template>
  <VContainer class="pa-6" fluid>
    <VCardText> Cliquez sur le tableau pour imprimer</VCardText>
    <div id="table" @click="print">
      <VDataTable
        sort-by="titre"
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
  name: "MediasPrintable",
  methods: {
    print() {
      this.$htmlToPaper("table");
    },
    async getObjects() {
      this.objects = [];
      instance
        .get("/medias/")
        .then((response) => response.data)
        .then((medias) => {
          this.objects = medias;
        });
    },
  },
  data() {
    return {
      search: "",
      headers: [
        { text: "Titre", align: "start", value: "titre" },
        { text: "Type", align: "start", value: "type" },
        { text: "Genre", align: "start", value: "genre" },
        { text: "Production", align: "start", value: "studios" },
        { text: "Support", align: "start", value: "support" },
        { text: "Année", align: "start", value: "annee" },
        { text: "Etat", align: "start", value: "etat" },
      ],
      objects: [],
    };
  },
  created() {
    document.title = "MediaManager - MyManager";
    this.getObjects();
  },
};
</script>

<style>
</style>