<template>
  <div class="absolute inset-1/3 z-20 border-2 shadow-md rounded-lg p-1 w-96 h-48 bg-slate-200">
    <div class="flex flex-row items-center p-2 gap-4">
      <img :src="require('@/assets/icons/55-error-outline.gif')" alt="Alert Icon" class="w-24">
      <div class="alert-body">
        <div class="font-semibold my-1">
          <!-- {{alert.title}} -->
        </div>
        <div>
          <!-- {{alert.content}} -->
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
        alert: 'error/errorMessage'
      })
    },
    methods: {
      ...mapActions({
            closeAlert: 'error/clearError'
        })
    }
}
</script>

<style>

</style>