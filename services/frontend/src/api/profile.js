import axios from "axios";
import { apiUrl } from './base';

export const apiProfile = {
    getProfileByPublicName(publicName) {
        return axios.get(`${apiUrl}/profile/${publicName}`)
    },
}