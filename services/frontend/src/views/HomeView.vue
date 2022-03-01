<template>
  <div class="home">
    <h3>Home View</h3>
    <Ping />
  </div>
</template>

<script>
// @ is an alias to /src
import Ping from "@/components/Ping.vue"

export default {
  name: 'HomeView',
  components: {
    Ping
  }
}
</script>
