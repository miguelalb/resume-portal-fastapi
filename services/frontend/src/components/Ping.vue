<template>
  <div id="ping">
      <h3>Ping: {{ pong }} </h3>
      <h4>Environment: {{ environment }}</h4>
  </div>
</template>

<script>
import {apiPing} from "@/api/ping.js";

export default {
    name: "ping",
    data() {
        return {
            pong: null,
            environment: null
        }
    },
    mounted() {
        apiPing.pingBackend()
            .then(res => {
                this.pong = res.data.ping;
                this.environment = res.data.environment;
            }).catch(err => console.log(err));
    }
}
</script>

<style>

</style>