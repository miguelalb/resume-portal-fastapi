<template>
  <div>
      <h4>Username: </h4>
      <input type="text" v-model="userIn.username" placeholder="username">
      <h4>Password: </h4>
      <input type="password" v-model="userIn.password" placeholder="password" >
      <br>
      <br>
      <button @click="loginUser">Submit</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: 'LoginForm',
    data() {
        return {
            userIn: {
                username: '',
                password: ''
                }
        }
    },
    methods: {
        ...mapActions({
            login: 'auth/login'
        }),
        loginUser() {
            this.login(this.userIn);
        }
    }
}
</script>

<style>

</style>