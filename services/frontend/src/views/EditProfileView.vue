<template>
  <div id="edit-profile">
      <Navbar />
      <EditProfileForm />
  </div>
</template>

<script>
import EditProfileForm from "@/components/profile/EditProfileForm.vue"
import Navbar from "@/components/Navbar.vue"

export default {
    name: "EditProfile",
    components: {
        EditProfileForm,
        Navbar
    }
}
</script>

<style>

</style>