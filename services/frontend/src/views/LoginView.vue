<template>
  <div id="login-view" class="bg-slate-50 min-h-screen pt-24">
      <Transition name="slide-fade">
          <AlertBox v-if="this.$store.state.error.error" />
      </Transition>
      <LoginForm />
  </div>
</template>

<script>
import LoginForm from "@/components/auth/LoginForm.vue";

export default {
    name: 'LoginView',
    components: {
        LoginForm
    }
}
</script>

<style>

</style>