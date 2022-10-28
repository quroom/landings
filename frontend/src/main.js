import router from "./router";
import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "tw-elements";

import * as Vue from "vue"; // in Vue 3
import axios from "axios";
import VueAxios from "vue-axios";

const app = createApp(App);
app.use(VueAxios, axios);
app.use(router);
app.mount("#app");
