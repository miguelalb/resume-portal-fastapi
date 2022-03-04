<template>
  <nav class="text-center">
    <router-link :to="{'name': 'home'}">Home</router-link> |
    <router-link :to="{'name': 'editprofile'}"> Edit my Profile</router-link> |
    <router-link to="/profile/alberteinstein">Sample Resume</router-link> |
    <router-link :to="{'name': 'login'}">Log In</router-link>
  </nav>
</template>

<script>
export default {
    name: "Navbar"
}
</script>

<style>
nav {
  padding: 10px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>