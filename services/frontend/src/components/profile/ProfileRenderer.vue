<template>
  <div id="renderprofile">
      <h2>Render user profile component</h2>
      <h2>Public Name: {{publicName}}</h2>
  </div>
</template>

<script>
export default {
    props: {
        publicName: String
    },
    name: "RenderProfile",
    data() {
        return {

        }
    },
    methods: {

    }
}
</script>

<style>

</style>