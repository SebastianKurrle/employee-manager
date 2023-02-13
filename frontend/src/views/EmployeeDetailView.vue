<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { useCompanyStore } from '@/stores/company';
    import { useLoaderStore } from '@/stores/loader';
    import axios from 'axios';
    import router from '@/router';

    //components
    import EmployeDetailTable from '@/components/EmployeeDetailTable.vue'
    import BackButton from '@/components/BackButton.vue';

    // interfaces
    interface Employee {
        first_name:string,
        last_name:string,
        department:string,
        birthday:string,
        salary_per_hour:number,
        hours_per_week:number,
        get_absolute_salary:string,
        get_image:string,
        company:number
    }

    //stores
    const companyStore = useCompanyStore()
    const loaderStore = useLoaderStore()

    const emp:Employee = Object()
    const employee = ref(emp)

    // toggler if the data is loaded to show the table
    const loaded = ref(false)

    const getEmployee = async () => {
        const empId = router.currentRoute.value.params.empId
        const compId = companyStore.company.id

        loaderStore.setIsLoading()

        await axios
            .get(`/api/employee/${compId}/${empId}/`)
            .then(response => {
                employee.value = response.data
            })
            .catch(error => {
                console.log(error)
            })
        
        loaded.value = true
        loaderStore.setIsLoading()
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
        <h1 class="text-lg text-center font-semibold">Employee Detail</h1>

        <div class="bg-gray-800 p-3 rounded-md mt-3 text-white">
            <div class="flex justify-center mb-3">
                <div class="img">
                    <img :src="employee.get_image" class="circle w-full h-full object-cover"/>
                </div>
            </div>

            <h5 class="text-lg font-semibold text-center">Employee Data <font-awesome-icon icon="fa-solid fa-circle-info" /></h5>
            <EmployeDetailTable :employee="employee" v-if="loaded"/>
        </div>

        <BackButton :url="`${companyStore.company.get_absolute_url}/manage-employees`"/>
    </div>
</template>

<style scoped>

.circle {
    border-radius: 100%;
}

.img {
    width: 70px;
    height: 70px;
    background: #e8e8e8;
    border-radius: 100%;
    margin: auto;
    margin-top: 20px;
}
</style>