import axios from "axios";
import base from './base';

export default {
    pingBackend() {
        return axios.get(`${base.apiUrl}/ping`)
    }
}