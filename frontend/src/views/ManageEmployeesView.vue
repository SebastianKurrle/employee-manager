<script setup lang="ts">
    import { ref, reactive, onMounted } from 'vue'
    import { useCompanyStore } from '@/stores/company';
    import { useLoaderStore } from '@/stores/loader';
    import axios from 'axios';
    import router from '@/router';

    //components
    import AddButton from '@/components/AddButton.vue'
    import BackButton from '@/components/BackButton.vue';
    import EmployeeCard from '@/components/EmployeeCard.vue';

    //stores
    const companyStore = useCompanyStore()
    const loaderStore = useLoaderStore()

    // interfaces
    interface Employee {
        id: Number,
        firstName: String,
        lastName: String,
        birthday: String,
        department: String,
        salaryPerHour: Number,
        hoursPerWeek: Number,
        image: String,
        company: Number,
        getImage: String
    }

    const employees = reactive(Array<Employee>())

    const getEmployees = async () => {
        loaderStore.setIsLoading()

        await axios
                .get(`/api/employees/${companyStore.company.id}/`)
                .then(response => {
                    response.data.map((emp:Employee) => {
                        employees.push(emp)
                    })
                })
                .catch(error => {
                    console.log(error)
                })
        
        loaderStore.setIsLoading()
    }

    onMounted(() => {
        // checks if a copmany is selected
        if (companyStore.company.id === -1) {
            router.push('/companies')
        } else {
            getEmployees()
        }
    })
</script>

<template>
    <div>
        <h1 class="text-lg text-center font-semibold">Manage Employees</h1>
        <AddButton url="/employee/create"/>

        <div class="flex justify-center mt-3">
            <div class="grid lg:grid-cols-3 md:grid-cols-2 gap-2">
                <EmployeeCard v-for="emp in employees" :employee="emp" :key="Number(emp.id)"/>
            </div>
        </div>

        <BackButton :url="companyStore.company.get_absolute_url"/>
    </div>
</template>

<style scoped>
</style>