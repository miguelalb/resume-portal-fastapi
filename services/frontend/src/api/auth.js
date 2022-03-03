import axios from "axios";
import { apiUrl } from './base';

export const apiAuth = {
    async logIn(username, password) {
        const data = {
            username: username,
            password: password
        }
        return axios.post(`${apiUrl}/auth/login`, data)
    },
    async register(username, password) {
        const data = {
            username: username,
            password: password
        }
        return axios.post(`${apiUrl}/auth/register`, data)
    }
}