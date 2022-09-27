<template>
  <VApp id="app">
    <VAppBar id="main-navbar" app color="white" height="56px">
      <VCol class="d-flex">
        <VToolbarTitle class="d-flex align-center">
          <span class="mr-1 font-weight-bold">MyManager</span>
          <VCol />
        </VToolbarTitle>
        <VDivider vertical />
      </VCol>
      <VTabs color="#005499" show-arrows fixed-tabs centered optional>
        <VTab :to="{ name: 'medias' }"
          ><VIcon class="pr-2">mdi-play-circle</VIcon> Media Manager</VTab
        >
        <VTab :to="{ name: 'career' }"
          ><VIcon class="pr-2">mdi-account-tie</VIcon>Career Manager</VTab
        >
        <VTab :to="{ name: 'rent' }"
          ><VIcon class="pr-2">mdi-home-group</VIcon>Rent Manager</VTab
        >
      </VTabs>
      <VCol class="d-flex justify-end">
        <VDivider vertical class="my-1" />
        <VIcon class="px-2" @click="panel = true">mdi-cog</VIcon>
        <VDivider vertical class="my-1" />
        <ToolbarTitle class="pl-8 align-end">
          <VRow no-gutters dense justify="end"> {{ date }}</VRow>
          <VRow no-gutters dense justify="end">{{ time }}</VRow>
        </ToolbarTitle>
      </VCol>
    </VAppBar>
    <VMain>
      <VDialog width="600px" persistent v-model="panel">
        <VCard outlined>
          <VToolbar dark color="#005499">
            <VCardTitle class="pa-2"
              ><VIcon class="pr-2">mdi-cog</VIcon>Panneau de
              configuration</VCardTitle
            >
          </VToolbar>
          <VTabs
            color="#005499"
            show-arrows
            fixed-tabs
            centered
            optional
            v-model="page"
          >
            <VTab><VIcon class="pr-2">mdi-home-group</VIcon>Rent Manager</VTab>
            <VTab
              ><VIcon class="pr-2">mdi-help-network</VIcon>Etat des
              services</VTab
            >
          </VTabs>
          <VCard tile class="pa-4" color="#f8f9ff" height="765px">
            <VTabsItems v-model="page" style="background-color: #f8f9ff">
              <VTabItem><RentSettingsComponent /></VTabItem>
              <VTabItem><AboutComponent /></VTabItem>
            </VTabsItems>
            <VRow class="justify-center">
              <VBtn
                dark
                class="text-none ma-6"
                color="#005499"
                @click="panel = false"
                ><VIcon class="pr-2">mdi-close</VIcon>Fermer</VBtn
              >
            </VRow>
            <slot />
          </VCard>
        </VCard>
      </VDialog>
      <RouterView />
    </VMain>
    <VRow style="height: 56px"> </VRow>
    <footer style="position: fixed; bottom: 0px; left: 0px; right: 0px">
      <VToolbar id="footer" color="white" height="56px">
        <VCol>
          <VRow no-gutters dense justify="center" @click="panel = true"
            >MyManager - 2022</VRow
          >
        </VCol>
      </VToolbar>
    </footer>
  </VApp>
</template>

<script>
import RentSettingsComponent from "./components/RentSettingsComponent.vue";
import AboutComponent from "./components/AboutComponent.vue";

export default {
  name: "App",
  components: {
    AboutComponent,
    RentSettingsComponent,
  },
  data() {
    return {
      date: "",
      time: "",
      timer: "",
      panel: false,
      page: 0,
    };
  },
  methods: {
    currentDate() {
      const current = new Date();
      const date =
        current.getDate().toString().padStart(2, "0") +
        "/" +
        (current.getMonth() + 1).toString().padStart(2, "0") +
        "/" +
        current.getFullYear();

      this.date = date;
    },
    currentTime() {
      const current = new Date();
      const time =
        current.getHours().toString().padStart(2, "0") +
        ":" +
        current.getMinutes().toString().padStart(2, "0") +
        ":" +
        current.getSeconds().toString().padStart(2, "0");

      this.time = time;
    },
  },
  async created() {
    this.currentDate();
    this.currentTime();
    this.timer = setInterval(this.currentDate, 1);
    this.timer = setInterval(this.currentTime, 1);
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap");

:root {
  background-color: #f8f9ff;
  font-family: "Roboto", sans-serif;
  line-height: 1.5;
}

#app {
  background-color: #f8f9ff !important;
}

#main-navbar {
  background-color: white;
  box-shadow: 0 1px 1px 0 #eceef3 !important;

  .v-toolbar__content {
    padding: 0 24px;
  }
}

#footer {
  background-color: white;
  box-shadow: 1px 0 0 1px #eceef3 !important;

  .v-toolbar__content {
    padding: 0 24px;
  }
}
</style>
