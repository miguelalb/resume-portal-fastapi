
export const apiUrl = process.env.VUE_APP_AXIOS_DEFAULT_URL;

export function authHeaders(token) {
    return {
        headers: {
            token: `${token}`
        }
    }
}
