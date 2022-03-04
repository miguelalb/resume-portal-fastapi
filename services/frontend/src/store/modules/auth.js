import { apiAuth } from "../../api/auth";

const state = {
    isLoggedIn: false,
    token: localStorage.getItem('token') || '',
}

const actions = {
    async login(context, user) {
        try {
            const response = await apiAuth.logIn(user.username, user.password);
            const data = response.data;
            if (data){
                localStorage.setItem('token', response.data.access_token);
                context.commit('setLogin');
            }
        } catch (err) {
            console.log(err);
            context.commit('clearLogin');
        }
    },
    logout(context) {
        localStorage.removeItem('token');
        context.commit('clearLogin');
    },
    async register(context, user) {
        try {
            const response = await apiAuth.register(user.username, user.password);
            context.dispatch('error/clearError');
        } catch (err) {
            console.log(err);
            context.dispatch('error/setError', err);
        }
    }
}

const mutations = {
    setLogin(state) {
        state.isLoggedIn = true;
    },
    clearLogin(state) {
        state.isLoggedIn = false;
    }
}

const getters = {}

export default {
    namespaced: true,
    state,
    actions,
    mutations,
    getters
}