<template>
  <div id="register-view" class="bg-slate-50 min-h-screen pt-24">
      <Transition name="slide-fade">
          <AlertBox v-if="this.$store.state.error.error" />
      </Transition>
      <RegisterForm />
  </div>
</template>

<script>
import RegisterForm from "@/components/auth/RegisterForm";

export default {
    name: 'RegisterView',
    components: {
        RegisterForm
    }
}
</script>

<style>

</style>