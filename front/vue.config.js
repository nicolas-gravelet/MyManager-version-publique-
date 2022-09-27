module.exports = {
  lintOnSave: false,

  // CHOOSE A PORT FOR A NEW FRONT PROJECT
  devServer: {
    port: 8080
  },

  pluginOptions: {
    i18n: {
      locale: "fr",
      fallbackLocale: "fr",
      localeDir: "lang",
      enableInSFC: true
    }
  },

  transpileDependencies: ["vuetify"]
};
