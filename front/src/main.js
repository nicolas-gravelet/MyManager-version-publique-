import Vue from "vue";
import VueRouter from "vue-router";
import VueHtmlToPaper from "vue-html-to-paper";
import App from "./App.vue";
import vuetify from "@/plugins/vuetify";
import MediasPage from "./views/MediasPage.vue";
import MediasPrintable from "./views/MediasPrintable.vue"
import CareerPage from "./views/CareerPage.vue";
import CareerPrintable from "./views/CareerPrintable.vue"
import RentPage from "./views/RentPage.vue";
import RentPrintable from "./views/RentPrintable.vue"
import HomePage from "./views/HomePage.vue";

Vue.config.productionTip = false;
Vue.use(VueRouter);

const options = {
  name: "_blank",
  specs: [
      "fullscreen=yes",
      "titlebar=yes",
      "scrollbars=yes",
  ],
  styles: [
      "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css",
      "https://unpkg.com/kidlat-css/css/kidlat.css",
      "/table.css",
      "/vuetify.css"
  ]
}

Vue.use(VueHtmlToPaper, options);

const routes = [
  { path: "/", name: "home", component: HomePage },
  { path: "/media-manager", name: "medias", component: MediasPage },
  { path: "/media-manager/print", name: "medias-print", component: MediasPrintable },
  { path: "/career-manager", name: "career", component: CareerPage },
  { path: "/career-manager/print", name: "career-print", component: CareerPrintable },
  { path: "/rent-manager", name: "rent", component: RentPage },
  { path: "/rent-manager/print", name: "rent-print", component: RentPrintable },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
