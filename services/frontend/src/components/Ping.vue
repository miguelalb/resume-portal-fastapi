<template>
  <div id="ping">
      <h3>Ping: {{ pong }}</h3>
      <h4>Environment: {{ environment }}</h4>
  </div>
</template>

<script>
import api from "../api";

export default {
    name: "Ping",
    data() {
        return {
            pong: null,
            environment: null
        }
    },
    mounted() {
        api.pingBackend()
        .then(res => {
        this.pong = res.data.ping;
        this.environment = res.data.environment;
        }).catch(err => console.log(err));
  }
}
</script>
