<template>
  <VContainer class="pa-6" fluid>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined>
          <VCardTitle class="pt-6 pb-4 px-6">
            <VCol cols="6">Mes offres </VCol>
            <VCol cols="6">
              <VBtn
                dark
                color="#005499"
                block
                class="text-none"
                :to="{ name: 'career-print' }"
                ><VIcon class="pr-2">mdi-printer</VIcon>Version imprimable</VBtn
              >
            </VCol>
          </VCardTitle>
          <VTextField
            v-model="search"
            append-icon="mdi-magnify"
            label="Rechercher une offre"
            single-line
            hide-details
            outlined
            dense
            class="px-9 pb-3"
          ></VTextField>
          <VDataTable
            sort-by="intitule"
            class="px-6 py-0"
            :headers="headers"
            :search="search"
            :items="objects"
          >
            <template v-slot:[`item.intitule`]="{ item }">
              <a :href="item.url">{{ item.intitule }}</a>
            </template>
            <template v-slot:[`item.etat`]="{ item }">
              <VSelect
                v-model="item.etat"
                :items="states"
                class="mt-7"
                outlined
                dense
                @change="changeState($event, item)"
              >
              </VSelect>
            </template>
            <template v-slot:[`item.id`]="{ item }">
              <VBtn
                outlined
                color="red"
                class="text-none"
                @click="openDeleteMessage(item)"
                ><VIcon class="pr-2">mdi-delete</VIcon>Supprimer</VBtn
              >
            </template>
          </VDataTable>
        </VCard>
      </VCol>
    </VRow>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined class="pa-2">
          <VCardTitle class="pt-6 pb-4 px-6"
            >Plateformes de recrutement
          </VCardTitle>
          <VRow dense class="pa-6 py-1 mx-3 justify-center">
            <VBtn
              dark
              class="text-none ma-1"
              color="blue"
              href="https://epitech.jobteaser.com/"
              >Career Development Center</VBtn
            >
            <VBtn
              class="text-none ma-1"
              color="rgb(255, 205, 0)"
              href="https://www.welcometothejungle.com/fr"
              >Welcome to the Jungle</VBtn
            >
            <VBtn
              class="text-none ma-1"
              color="#8782ff"
              href="https://jobs.wizbii.com/"
              >Wizbii Jobs</VBtn
            >
            <VBtn
              dark
              class="text-none ma-1"
              color="#005499"
              href="https://www.linkedin.com/"
              >LinkedIn</VBtn
            >
            <VBtn
              dark
              class="text-none ma-1"
              color="#005499"
              href="https://fr.indeed.com/"
              >Indeed</VBtn
            >
            <VBtn
              class="text-none ma-1"
              color="white"
              href="https://www.hellowork.com/fr-fr"
              >HelloWork</VBtn
            >
            <VBtn
              dark
              class="text-none ma-1"
              color="blue"
              href="https://app.kerteam.com/"
              >Kerteam</VBtn
            >
            <VBtn
              dark
              class="text-none ma-1"
              color="green"
              href="https://www.jobibou.com/"
              >Jobibou</VBtn
            >
          </VRow>
        </VCard>
      </VCol>
    </VRow>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined class="pa-2">
          <VCardTitle class="pt-6 pb-4 px-6">Ajouter une offre </VCardTitle>
          <VForm class="pa-6 py-0 mx-3">
            <VRow>
              <VCol class="text-center">
                <VTextField
                  v-model="intitule"
                  outlined
                  dense
                  label="Intitulé"
                ></VTextField>
                <VSelect
                  v-model="type"
                  :items="types"
                  outlined
                  dense
                  label="Type"
                ></VSelect>
                <VTextField
                  v-model="entreprise"
                  outlined
                  dense
                  label="Entreprise"
                ></VTextField>
                <VTextField
                  v-model="adresse"
                  outlined
                  dense
                  label="Adresse"
                ></VTextField>
                <VSelect
                  v-model="etat"
                  :items="states"
                  outlined
                  dense
                  label="Etat"
                ></VSelect>
                <VTextField
                  v-model="url"
                  outlined
                  dense
                  label="Lien hypertexte"
                ></VTextField>
                <VBtn
                  dark
                  color="green"
                  class="text-none mt-2"
                  @click="createOffer()"
                  ><VIcon class="pr-2">mdi-plus</VIcon>Ajouter</VBtn
                >
              </VCol>
            </VRow>
          </VForm>
        </VCard>
      </VCol>
    </VRow>
    <VDialog width="600px" persistent v-model="del">
      <VCard outlined>
        <VToolbar dark color="red">
          <VCardTitle class="pa-2"
            ><VIcon class="pr-2">mdi-delete</VIcon>Supprimer une
            offre</VCardTitle
          >
        </VToolbar>
        <VCard tile class="pa-4" color="#f8f9ff">
          <div>
            <VCard class="d-flex ma-4" outlined>
              <VCardText> Voulez-vous supprimer cette offre ? </VCardText>
            </VCard>
            <VCard class="ma-4" outlined>
              <VCard class="ma-1 d-flex">
                <VCol>Intitulé : </VCol>
                <VCol>{{ item.intitule }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Type : </VCol>
                <VCol>{{ item.type }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Entreprise : </VCol>
                <VCol>{{ item.entreprise }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Adresse : </VCol>
                <VCol>{{ item.adresse }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Etat : </VCol>
                <VCol>{{ item.etat }}</VCol>
              </VCard>
            </VCard>
            <VRow class="justify-center">
              <VBtn
                class="ma-6 text-none"
                dark
                color="red"
                @click="deleteOffer(item.id)"
                ><VIcon class="pr-2">mdi-delete</VIcon>Supprimer</VBtn
              >
              <VBtn
                class="ma-6 text-none"
                dark
                color="#005499"
                @click="del = false"
                ><VIcon class="pr-2">mdi-close</VIcon>Annuler</VBtn
              >
            </VRow>
          </div>
          <slot />
        </VCard>
      </VCard>
    </VDialog>
  </VContainer>
</template>

<script>
import instance from "@/plugins/axios";

export default {
  name: "CareerPage",
  methods: {
    async getObjects() {
      this.objects = [];
      instance
        .get("/career/")
        .then((response) => response.data)
        .then((offers) => {
          this.objects = offers;
        });
    },
    openDeleteMessage(item) {
      this.del = true;
      this.item = item;
    },
    async deleteOffer(id) {
      await instance({
        method: "delete",
        url: "/career/" + id + "/",
      });
      this.del = false;
      this.getObjects();
    },
    async changeState(value, offer) {
      const request_data = {
        ...offer,
        etat: value,
      };
      await instance({
        method: "patch",
        url: "/career/" + offer.id + "/",
        data: request_data,
      });
      this.getObjects();
    },
    async createOffer() {
      await instance({
        method: "post",
        url: "/career/",
        data: {
          intitule: this.intitule,
          type: this.type,
          entreprise: this.entreprise,
          adresse: this.adresse,
          etat: this.etat,
          url: this.url,
        },
      });
      this.getObjects();
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
        { align: "start", value: "id", width: "8%" },
      ],
      objects: [],
      types: ["Stage", "Alternance", "Intérim", "CDD", "CDI"],
      states: [
        "Non postulé",
        "A voir",
        "Postulé",
        "Entretien à venir",
        "Process de recrutement en cours",
        "Recalé",
        "Accepté",
      ],
      intitule: "",
      type: "",
      entreprise: "",
      adresse: "",
      etat: "",
      url: "",
      del: false,
      item: [],
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