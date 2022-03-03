import axios from "axios";
import base from './base';

export default {
    getProfileByPublicName(publicName) {
        return axios.get(`${base.apiUrl}/profile/${publicName}`)
    },
}