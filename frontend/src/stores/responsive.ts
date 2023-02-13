import { defineStore } from "pinia";
import { ref } from 'vue'

export const useResponsiveStore = defineStore('responsive', () => {
    // to check if the mini menu is active or not
    const isToggeld = ref(false)

    // function to set the toggel ref
    const setIsToggeld = (toggeld:boolean) => {
        isToggeld.value = toggeld
    }

    return { isToggeld, setIsToggeld }
})
