<template>
  <div class="home">
    <Navbar />
    <h3>Home View</h3>
    <Ping />
  </div>
</template>

<script>
// @ is an alias to /src
import Ping from "@/components/Ping.vue"
import Navbar from "@/components/Navbar.vue"

export default {
  name: 'HomeView',
  components: {
    Ping,
    Navbar
  }
}
</script>
