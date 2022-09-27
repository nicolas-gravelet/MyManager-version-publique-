<template>
  <VContainer class="pa-6" fluid>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined>
          <VCardTitle class="pt-6 pb-4 px-6"
            ><VCol cols="6">Mes locataires </VCol>
            <VCol cols="6"
              ><VBtn
                dark
                color="#005499"
                block
                class="text-none"
                :to="{ name: 'rent-print' }"
                ><VIcon class="pr-2">mdi-printer</VIcon>Version imprimable</VBtn
              ></VCol
            ></VCardTitle
          >
          <VTextField
            v-model="search"
            append-icon="mdi-magnify"
            label="Rechercher un locataire"
            single-line
            hide-details
            outlined
            dense
            class="px-9 pb-3"
          ></VTextField>
          <VDataTable
            sort-by="date_arrivee"
            class="px-6 py-0"
            :headers="headers"
            :search="search"
            :items="objects"
          >
            <template v-slot:[`item.loyer`]="{ item }">
              {{ item.loyer }} €
            </template>
            <template v-slot:[`item.commentaires`]="{ item }">
              <VTextarea
                v-model="item.commentaires"
                :items="commentaires"
                class="mt-7"
                rows="1"
                outlined
                auto-grow
                dense
                @input="changeComment($event, item)"
              >
              </VTextarea>
            </template>
            <template v-slot:[`item.id`]="{ item }">
              <VBtn
                outlined
                color="red"
                class="text-none"
                @click="openDeleteMessage(item)"
                ><VIcon class="pr-2">mdi-delete</VIcon>Supprimer
              </VBtn>
            </template>
          </VDataTable>
        </VCard>
      </VCol>
    </VRow>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined class="pa-2">
          <VCardTitle class="pt-6 pb-4 px-6">
            <VCol cols="6"> Ajouter un locataire </VCol>
            <VCol cols="6">
              <VBtn
                :disabled="!params.lien"
                dark
                color="#005499"
                block
                class="text-none"
                :href="link"
                >Consulter l'offre sur Airbnb
              </VBtn>
            </VCol>
          </VCardTitle>
          <VForm class="pa-6 py-0 mx-3">
            <VRow>
              <VCol class="text-center">
                <VTextField
                  v-model="prenom"
                  outlined
                  dense
                  label="Prénom"
                ></VTextField>
                <VTextField
                  v-model="nom"
                  outlined
                  dense
                  label="Nom"
                ></VTextField>
                <VTextField
                  v-model="telephone"
                  outlined
                  dense
                  label="Numéro de téléphone"
                ></VTextField>
                <VTextField
                  v-model="nationalite"
                  outlined
                  dense
                  label="Nationalité"
                ></VTextField>
                <VRow class="px-3 pb-7 justify-space-around">
                  <VCard outlined class="pa-2">
                    <VCardText>Dates du séjour</VCardText>
                    <VDatePicker
                      v-model="dates"
                      range
                      dense
                      locale="fr-fr"
                      color="#005499"
                      landscape
                      full-width
                      @click:date="setDates()"
                    ></VDatePicker>
                  </VCard>
                </VRow>
                <VTextField
                  class="priceField"
                  reverse
                  v-model="loyer"
                  outlined
                  dense
                  prefix=" € "
                  label="Loyer"
                ></VTextField>
                <VTextField
                  v-model="commentaires"
                  outlined
                  dense
                  label="Commentaires"
                ></VTextField>
                <VBtn
                  dark
                  color="green"
                  class="text-none mt-2"
                  @click="createOffer()"
                  ><VIcon class="pr-2">mdi-plus</VIcon>Ajouter
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
            locataire</VCardTitle
          >
        </VToolbar>
        <VCard tile class="pa-4" color="#f8f9ff">
          <div>
            <VCard class="d-flex ma-4" outlined>
              <VCardText> Voulez-vous supprimer ce locataire ? </VCardText>
            </VCard>
            <VCard class="ma-4" outlined>
              <VCard class="ma-1 d-flex">
                <VCol>Identité : </VCol>
                <VCol>{{ item.prenom }} {{ item.nom }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Numéro de téléphone : </VCol>
                <VCol>{{ item.telephone }}</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Dates du séjour : </VCol>
                <VCol
                  >Du {{ item.date_arrivee }} au {{ item.date_depart }}</VCol
                >
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Loyer : </VCol>
                <VCol>{{ item.loyer }} €</VCol>
              </VCard>
              <VCard class="ma-1 d-flex">
                <VCol>Commentaires : </VCol>
                <VCol>{{ item.commentaires }}</VCol>
              </VCard>
            </VCard>
            <VRow class="justify-center">
              <VBtn
                class="ma-6 text-none"
                dark
                color="red"
                @click="deleteRent(item.id)"
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
import moment from "moment";
import instance from "@/plugins/axios";

export default {
  name: "RentPage",
  methods: {
    async getObjects() {
      this.objects = [];
      instance
        .get("/rent/")
        .then((response) => response.data)
        .then((offers) => {
          this.objects = offers;
        });
    },
    async getParams() {
      let params = [];
      await instance
        .get("/locparams/")
        .then((response) => response.data)
        .then((offers) => {
          params = offers;
        });
      if (params.length == 0) {
        params = {
          lien: true,
          numero: "00000000000000000",
          loyer: "100.00",
        };
      }
      return params;
    },
    openDeleteMessage(item) {
      this.del = true;
      this.item = item;
    },
    async deleteRent(id) {
      await instance({
        method: "delete",
        url: "/rent/" + id + "/",
      });
      this.del = false;
      this.getObjects();
    },
    async changeComment(value, rent) {
      const request_data = {
        ...rent,
        commentaires: value,
      };
      await instance({
        method: "patch",
        url: "/rent/" + rent.id + "/",
        data: request_data,
      });
    },
    async setDates() {
      this.date_arrivee = this.dates[0];
      this.date_depart = this.dates[1];
      if (this.date_arrivee && this.date_depart) {
        let da = moment(this.date_arrivee, "YYYY-MM-DD");
        let dd = moment(this.date_depart, "YYYY-MM-DD");
        let nb_jours = dd.diff(da, "days", false) + 1;
        this.loyer = String(nb_jours * parseInt(this.params.loyer) + ".00");
      }
    },
    async createOffer() {
      await instance({
        method: "post",
        url: "/rent/",
        data: {
          prenom: this.prenom,
          nom: this.nom,
          telephone: this.telephone,
          nationalite: this.nationalite,
          date_arrivee: this.date_arrivee,
          date_depart: this.date_depart,
          loyer: this.loyer,
          commentaires: this.commentaires,
        },
      });
      this.getObjects();
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
        { align: "start", value: "id", width: "8%" },
      ],
      objects: [],
      prenom: "",
      nom: "",
      telephone: "",
      nationalite: "",
      dates: [],
      date_arrivee: "",
      date_depart: "",
      loyer: "",
      commentaires: "",
      del: false,
      item: [],
      params: [],
      link: "",
    };
  },
  computed: {
    getDates() {
      this.date_arrivee = this.dates[0];
      this.date_depart = this.dates[1];
      console.log(this.date_arrivee, this.date_depart);
      return 0;
    },
  },
  async created() {
    document.title = "RentManager - MyManager";
    this.getObjects();
    let params = await this.getParams();
    this.params = params[0];
    this.link = "https://www.airbnb.com/rooms/" + this.params.numero;
  },
  async updated() {
    let params = await this.getParams();
    this.params = params[0];
    this.link = "https://www.airbnb.com/rooms/" + this.params.numero;
  },
};
</script>

<style>
</style>