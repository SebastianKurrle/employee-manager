<script setup lang="ts">
    import { ref, reactive } from 'vue'
    import axios from 'axios';

    // for the company
    const compName = ref('')
    const compDesc = ref('')

    const errors = reactive(Array())

    // defines an company
    interface Company {
        name:String,
        description:String
    }

    const createCompany = ():void => {
        const comp:Company = {
            name: compName.value,
            description: compDesc.value
        }

        console.log(comp)

        axios
            .post('/api/company/create/', comp)
            .then(response => {
                console.log(response)
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
</script>

<template>
    <div>
        <h5 class="text-lg font-semibold text-center">Create Company</h5>

        <div class="flex justify-center border p-3 mt-3 rounded-md">
            <div>
                <form @submit.prevent="createCompany">
                    <input type="text" class="input w-96 mb-3" required placeholder="Company Name" v-model="compName"/> <br/>
                    <textarea class="input w-96 mb-3" cols="30" required rows="10" placeholder="Description" v-model="compDesc"></textarea> <br/>

                    <div class="bg-red-500 text-white rounded p-3 mb-3" v-if="errors.length">
                        <p v-for="error in errors">{{ error }}</p>
                    </div>

                    <button class="bg-green-500 p-3 rounded-md w-full"><font-awesome-icon icon="fa-solid fa-plus" /> Add</button>
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
