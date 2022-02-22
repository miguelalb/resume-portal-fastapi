<template>
  <div id="editprofile">
      <PersonalInfo />
      <br>
      <Skills />
      <br>
      <Experience />
      <br>
      <Certification />
      <br>
      <Education />
  </div>
</template>

<script>
import PersonalInfo from "../components/profile/PersonalInfo.vue";
import Skills from "../components/profile/Skills.vue";
import Experience from "../components/profile/Experience.vue";
import Certification from "../components/profile/Certification.vue";
import Education from "../components/profile/Education.vue";

export default {
    name: "EditProfile",
    components: {
        PersonalInfo,
        Skills,
        Experience,
        Certification,
        Education,
    }
}
</script>

<style>

</style>