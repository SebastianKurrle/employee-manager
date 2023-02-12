import { defineStore } from "pinia";
import { ref } from 'vue'

export const useAuthenitacedStore = defineStore('authenticated', () => {
    let authenticated = ref(false)
    let token = ref('')

    const setAuthenticated = () => {
        // sets the authtenicate variable to true if an token exists
        if (localStorage.getItem('token')) {
            authenticated.value = true
            token.value = String(localStorage.getItem('token'))
        } else {
            token.value = ''
            authenticated.value = false
        }
    }

    // logsout the user
    const logout = () => {
        authenticated.value = false
        localStorage.removeItem('token')
        localStorage.removeItem('username')
        localStorage.removeItem('company')
    }

    return {authenticated, token, setAuthenticated, logout}
})
