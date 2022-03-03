
const state = () => ({
    error: false,
    errorMessage: ''
})

const actions = {
    postError(context, errorMessage) {
        context.commit('setError', errorMessage);
    },
    clearError(context) {
        context.commit('clearError');
    }
}

const mutations = {
    setError(state, message) {
        state.error = true;
        state.errorMessage = message;
    },
    clearError(state) {
        state.error = false;
        state.message = '';
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