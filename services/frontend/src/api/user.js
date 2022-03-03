import axios from "axios";
import base from './base';

export default {
    getUserMe(token) {
        config = base.authHeaders(token);
        return axios.get(`${base.apiUrl}/users/me`, config)
    },
    updateUser(user, token) {
        config = base.authHeaders(token);
        return axios.put(`${base.apiUrl}/users`, user, config)
    }
}