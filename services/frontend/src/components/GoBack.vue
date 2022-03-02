<template>
  <div class="goback">
      <div id="icon" @click="this.$router.go(-1)">
          <i class="fa-solid fa-arrow-left fa-xl" ></i>
      </div>
  </div>
</template>

<script>
export default {
    name: "Goback",
}
</script>

<style>
.goback {
    position: absolute;
    left: 0;
    padding: 1rem;
    cursor: pointer;
    z-index: 10;
}


</style>