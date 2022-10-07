import { createRouter, createWebHistory } from "vue-router";
import LandingList from "../views/LandingList.vue";

const routes = [
  {
    path: "/",
    name: "landing-list",
    component: LandingList,
    meta: { title: "랜딩페이지 목록" },
  },
];

const router = createRouter({ history: createWebHistory(), routes });
export default router;
