<template>
  <div class="goback">
      <div id="icon" @click="this.$router.go(-1)">
          <i class="fa-solid fa-arrow-left fa-xl" ></i>
      </div>
      <router-link id="home" :to="{'name': 'home'}"><i class="fa-solid fa-house-user fa-xl"></i></router-link>
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
    z-index: 10;
    display: flex;
}

#icon {
    cursor: pointer;
}

#home {
    margin: 0 1em;
    color: #2c3e50;
}

</style>