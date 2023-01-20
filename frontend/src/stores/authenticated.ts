import { defineStore } from "pinia";
import { ref } from 'vue'

export const useAuthenitacedStore = defineStore('authenticated', () => {
    let authenticated = ref(false)
    let token:String = ''

    const setAuthenticated = () => {
        // sets the authtenicate variable to true if an token exists
        if (localStorage.getItem('token')) {
            authenticated.value = true
            token = String(localStorage.getItem('token'))
        } else {
            token = ''
            authenticated.value = false
        }
    }

    // logsout the user
    const logout:object = () => {
        authenticated.value = false
        localStorage.removeItem('token')
        localStorage.removeItem('username')
    }

    return {authenticated, token, setAuthenticated, logout}
})
