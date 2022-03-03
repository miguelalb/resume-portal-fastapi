import axios from "axios";
import { apiUrl } from './base';

export const apiPing = {
    pingBackend() {
        return axios.get(`${apiUrl}/ping`)
    }
}