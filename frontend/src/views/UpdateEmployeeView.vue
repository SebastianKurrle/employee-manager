<script setup lang="ts">
    import { ref, reactive, onMounted } from 'vue'
    import { useCompanyStore } from '@/stores/company';
    import axios from 'axios';
    import router from '@/router';

    // interfaces
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

    //stores
    const companyStore = useCompanyStore()

    const employee = ref({})

    const firstname = ref('')
    const lastname = ref('')
    const departemnt = ref('')
    const salaryPerHour = ref(0)
    const hoursPerWeek = ref(0)
    const birthday = ref('')
    const image = ref({})
    const imageUrl = ref('')

    const errors = reactive(Array())

    // gets the employee from the backend
    const getEmployee = ():void => {
        const empId = router.currentRoute.value.params.empId
        const compId = companyStore.company.id

        axios
            .get(`/api/employee/${compId}/${empId}/`)
            .then(response => {
                employee.value = response.data

                initVars(employee.value)
            })
            .catch(error => {
                router.push('/not-found')
            })
    }

    // initialize the vars with the employee values
    const initVars = (employee:any) => {
        firstname.value = employee.first_name
        lastname.value = employee.last_name
        departemnt.value = employee.department,
        salaryPerHour.value = employee.salary_per_hour,
        hoursPerWeek.value = employee.hours_per_week,
        birthday.value = employee.birthday
        imageUrl.value = employee.get_image
        
        getImage(employee)
    }

    const setImage = (event:any) => {
        if (event.target.files.length > 0) {
            image.value = event.target.files[0]
        } else {
            image.value = ''
        }

        console.log(image.value)
    }

    const formatDate = (date:Date) => {
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();

        return `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`;
    }

    const getImage = (employee:any) => {
        axios
            .get(imageUrl.value, {
                responseType: 'blob'
            })
            .then(response => {
                image.value = new File([response.data], String(employee.image))
            })
    }

    // to update the employee
    const updateEmployee = () => {
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

        const empId = router.currentRoute.value.params.empId
        const compId = companyStore.company.id

        axios
            .put(`/api/employee/${compId}/${empId}/`, employee, {
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
    }

    onMounted(() => {
        // checks if a copmany is selected
        if (companyStore.company.id === -1) {
            router.push('/companies')
        } else {
            getEmployee()
        }
    })
</script>

<template>
    <div>
        <h1 class="text-lg text-center font-semibold">Update Employee</h1>

        <div class="flex justify-center border p-3 mt-3 rounded-md">
            <div>
                <form @submit.prevent="updateEmployee" enctype="multipart/form-data" method="POST">   	
                    <input type="text" class="input w-96 mb-3" required placeholder="Firstname *" v-model="firstname"/> <br/>
                    <input type="text" class="input w-96 mb-3" required placeholder="Lastname *" v-model="lastname"/> <br/>
                    <input type="text" class="input w-96 mb-3" required placeholder="Department *" v-model="departemnt"/> <br/>
                    <input type="number" class="input w-96 mb-3" required placeholder="Salary per hour * " v-model="salaryPerHour"/> <br/>
                    <input type="number" class="input w-96 mb-3" required placeholder="Hours per week *" v-model="hoursPerWeek"/>
                    
                    <div class="mb-3">
                        <label class="font-semibold">Birthday *</label> <br/>
                        <input type="date" class="w-96 rounded-md bg-gray-700" v-model="birthday">
                    </div>
                    
                    <p><span class="font-semibold">Current image:</span> {{ image }}</p>
                    <input @change="setImage" class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" type="file">
                    
                    <div class="bg-red-500 text-white rounded p-3 mb-3" v-if="errors.length">
                        <p v-for="error in errors">{{ error }}</p>
                    </div>

                    <button class="bg-green-500 p-3 rounded-md w-full mt-3"><font-awesome-icon icon="fa-solid fa-pen-to-square" /> Update</button>
                </form>
            </div>
        </div>
    </div>    
</template>

<style scoped>
@import '@/assets/style/input.css';
</style>