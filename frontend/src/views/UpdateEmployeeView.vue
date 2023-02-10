<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { useCompanyStore } from '@/stores/company';
    import axios from 'axios';
    import router from '@/router';

    //stores
    const companyStore = useCompanyStore()

    const employee = ref({})

    // gets the employee from the backend
    const getEmployee = ():void => {
        const empId = router.currentRoute.value.params.empId
        const compId = companyStore.company.id

        axios
            .get(`/api/employee/${compId}/${empId}/`)
            .then(response => {
                employee.value = response.data
            })
            .catch(error => {
                router.push('/not-found')
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
    </div>    
</template>

<style scoped>
</style>