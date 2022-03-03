import { apiUser } from "../../api/user.js";

const state = () => ({
    user: null,
})

const actions = {
    async getMe(context) {
        try {
            token = context.rootState.auth.token;
            const response = await apiUser.getUserMe(token);
            if (response.data) {
                context.commit('setUser', response.data);
            }
        } catch (err) {
            console.log(err);
            context.commit('clearUser');
        }
    },
    async updateUserMe(context, user) {
        try {
            token = context.rootState.auth.token;
            const response = await apiUser.updateUser(user, token);
        } catch (err) {
            console.log(err);
        }
    }
}

const mutations = {
    setUser(state, user) {
        state.user = user;
    },
    clearUser(state) {
        state.user = null;
    }
}

const getters = {}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}