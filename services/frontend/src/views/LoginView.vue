<template>
  <div>
      <AlertBox />
      <LoginForm />
  </div>
</template>

<script>
import LoginForm from "@/components/auth/LoginForm.vue";
import AlertBox from "@/components/error/AlertBox";

export default {
    name: 'LoginView',
    components: {
        LoginForm,
        AlertBox
    }
}
</script>

<style>

</style>