<template>
  <div>
    <div
      v-for="landing in landings"
      :key="landing"
      class="mb-2 rounded-lg bg-white shadow-lg"
    >
      <div class="relative">
        <div class="absolute block h-full w-full bg-black bg-opacity-40">
          <h5 class="mt-4 text-center text-2xl font-bold text-white">
            {{ landing.title }}
          </h5>
        </div>
        <a href="#!">
          <img class="rounded-t-lg" :src="landing.img" alt="그림" />
        </a>
        <button
          type="button"
          class="absolute bottom-0 inline-block h-20 rounded bg-red-600 px-6 py-2.5 text-xs font-medium uppercase leading-tight text-white shadow-md transition duration-150 ease-in-out hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-red-800 active:shadow-lg"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="m-auto h-6 w-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M7.5 15h2.25m8.024-9.75c.011.05.028.1.052.148.591 1.2.924 2.55.924 3.977a8.96 8.96 0 01-.999 4.125m.023-8.25c-.076-.365.183-.75.575-.75h.908c.889 0 1.713.518 1.972 1.368.339 1.11.521 2.287.521 3.507 0 1.553-.295 3.036-.831 4.398C20.613 14.547 19.833 15 19 15h-1.053c-.472 0-.745-.556-.5-.96a8.95 8.95 0 00.303-.54m.023-8.25H16.48a4.5 4.5 0 01-1.423-.23l-3.114-1.04a4.5 4.5 0 00-1.423-.23H6.504c-.618 0-1.217.247-1.605.729A11.95 11.95 0 002.25 12c0 .434.023.863.068 1.285C2.427 14.306 3.346 15 4.372 15h3.126c.618 0 .991.724.725 1.282A7.471 7.471 0 007.5 19.5a2.25 2.25 0 002.25 2.25.75.75 0 00.75-.75v-.633c0-.573.11-1.14.322-1.672.304-.76.93-1.33 1.653-1.715a9.04 9.04 0 002.86-2.4c.498-.634 1.226-1.08 2.032-1.08h.384"
            />
          </svg>
          별로요
        </button>
        <button
          type="button"
          class="absolute right-0 bottom-0 inline-block h-20 rounded bg-blue-600 px-6 py-2.5 text-xs font-medium uppercase leading-tight text-white shadow-md transition duration-150 ease-in-out hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="m-auto h-6 w-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M6.633 10.5c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 012.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 00.322-1.672V3a.75.75 0 01.75-.75A2.25 2.25 0 0116.5 4.5c0 1.152-.26 2.243-.723 3.218-.266.558.107 1.282.725 1.282h3.126c1.026 0 1.945.694 2.054 1.715.045.422.068.85.068 1.285a11.95 11.95 0 01-2.649 7.521c-.388.482-.987.729-1.605.729H13.48c-.483 0-.964-.078-1.423-.23l-3.114-1.04a4.501 4.501 0 00-1.423-.23H5.904M14.25 9h2.25M5.904 18.75c.083.205.173.405.27.602.197.4-.078.898-.523.898h-.908c-.889 0-1.713-.518-1.972-1.368a12 12 0 01-.521-3.507c0-1.553.295-3.036.831-4.398C3.387 10.203 4.167 9.75 5 9.75h1.053c.472 0 .745.556.5.96a8.958 8.958 0 00-1.302 4.665c0 1.194.232 2.333.654 3.375z"
            />
          </svg>
          좋아요
          <div class="block h-4">({{ landing.likes }})</div>
        </button>
      </div>
      <div class="px-4 pt-2">
        <p class="text-base text-gray-700">
          {{ landing.detail }}
        </p>
      </div>
      <div class="text-center">
        <Modal :id="`launchAlarm${landing.id}`">
          <template #title> {{ `${landing.title} 출시알람` }} </template>
          <template v-slot:btn>
            <button
              type="button"
              class="mb-2 inline-block rounded bg-blue-600 px-4 py-2.5 text-xs font-medium uppercase leading-tight text-white shadow-md transition duration-150 ease-in-out hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg"
              data-bs-toggle="modal"
              :data-bs-target="`#launchAlarm${landing.id}`"
            >
              출시알람받기
            </button>
          </template>
          <template #body>
            <div class="form-group mb-6">
              <input
                type="email"
                class="form-control m-0 block w-full rounded border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-1.5 text-base font-normal text-gray-700 transition ease-in-out focus:border-blue-600 focus:bg-white focus:text-gray-700 focus:outline-none"
                id="exampleInput8"
                placeholder="이메일"
              />
            </div>
            <div class="form-group mb-6">
              <input
                type="text"
                class="form-control m-0 block w-full rounded border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-1.5 text-base font-normal text-gray-700 transition ease-in-out focus:border-blue-600 focus:bg-white focus:text-gray-700 focus:outline-none"
                id="exampleInput7"
                placeholder="연락처"
              />
            </div>
          </template>
          <template v-slot:footer>
            <button
              type="button"
              class="ml-1 inline-block rounded bg-blue-600 px-6 py-2.5 text-xs font-medium uppercase leading-tight text-white shadow-md transition duration-150 ease-in-out hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg"
            >
              사전예약
            </button>
          </template>
        </Modal>
      </div>
    </div>
  </div>
</template>

<script>
import Modal from "@/components/Modal.vue";

export default {
  name: "LandingList",
  components: { Modal },
  data() {
    return {
      landings: [
        {
          id: 1,
          title: "거꾸로 부동산",
          img: "https://st.depositphotos.com/1194063/2151/i/450/depositphotos_21515189-stock-photo-agent-with-house-model-and.jpg",
          detail:
            "매물 찾느라 힘드세요? 매물 조건만 남기면 실시간으로\
          찾아서 알려드려요. 선택만 하세요.",
          likes: 50,
          dislikes: 5,
        },
        {
          id: 2,
          title: "비대면 부동산 방문",
          img: "https://www.onlinemarketplaces.com/wp-content/uploads/2021/07/Contactless-World-1.jpg",
          detail:
            "허위 매물로 고생하신 경험 있으세요? 첫 방문은 비대면으로! 허위매물 완벽차단!",
          likes: 20,
          dislikes: 5,
        },
      ],
    };
  },
};
</script>

<style></style>
