<script setup lang="ts">
    import { ref } from 'vue'
    import { useLoaderStore } from '@/stores/loader';
    import { useCompanyStore } from '@/stores/company';
    import axios from 'axios';
    import router from '@/router';

    // components
    import DeleteCompanyConfrime from '@/components/DeleteCompanyConfrime.vue';

    // stores
    const loaderStore = useLoaderStore()
    const companyStore = useCompanyStore()

    interface Company {
        id:number,
        name:string,
        description:string,
        get_absolute_url:string
    }

    let startComp:Company = {
        id: -1,
        name: '',
        description: '',
        get_absolute_url: ''
    }

    const company = ref(startComp)

    // gets the company
    const getCompany = async () => {
        loaderStore.setIsLoading()
        const compSlug = router.currentRoute.value.params.slug

        await axios
            .get(`/api/company/get/${compSlug}/`)
            .then(response => {
                company.value = response.data
                companyStore.setCompany(company.value)
                localStorage.setItem('company', JSON.stringify(company.value))
            })
            .catch(error => {
                router.push('/not-found')
            })
        
        loaderStore.setIsLoading()
    }

    getCompany()
</script>

<template>
    <div>
        <h1 class="text-3xl text-center font-semibold">{{ company.name }}</h1>

        <div class="bg-gray-700 p-3 mt-3">
            <h4 class="text-lg text-center font-semibold">Overview</h4>
            
            <p><span class="font-semibold text-gray-300">Description:</span> <br/> {{ company.description }}</p>

            <h5 class="text-lg text-gray-300 font-semibold mt-3">Options:</h5>
            <br/>
            <div class="mb-3 flex flex-col gap-1 text-center">
                <RouterLink :to="String(company.get_absolute_url) + '/manage-employees'" class="bg-blue-800 text-white p-3 rounded-md hover:scale-105 duration-200">
                    Manage Employees <font-awesome-icon icon="fa-solid fa-people-roof" /></RouterLink>
                <DeleteCompanyConfrime />
            </div>
        </div>
    </div>
</template>

<style scoped>

</style>