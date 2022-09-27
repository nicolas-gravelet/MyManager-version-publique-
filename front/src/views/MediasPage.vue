<template>
  <VContainer class="pa-6" fluid>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined>
          <VCardTitle class="pt-6 pb-4 px-6">
            <VCol cols="6">Mes médias </VCol>
            <VCol cols="6"
              ><VBtn
                dark
                color="#005499"
                block
                class="text-none"
                :to="{ name: 'medias-print' }"
                ><VIcon class="pr-2">mdi-printer</VIcon>Version imprimable</VBtn
              ></VCol
            ></VCardTitle
          >
          <VTextField
            v-model="search"
            append-icon="mdi-magnify"
            label="Rechercher un média"
            single-line
            hide-details
            outlined
            dense
            class="px-9 pb-3"
          ></VTextField>
          <VDataTable
            sort-by="titre"
            class="px-6 py-0"
            :headers="headers"
            :search="search"
            :items="objects"
          >
            <template v-slot:[`item.etat`]="{ item }">
              <VSelect
                v-model="item.etat"
                :items="states"
                class="mt-7"
                outlined
                dense
                @change="changeState($event, item)"
              ></VSelect>
            </template>
            <template v-slot:[`item.id`]="{ item }">
              <VBtn
                outlined
                color="red"
                class="text-none"
                @click="openDeleteMessage(item)"
              >
                <VIcon class="pr-2">mdi-delete</VIcon>Supprimer
              </VBtn>
            </template>
          </VDataTable>
        </VCard>
      </VCol>
    </VRow>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined class="pa-2">
          <VCardTitle class="pt-6 pb-4 px-6"> Ajouter un média </VCardTitle>
          <VForm class="pa-6 py-0 mx-2">
            <VRow>
              <VCol class="text-center">
                <VTextField
                  v-model="titre"
                  outlined
                  dense
                  label="Titre"
                ></VTextField>
                <VSelect
                  v-model="type"
                  :items="types"
                  outlined
                  dense
                  label="Type"
                ></VSelect>
                <VSelect
                  v-model="genre"
                  :items="getGenre(type)"
                  outlined
                  dense
                  label="Genre"
                  :disabled="!type"
                >
                </VSelect>
                <VTextField
                  v-model="studios"
                  outlined
                  dense
                  label="Studios"
                ></VTextField>
                <VSelect
                  v-model="support"
                  :items="getSupport(type)"
                  outlined
                  dense
                  label="Support"
                  :disabled="!type"
                >
                </VSelect>
                <VTextField
                  v-model="annee"
                  outlined
                  dense
                  type="number"
                  label="Année"
                ></VTextField>
                <VSelect
                  v-model="etat"
                  :items="states"
                  outlined
                  dense
                  label="Etat"
                ></VSelect>
                <VBtn
                  dark
                  color="green"
                  class="text-none mt-2"
                  @click="createMedia()"
                >
                  <VIcon class="pr-2">mdi-plus</VIcon>Ajouter
                </VBtn>
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
            ><VIcon class="pr-2">mdi-delete</VIcon>Supprimer un
            média</VCardTitle
          >
        </VToolbar>
        <VCard tile class="pa-4" color="#f8f9ff">
          <div>
            <VCard class="d-flex ma-4" outlined>
              <VCardText> Voulez-vous supprimer ce média ? </VCardText>
            </VCard>
            <VCard class="ma-4" outlined>
              <VCard class="ma-1 d-flex">
                <VCol>Titre : </VCol>
                <VCol>{{ item.titre }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Type : </VCol>
                <VCol>{{ item.type }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Genre : </VCol>
                <VCol>{{ item.genre }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Production : </VCol>
                <VCol>{{ item.studios }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Support : </VCol>
                <VCol>{{ item.support }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Année de sortie : </VCol>
                <VCol>{{ item.annee }}</VCol>
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
                @click="deleteMedia(item.id)"
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
  name: "MediasPage",
  methods: {
    async getObjects() {
      this.objects = [];
      instance
        .get("/medias/")
        .then((response) => response.data)
        .then((medias) => {
          this.objects = medias;
        });
    },
    getGenre(type) {
      let genres = [];
      if (type == "Film") {
        genres = [
          "Comédie",
          "Comédie musicale",
          "Drame",
          "Fantastique",
          "Super-héros",
          "Science-fiction",
        ];
      }
      if (type == "Emission télévisée") {
        genres = ["Télé-réalité", "Sketches"];
      }
      if (type == "Jeu vidéo") {
        genres = ["Accessoire", "Aventure", "Courses", "Plateformes", "RPG"];
      }
      if (type == "Série TV") {
        genres = ["Comédie", "Drame", "Fantastique", "Science-fiction"];
      }
      return genres;
    },
    getSupport(type) {
      let supports = [];
      if (type == "Jeu vidéo") {
        supports = ["GameBoy", "GameCube", "PS4", "Switch"];
      } else {
        supports = ["Blu-ray", "DVD"];
      }
      return supports;
    },
    openDeleteMessage(item) {
      this.del = true;
      this.item = item;
    },
    async deleteMedia(id) {
      await instance({
        method: "delete",
        url: "/medias/" + id + "/",
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
        url: "/medias/" + offer.id + "/",
        data: request_data,
      });
      this.getObjects();
    },
    async createMedia() {
      await instance({
        method: "post",
        url: "/medias/",
        data: {
          titre: this.titre,
          type: this.type,
          genre: this.genre,
          studios: this.studios,
          support: this.support,
          annee: this.annee,
          etat: this.etat,
        },
      });
      this.getObjects();
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
        { text: "Etat", align: "start", value: "etat", width: "11%" },
        { align: "start", value: "id", width: "8%" },
      ],
      objects: [],
      types: ["Emission télévisée", "Film", "Jeu vidéo", "Série TV"],
      supports: [],
      genres: [],
      states: ["A voir", "En cours", "Terminé"],
      titre: "",
      type: "",
      genre: "",
      studios: "",
      support: "",
      annee: "",
      etat: "",
      del: false,
      item: [],
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