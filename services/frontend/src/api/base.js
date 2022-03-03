
const apiUrl = process.env.VUE_APP_AXIOS_DEFAULT_URL;

function authHeaders(token) {
    return {
        headers: {
            token: `${token}`
        }
    }
}

export default {
    apiUrl,
    authHeaders
}