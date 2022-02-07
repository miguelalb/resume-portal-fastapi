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
    pingBackend() {
        return axios.get(`${apiUrl}/ping`)
    },
    sanityCheck() {
        return axios.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    }
}