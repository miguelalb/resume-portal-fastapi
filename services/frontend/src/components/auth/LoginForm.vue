<template>
    <Card class="mx-auto">
        <template #title>
            Log In
        </template>
        <template class="text-center" #content>
            <label for="username">Username</label>
            <InputText id="username" type="text" v-model="userIn.username" />
            
            <label for="password">Password</label>
            <Password id="password" v-model="userIn.password" toggleMask/>
        </template>
        <template #footer>
            <Button icon="pi pi-check" label="Submit" @click="loginUser"/>
        </template>
    </Card>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: 'LoginForm',
    data() {
        return {
            userIn: {
                username: '',
                password: ''
                }
        }
    },
    methods: {
        ...mapActions({
            login: 'auth/login'
        }),
        loginUser() {
            this.login(this.userIn);
        }
    }
}
</script>

<style scoped>
.p-card {
    /* margin: 3rem auto; */
    width: 50%;
}

.p-card-content label {
    display: block;
    margin: 1em;
}
</style>