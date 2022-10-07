<template>
  <div class="mx-auto mt-2 block max-w-md rounded-lg bg-white p-6 shadow-lg">
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
        placeholder="연락처(선택)"
      />
    </div>
    <button
      type="submit"
      class="w-full rounded bg-blue-600 px-6 py-2.5 text-xs font-medium uppercase leading-tight text-white shadow-md transition duration-150 ease-in-out hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg"
    >
      전송
    </button>
  </div>
</template>

<script>
export default {
  name: "ContactForm",
};
</script>

<style></style>
