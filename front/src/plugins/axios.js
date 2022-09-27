import axios from "axios";

const instance = axios.create({
  baseURL: "http://" + window.location.hostname + ":8000/",
  timeout: 1000,
});

export default instance;
