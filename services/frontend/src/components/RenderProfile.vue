<template>
  <div id="renderer">
      <div v-html="content"></div>
      <div v-if="notFound">
          <h4>Profile not found.</h4>
          <h4>Please check the public name provided.</h4>
      </div>
  </div>
</template>

<script>
import api from "@/api.js"
import services from "@/services.js"

export default {
    name: "RenderTemplate",
    data() {
        return {
            content: "",
            notFound: false
        }
    },
    mounted() {
        api.getProfileByPublicName(this.$route.params.public_name)
            .then(res => {
                this.notFound = false;
                const content = res.data.content;
                const decoded = services.base64Decode(content);
                this.content = decoded;
            }).catch(err => {
                if (err.response)
                    if (err.response.status === 404)
                        this.notFound = true;
                else console.log(err);
            });
    }
}
</script>

<style scoped>
#renderer{
    position: absolute;
    left: 0;
    right: 0;
    padding: 0 1rem;
}
</style>
