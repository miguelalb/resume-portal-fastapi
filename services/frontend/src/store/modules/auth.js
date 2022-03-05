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
            localStorage.removeItem('token');
            context.commit('clearLogin');
            if (err.response.status === 403 || err.response.status === 401) {
                context.commit('error/setError', {
                    title: 'Invalid Credentials',
                    content: err.response.data.detail
                }, {root: true});
            } else {
                console.log(err);
            }
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
            context.commit('error/setError', {
                title: 'Something went wrong!',
                content: err.response.data.detail
            }, {root: true});
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