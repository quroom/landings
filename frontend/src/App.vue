<template>
  <div class="container mx-auto max-w-sm">
    <router-view></router-view>
    <div class="mt-2 block text-center">
      <Modal id="opinionModal">
        <template v-slot:btn>
          <button
            type="button"
            class="inline-block rounded bg-slate-500 px-6 py-2.5 text-xs font-medium uppercase leading-tight text-white shadow-md transition duration-150 ease-in-out hover:bg-slate-600 hover:shadow-lg focus:bg-slate-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-slate-700 active:shadow-lg"
            data-bs-toggle="modal"
            data-bs-target="#opinionModal"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="m-auto h-6 w-6"
            >
              <path
                fill-rule="evenodd"
                d="M4.848 2.771A49.144 49.144 0 0112 2.25c2.43 0 4.817.178 7.152.52 1.978.292 3.348 2.024 3.348 3.97v6.02c0 1.946-1.37 3.678-3.348 3.97a48.901 48.901 0 01-3.476.383.39.39 0 00-.297.17l-2.755 4.133a.75.75 0 01-1.248 0l-2.755-4.133a.39.39 0 00-.297-.17 48.9 48.9 0 01-3.476-.384c-1.978-.29-3.348-2.024-3.348-3.97V6.741c0-1.946 1.37-3.68 3.348-3.97z"
                clip-rule="evenodd"
              />
            </svg>
            의견남기기(이벤트)
          </button>
        </template>
        <template #title>소중한의견</template>
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
            <textarea
              class="form-control m-0 block w-full rounded border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-1.5 text-base font-normal text-gray-700 transition ease-in-out focus:border-blue-600 focus:bg-white focus:text-gray-700 focus:outline-none"
              id="exampleFormControlTextarea13"
              rows="3"
              placeholder="귀중한 의견을 남겨주신 고객님께는 추첨을 통하여 치킨 기프티콘을 드립니다."
            ></textarea>
          </div>
          <div class="form-group form-check mb-6 text-center">
            <input
              type="checkbox"
              class="form-check-input mt-1 mr-2 h-4 w-4 cursor-pointer appearance-none rounded-sm border border-gray-300 bg-white bg-contain bg-center bg-no-repeat align-top transition duration-200 checked:border-blue-600 checked:bg-blue-600 focus:outline-none"
              id="exampleCheck87"
              checked
            />
            <label
              class="form-check-label inline-block text-gray-800"
              for="exampleCheck87"
              >나에게도 이 내용을 보내기</label
            >
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
            소중한 의견제출
          </button>
        </template>
      </Modal>
    </div>
  </div>
</template>

<script>
import ContactForm from "@/components/ContactForm.vue";
import Modal from "@/components/Modal.vue";
export default {
  name: "app",
  components: { ContactForm, Modal },
};
</script>

<style scoped></style>
