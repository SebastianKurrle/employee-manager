<script setup lang="ts">
    import { ref, onMounted } from 'vue';
    import { useCompanyStore } from '@/stores/company';
    import axios from 'axios';

    // stores
    const companyStore = useCompanyStore()

    const totalCosts = ref(0)

    // gets the total costs
    const getCompanyTotalCosts = ():void => {
        axios
            .get(`/api/company/${companyStore.company.id}/costs/`)
            .then(response => {
                totalCosts.value = response.data.totalCosts
            })
            .catch(error => {
                console.log(error);
            })
    }

    getCompanyTotalCosts()
</script>

<template>
    <!-- Modal -->
    <div class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
        id="totalCostsModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog relative w-auto pointer-events-none">
            <div
                class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current">
                <div
                    class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md">
                    <h5 class="text-xl font-medium leading-normal text-gray-800" id="exampleModalLabel">Total costs for {{ companyStore.company.name }}</h5>
                    <button type="button"
                        class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
                        data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body relative p-4 text-gray-800">
                    <p class="font-semibold mb-2">Total costs: {{ totalCosts }} €</p>

                    <p>This value represents the total costs for employees on {{ companyStore.company.name }}</p>
                </div>
                <div
                    class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-gray-200 rounded-b-md">
                    <button type="button" class="px-6
        py-2.5
        bg-red-800
        text-white
        font-medium
        text-xs
        leading-tight
        uppercase
        rounded
        shadow-md
        hover:bg-red-700 hover:shadow-lg
        focus:bg-red-700 focus:shadow-lg focus:outline-none focus:ring-0
        transition
        duration-150
        ease-in-out" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>