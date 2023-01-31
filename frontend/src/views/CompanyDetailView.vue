<script setup lang="ts">
    import { reactive, ref } from 'vue'
    import { useLoaderStore } from '@/stores/loader';
    import axios from 'axios';
    import router from '@/router';

    const loaderStore = useLoaderStore()

    interface Company {
        id:Number,
        name:String,
        description:String,
        get_absolute_url:String
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
            })
            .catch(error => {
                console.log(error)
            })
        
        loaderStore.setIsLoading()
    }

    getCompany()
</script>

<template>
    <div>
        <h1 class="text-lg text-center font-semibold">{{ company.name }}</h1>
    </div>
</template>

<style scoped>

</style>