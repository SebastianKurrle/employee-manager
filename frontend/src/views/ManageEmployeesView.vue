<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { useCompanyStore } from '@/stores/company';

    //components
    import AddButton from '@/components/AddButton.vue'

    //stores
    const companyStore = useCompanyStore()
</script>

<template>
    <div>
        <h1 class="text-lg text-center font-semibold">Manage Employees</h1>
        <AddButton url="/employee/create"/>
    </div>
</template>

<style scoped>
</style>