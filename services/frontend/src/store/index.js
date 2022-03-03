import { createStore } from 'vuex'
import auth from "./modules/auth"
import error from "./modules/error"
import user from "./modules/user"

export default createStore({
  modules: {
    auth,
    error,
    user
  }
})
