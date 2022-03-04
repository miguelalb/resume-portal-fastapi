
const state = () => ({
    error: false,
    errorMessage: {
        title: 'title',
        content: 'content'
    }
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
        state.errorMessage.title = message.title;
        state.errorMessage.content = message.content
    },
    clearError(state) {
        state.error = false;
        state.message.title = '';
        state.message.content = '';
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