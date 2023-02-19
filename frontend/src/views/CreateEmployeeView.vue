<script setup lang="ts">
    import { ref, reactive } from 'vue';
    import { useCompanyStore } from '@/stores/company';
    import axios from 'axios';

    // components
    import BackButton from '@/components/BackButton.vue';

    // stores
    const companyStore = useCompanyStore()

    interface Employee {
        first_name:string,
        last_name:string,
        department:string,
        birthday:string,
        salary_per_hour:number,
        hours_per_week:number,
        image:object,
        company:number
    }


    // vars for the form
    const firstname = ref('')
    const lastname = ref('')
    const departemnt = ref('')
    const salaryPerHour = ref(0)
    const hoursPerWeek = ref(0)
    const birthday = ref('')
    const image = ref({})

    const errors = reactive(Array())

    const setImage = (event:any) => {
        if (event.target.files.length > 0) {
            image.value = event.target.files[0]
        } else {
            image.value = ''
        }
    }

    const formatDate = (date:Date) => {
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();

        return `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`;
    }

    const createEmployee = () => {
        errors.length = 0

        const employee:Employee = {
            first_name:firstname.value,
            last_name:lastname.value,
            department:departemnt.value,
            salary_per_hour:salaryPerHour.value,
            hours_per_week:hoursPerWeek.value,
            birthday:formatDate(new Date(birthday.value)),
            image:image.value,
            company:companyStore.company.id
        }

        axios
            .post('/api/employee/', employee, {
                headers: {
                    "Content-Type": "multipart/form-data",
                }
            })
            .then(response => {
                
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
        
        firstname.value = ''
        lastname.value = ''
        departemnt.value = '',
        salaryPerHour.value = 0,
        hoursPerWeek.value = 0,
        birthday.value = '',
        image.value = ''
    }

</script>

<template>
    <div>
        <h5 class="text-lg font-semibold text-center">Create Employee</h5>

        <div class="flex justify-center border p-3 mt-3 rounded-md">
            <div>
                <form @submit.prevent="createEmployee" enctype="multipart/form-data" method="POST">   	
                    <input type="text" class="input w-96 mb-3" required placeholder="Firstname *" v-model="firstname"/> <br/>
                    <input type="text" class="input w-96 mb-3" required placeholder="Lastname *" v-model="lastname"/> <br/>
                    <input type="text" class="input w-96 mb-3" required placeholder="Department *" v-model="departemnt"/> <br/>
                    <input type="number" class="input w-96 mb-3" required placeholder="Salary per hour * " v-model="salaryPerHour"/> <br/>
                    <input type="number" class="input w-96 mb-3" required placeholder="Hours per week *" v-model="hoursPerWeek"/>
                    
                    <div class="mb-3">
                        <label class="font-semibold">Birthday *</label> <br/>
                        <input type="date" class="w-96 rounded-md bg-gray-700" v-model="birthday">
                    </div>
                    
                    <label class="block mb-2 text-md font-medium text-white dark:text-white" for="file_input">Image</label>
                    <input @change="setImage" class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" type="file">
                    
                    <div class="bg-red-500 text-white rounded p-3 mb-3" v-if="errors.length">
                        <p v-for="error in errors">{{ error }}</p>
                    </div>

                    <button class="bg-green-500 p-3 rounded-md w-full mt-3"><font-awesome-icon icon="fa-solid fa-plus" /> Add</button>
                </form>
            </div>
        </div>

        <BackButton :url="`${companyStore.company.get_absolute_url}/manage-employees`"/>
    </div>
</template>

<style scoped>
@import '@/assets/style/input.css';
</style>