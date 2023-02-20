<script setup lang="ts">
    import { ref, reactive, onMounted } from 'vue'
    import { useCompanyStore } from '@/stores/company';
    import { useLoaderStore } from '@/stores/loader';
    import { useFilterEmployeeStore } from '@/stores/filterEmployee';
    import axios from 'axios';
    import router from '@/router';

    //components
    import AddButton from '@/components/AddButton.vue'
    import BackButton from '@/components/BackButton.vue';
    import EmployeeCard from '@/components/EmployeeCard.vue';
    import SerachEmployee from '@/components/SerachEmployee.vue';

    //stores
    const companyStore = useCompanyStore()
    const loaderStore = useLoaderStore()
    const filterEmployeeStore = useFilterEmployeeStore()

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
            filterEmployeeStore.clearFilter()
        }
    })
</script>

<template>
    <div>
        <h1 class="text-lg text-center font-semibold">Manage Employees</h1>
        <AddButton url="/employee/create"/>

        <div class="flex justify-center md:justify-start">
            <button class="bg-blue-800 p-3 mt-3 rounded-md hover:bg-blue-600" data-bs-toggle="modal" data-bs-target="#filterEmployeesModal">Filter Employees</button>
        </div>
        <SerachEmployee />

        <div v-if="filterEmployeeStore.isFiltert">
            <h5 class="text-lg text-center font-semibold">Filter results</h5>

            <div class="flex justify-center mt-3 mb-3">
                <div class="grid lg:grid-cols-3 md:grid-cols-2 gap-2">
                    <EmployeeCard v-for="emp in filterEmployeeStore.filtertEmployees" :employee="emp" :key="Number(emp.id)"/>
                </div>
            </div>
        </div>

        <div class="flex justify-center mt-3" v-else>
            <div class="grid lg:grid-cols-3 md:grid-cols-2 gap-2">
                <EmployeeCard v-for="emp in employees" :employee="emp" :key="Number(emp.id)"/>
            </div>
        </div>

        <BackButton :url="companyStore.company.get_absolute_url"/>
    </div>
</template>

<style scoped>
</style>