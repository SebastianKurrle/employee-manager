<script setup lang="ts">
    import { ref, reactive } from 'vue'
    import { RouterLink } from 'vue-router';
    import axios from 'axios';
    import router from '@/router';

    // Vars for sign up
    const username = ref('')
    const firstName = ref('')
    const lastName = ref('')
    const email = ref('')
    const password = ref('')
    const password2 = ref('')

    const errors = reactive(Array())

    const signUp = () => {
        errors.length = 0

        if (password.value != password2.value) {
            errors.push({passwords : 'The passwords are not equal'})
        } else {
            const formData:object = {
                username: username.value,
                first_name: firstName.value,
                last_name: lastName.value,
                email: email.value,
                password: password.value
            }

            axios
                .post('/api/user/register/', formData)
                .then(response => {
                    router.push('/sign-in')
                })
                .catch(error => {
                    console.log(error)

                    if (error.response) {
                        // Loops the server errors and push it in the errors array
                        for (const property in error.response.data) {
                            errors.push(
                                `${property}: ${error.response.data[property]}`
                            );
                        }
                    }
                })
        }

        username.value = ''
        firstName.value = ''
        lastName.value = ''
        email.value = ''
        password.value = ''
        password2.value = ''
    }
</script>

<template>
    <div>
        <h4 class="text-lg text-center font-semibold">Sign Up</h4>

        <div class="flex justify-center mt-3">
            <div>
                <form @submit.prevent="signUp">
                    <input type="text" required class="input w-96 mb-3" placeholder="username" v-model="username">
                    <br/>
                    <input type="text" required class="input w-96 mb-3" placeholder="first name" v-model="firstName">
                    <br/>
                    <input type="text" required class="input w-96 mb-3" placeholder="lastname" v-model="lastName">
                    <br/>
                    <input type="email" required class="input w-96 mb-3" placeholder="email" v-model="email">
                    <br/>
                    <input type="password" required class="input w-96 mb-3" placeholder="password" v-model="password">
                    <br/>
                    <input type="password" required class="input w-96 mb-3" placeholder="password again" v-model="password2">

                    <br/>

                    <div class="bg-red-500 text-white rounded p-3 mb-3" v-if="errors.length">
                        <p v-for="error in errors">{{ error }}</p>
                    </div>

                    <button class="bg-green-600 rounded-lg p-3 w-96 hover:scale-110 duration-200 mb-2">Sign Up</button> <br/>

                    Already have na account? <RouterLink to="/sign-in" class="text-blue-700 underline">Sing In</RouterLink>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .input {
        border: 2px solid #e8e8e8;
        padding: 15px;
        border-radius: 10px;
        background-color: #212121;
        font-size: small;
        font-weight: bold;
        text-align: center;
    }
   
   .input:focus {
    outline-color: white;
    background-color: #212121;
    color: #e8e8e8;
    box-shadow: 5px 5px #888888;
   }
</style>
