<script setup lang="ts">
    import router from '@/router';
    import { useAuthenitacedStore } from '@/stores/authenticated';
    import axios from 'axios';

    const authenticatedStore = useAuthenitacedStore()

    const logout = () => {
        axios
            .post('/api/user/logout/')
            .then(response => {
                router.push('/sign-in')
            })
            .catch(error => {
                console.log(error)
            })

            axios.defaults.headers.common["Authorization"] = "";

            authenticatedStore.logout()
    }
</script>

<template>
    <div>
        <h1 class="text-lg font-semibold text-center">MyAccount</h1>

        <button class="bg-red-600 p-3 rounded-md w-40" @click="logout">Logout</button>
    </div>
</template>