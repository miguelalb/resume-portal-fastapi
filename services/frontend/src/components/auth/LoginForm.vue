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
            <submit-button @clicked-submit="loginUser">Submit</submit-button>
        </template>
    </Card>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import SubmitButton from "@/components/utils/SubmitButton.vue"

export default {
    name: 'LoginForm',
    components: {
        SubmitButton
    },
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
    width: 50%;
}

.p-card-content label {
    display: block;
    margin: 1em;
}
</style>