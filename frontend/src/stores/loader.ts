import { defineStore } from "pinia";
import { ref } from 'vue'

export const useLoaderStore = defineStore('loader', () => {
    const isLoading = ref(false)

    // sets the loading status
    const setIsLoading = () => {
        isLoading.value = !isLoading.value
    }

    return {isLoading, setIsLoading}
})
