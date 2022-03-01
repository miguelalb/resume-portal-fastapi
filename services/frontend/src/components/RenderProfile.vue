<template>
  <div>
      <div v-html="content"></div>
  </div>
</template>

<script>
import api from "@/api.js"
import services from "@/services.js"

export default {
    name: "RenderTemplate",
    data() {
        return {
            content: ""
        }
    },
    mounted() {
        api.getProfileByPublicName("alberteinstein")
            .then(res => {
                const content = res.data.content;
                const decoded = services.base64Decode(content);
                this.content = decoded;
            }).catch(err => console.log(err));
    }
}
</script>
