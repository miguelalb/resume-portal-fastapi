<template>
  <div id="profile">
      <RenderProfile :publicName="$route.params.public_name" />
  </div>
</template>

<script>
import RenderProfile from "../components/profile/ProfileRenderer.vue";

export default {
    name: "Profile",
    components: {
        RenderProfile
    },
}
</script>

<style>

</style>