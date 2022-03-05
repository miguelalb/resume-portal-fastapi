
const state = () => ({
    error: false,
    errorMessage: {
        title: 'Default Title',
        content: 'Default content'
    }
})

const actions = {
    // TODO YAGNI?? Error handling is inside store
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