<template>
  <Card>
      <template #title>
          Register
      </template>
      <template #content>
        <label for="username">Username</label>
        <InputText id="username" type="text" v-model="userIn.username" />
        
        <label for="password">Password</label>
        <Password id="password" v-model="userIn.password" toggleMask/>
      </template>
      <template #footer></template>
  </Card>
</template>

<script>
export default {

}
</script>

<style>

</style>