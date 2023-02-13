<script setup lang="ts">
    import { ref, reactive } from 'vue'
    import { useAuthenitacedStore } from '@/stores/authenticated';
    import axios from 'axios';
    import router from '@/router';
    import type { RouteLocationRaw, RouterLink } from 'vue-router';

    // Vars for sign in
    const username = ref('')
    const password = ref('')

    const errors = reactive(Array())

    const authenticatedStore = useAuthenitacedStore()

    const signIn = () => {
        const formData:object = {
            username: username.value,
            password: password.value
        }

        axios
            .post('/api/user/login/', formData)
            .then(response => {
                const token = response.data.token

                axios.defaults.headers.common['Authorization'] = 'Token ' + token 

                localStorage.setItem('token', token)
                localStorage.setItem('username', response.data.user_info.username)

                authenticatedStore.setAuthenticated()

                // gets the path for the router
                const toPath:RouteLocationRaw = String(router.currentRoute.value.query.to || '/')
                router.push(toPath)
            })
            .catch(error => {
                if (error.response) {
                    // Loops the server errors and push it in the errors array
                    for (const property in error.response.data) {
                        errors.push(
                            `${property}: ${error.response.data[property]}`
                        );
                    }
                }
            })
        
        username.value = ''
        password.value = ''
    }

</script>

<template>
    <div>
        <h4 class="text-lg text-center font-semibold">Sign In</h4>

        <div class="flex justify-center mt-3">
            <div>
                <form @submit.prevent="signIn">
                    <input type="text" class="input w-96 mb-3" required placeholder="Username" v-model="username"/>
                    <br/>
                    <input type="password" class="input w-96 mb-3" required placeholder="Password" v-model="password"/>
                    <br/>

                    <div class="bg-red-500 text-white rounded p-3 mb-3" v-if="errors.length">
                        <p v-for="error in errors">{{ error }}</p>
                    </div>

                    <button class="bg-green-600 rounded-lg p-3 w-96 hover:scale-110 duration-200 mb-2">Sign In</button> <br/>

                    Need an account? <RouterLink to="/sign-up" class="text-blue-700 underline">Sing Up</RouterLink>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
@import '@/assets/style/input.css';
</style>
