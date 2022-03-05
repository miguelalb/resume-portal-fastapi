<template>
    <Card class="mx-auto md:w-1/3 sm:w-1/2 text-center p-fluid">
        <template #title>
            Register
        </template>
        <template class="text-center" #content>
            <label for="username">Username</label>
            <span class="p-input-icon-left">
                <i class="pi pi-user" />
                <InputText id="username" type="text" v-model="userIn.username" />
            </span>
            
            <label for="password">Password</label>
            <Password id="password" v-model="userIn.password" toggleMask/>
            <div class="flex justify-center mt-1">
                <span class="text-sm">Already have an account with us? </span>
                <router-link :to="{'name': 'login'}" class="text-purple-600 text-sm font-semibold mx-1">Log In</router-link>
            </div>
        </template>
        <template #footer>
            <submit-button @clicked-submit="register(userIn)">Submit</submit-button>
        </template>
    </Card>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import SubmitButton from "@/components/utils/SubmitButton.vue"

export default {
    name: 'RegisterForm',
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
            register: 'auth/register'
        })
    }
}
</script>

<style scoped>

.p-card-content label {
    display: block;
    margin: 1em;
}
</style>