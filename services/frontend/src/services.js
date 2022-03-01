
export default {
    base64Encode(content) {
        return window.btoa(content);
    },
    base64Decode(content) {
        return window.atob(content);
    }
}