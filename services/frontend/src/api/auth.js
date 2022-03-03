import axios from "axios";
import base from './base';

export default {
    logIn(username, password) {
        data = {
            username: username,
            password: password
        }
        return axios.post(`${base.apiUrl}/auth/login`, data)
    },
    register(username, password) {
        data = {
            username: username,
            password: password
        }
        return axios.post(`${base.apiUrl}/auth/register`, data)
    }
}