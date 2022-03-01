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
    getProfileByPublicName(publicName) {
        return axios.get(`${apiUrl}/profile/${publicName}`)
    }
}