<template>
  <div style="background-color: #f8f9ff">
    <VCard class="d-flex ma-4 align-center" outlined>
      <VCol cols="4">Activer le lien Airbnb </VCol>
      <VCol>
        <VSwitch
          v-model="params.lien"
          inset
          color="orange"
          @change="changeLink($event)"
        ></VSwitch>
      </VCol>
    </VCard>
    <VCard class="d-flex ma-4 align-center" outlined>
      <VCol cols="4">Lien Airbnb </VCol>
      <VCol
        ><VTextField
          v-model="params.numero"
          outlined
          dense
          prefix="https://www.airbnb.com/rooms/"
          placeholder="numéro"
          persistent-hint
          hint="Entrez le numéro de votre annonce (composé de 18 chiffres)"
          @input="changeNumber($event)"
        ></VTextField
      ></VCol>
    </VCard>
    <VCard class="d-flex ma-4 align-center" outlined>
      <VCol cols="4">Loyer quotidien </VCol>
      <VCol
        ><VTextField
          v-model="params.loyer"
          class="priceField"
          reverse
          outlined
          dense
          prefix=" € "
          @input="changePrice($event)"
        ></VTextField
      ></VCol>
    </VCard>
  </div>
</template>

<script>
import axios from "axios";
import instance from "../plugins/axios";

export default {
  name: "RentSettingsComponent",
  data() {
    return {
      params: [],
    };
  },
  methods: {
    async initParams() {
      await instance({
        method: "post",
        url: "/locparams/",
        data: {
          lien: true,
          numero: "00000000000000000",
          loyer: "100.00",
        },
      });
    },
    async diagParams() {
      let params = [];
      await instance
        .get("/locparams/")
        .then((response) => response.data)
        .then((offers) => {
          params = offers;
        });
      if (params.length == 0) {
        await this.initParams();
        params = await this.diagParams();
      }
      return params;
    },
    async changeLink(value) {
      const request_data = {
        ...this.params,
        lien: value,
      };
      await instance({
        method: "patch",
        url: "/locparams/1/",
        data: request_data,
      });
    },
    async changeNumber(value) {
      const request_data = {
        ...this.params,
        numero: value,
      };
      await instance({
        method: "patch",
        url: "/locparams/1/",
        data: request_data,
      });
    },
    async changePrice(value) {
      const request_data = {
        ...this.params,
        loyer: value,
      };
      await instance({
        method: "patch",
        url: "/locparams/1/",
        data: request_data,
      });
    },
  },
  async created() {
    let params = await this.diagParams();
    this.params = params[0];
  },
};
</script>

<style>
</style>