<template>
  <VContainer class="pa-6" fluid>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined>
          <VCardTitle class="pt-6 pb-4 px-6">
            Bienvenue dans MyManager
          </VCardTitle>
          <VCardText class="px-6"
            >Que voulez-vous faire aujourd'hui ?</VCardText
          >
          <VRow class="justify-center">
            <VBtn
              outlined
              color="#005499"
              class="text-none ma-6"
              :to="{ name: 'medias' }"
              >Gérer ma médiathèque personnelle
            </VBtn>
          </VRow>
          <VRow class="justify-center">
            <VBtn
              outlined
              color="#005499"
              class="text-none ma-6"
              :to="{ name: 'career' }"
              >Gérer ma recherche de job</VBtn
            >
          </VRow>
          <VRow class="justify-center">
            <VBtn
              outlined
              color="#005499"
              class="text-none ma-6"
              :to="{ name: 'rent' }"
              >Gérer des locations</VBtn
            >
          </VRow>
        </VCard>
      </VCol>
    </VRow>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined>
          <VCardTitle class="pt-6 pb-4 px-6">
            Rechercher avec Google</VCardTitle
          >
          <VCardText> </VCardText>
          <VRow class="px-6 pr-10 d-flex justify-end">
            <VCol>
              <VTextField
                v-model="search"
                append-icon="mdi-magnify"
                outlined
                dense
                label="Rechercher"
              ></VTextField>
            </VCol>
            <VCol cols="1" class="mr-15">
              <VBtn
                outlined
                color="#005499"
                class="text-none mr-15"
                :href="getLink(search)"
                >Rechercher</VBtn
              >
            </VCol>
          </VRow>
        </VCard>
      </VCol>
    </VRow>
    <VRow class="justify-center">
      <VCol cols="10">
        <VCard outlined>
          <VCardTitle class="pt-6 pb-4 px-6"> Actualité </VCardTitle>
          <VCardText> </VCardText>
          <VCard class="mx-6 mb-6" outlined>
            <iframe
              src="https://fr.euronews.com/embed/timeline/"
              scrolling="no"
              style="border: none; min-height: 425px; width: 100%; height: 100%"
            ></iframe>
          </VCard>
        </VCard>
      </VCol>
    </VRow>
  </VContainer>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      search: "",
    };
  },
  methods: {
    getLink(search) {
      if (search != "") {
        let link = "http://www.google.fr/search?hl=fr&q=" + search;
        return link;
      }
      return search;
    },
  },
};
</script>

<style>
</style>