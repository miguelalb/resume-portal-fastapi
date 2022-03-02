import axios from 'axios';

const apiUrl = process.env.VUE_APP_AXIOS_DEFAULT_URL;

function authHeaders(token) {
    return {
        headers: {
            Authorization: `Bearer ${token}`
        }
    }
}

export default {
    sanityCheck() {
        return axios.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    },
    pingBackend() {
        return axios.get(`${apiUrl}/ping`)
    },
    userLogin(username, password) {
        // TODO Make this more secure both front and backend
        return axios.post(`${apiUrl}/auth/login?username=${username}&password=${password}`)
    },
    getProfileByPublicName(publicName) {
        return axios.get(`${apiUrl}/profile/${publicName}`)
    },
    getAllTemplates() {
        return axios.get(`${apiUrl}/template`)
    }
}