<template>
  <div class="">
    <slot name="btn"></slot>
  </div>
  <div
    class="fade modal fixed top-0 hidden h-full w-full max-w-sm overflow-y-auto overflow-x-hidden outline-none"
    :id="id"
    tabindex="-1"
    :aria-labelledby="id"
    aria-modal="true"
    role="dialog"
  >
    <div
      class="modal-dialog modal-dialog-centered modal-dialog-scrollable pointer-events-none relative w-auto"
    >
      <div
        class="modal-content pointer-events-auto relative flex w-full flex-col rounded-md border-none bg-white bg-clip-padding text-current shadow-lg outline-none"
      >
        <div
          class="modal-header flex flex-shrink-0 items-center justify-between rounded-t-md border-b border-gray-200 p-4"
        >
          <h5
            class="text-xl font-medium leading-normal text-gray-800"
            :id="`${id}Label`"
          >
            <slot name="title"></slot>
          </h5>
          <button
            type="button"
            class="btn-close box-content h-4 w-4 rounded-none border-none p-1 text-black opacity-50 hover:text-black hover:no-underline hover:opacity-75 focus:opacity-100 focus:shadow-none focus:outline-none"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body relative p-4">
          <slot name="body"></slot>
        </div>
        <div
          class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end rounded-b-md border-t border-gray-200 p-4"
        >
          <slot name="footer"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Modal",
  props: {
    id: {
      type: String,
      required: true,
    },
  },
};
</script>

<style></style>
