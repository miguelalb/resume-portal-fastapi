<template>
  <div class="absolute inset-1/3 z-20 border-2 shadow-md rounded-lg p-1 w-auto h-56 bg-slate-700 text-white">
    <div class="flex flex-row items-center p-2 gap-4">
      <img :src="require('@/assets/icons/55-error-outline.gif')" alt="Alert Icon" class="w-24">
      <div class="alert-body">
        <div class="font-semibold my-1">
          {{alert.title}}
        </div>
        <div>
          {{alert.content}}
        </div>
      </div>
      <span class="absolute top-2 right-2 cursor-pointer" @click="closeAlert">&#10006;</span>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
    name: 'AlertBox',
    computed: {
      ...mapState({
        alert: state => state.error.errorMessage
      }),
    },
    methods: {
      ...mapActions({
            closeAlert: 'error/clearError'
        })
    }
}
</script>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>