import { defineStore } from "pinia";
import { ref } from 'vue'

export const useAuthenitacedStore = defineStore('authenticated', () => {
    let authenticated:boolean = false
    let token:String = ''

    const setAuthenticated = () => {
        // sets the authtenicate variable to true if an token exists
        if (localStorage.getItem('token')) {
            authenticated = true
            token = String(localStorage.getItem('token'))
        } else {
            token = ''
            authenticated = false
        }
    }

    // logsout the user
    const logout:object = () => {
        authenticated = false
        localStorage.removeItem('token')
    }

    return {authenticated, setAuthenticated, logout}
})
