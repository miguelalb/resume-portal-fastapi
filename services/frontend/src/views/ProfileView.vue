<template>
  <div id="profile">
      <Goback />
      <RenderProfile />
  </div>
</template>

<script>
import RenderProfile from "@/components/RenderProfile.vue"
import Goback from "@/components/GoBack.vue"

export default {
    name: "Profile",
    components: {
        RenderProfile,
        Goback
    }
}
</script>

<style>

</style>