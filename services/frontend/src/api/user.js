import axios from "axios";
import { apiUrl, authHeaders } from './base';

export const apiUser = {
    async getUserMe(token) {
        const config = authHeaders(token);
        return axios.get(`${apiUrl}/users/me`, config)
    },
    async updateUser(user, token) {
        const config = authHeaders(token);
        return axios.put(`${apiUrl}/users`, user, config)
    }
}