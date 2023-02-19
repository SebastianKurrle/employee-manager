<script setup lang="ts">
    import { ref } from 'vue';
    import { useCompanyStore } from '@/stores/company';
    import { useFilterEmployeeStore } from '@/stores/filterEmployee';
    import axios from 'axios';

    // stores
    const companyStore = useCompanyStore()
    const filterEmployeeStore = useFilterEmployeeStore()

    const firstNameFilter = ref()
    const lastNameFilter = ref()
    const salaryPerHourFilter = ref()
    const hoursPerWeekFilter = ref()
    const departmentFilter = ref()

    const filterEmployees = () => {
        const filter:object = {
            first_name: firstNameFilter.value,
            last_name: lastNameFilter.value,
            hours_per_week: hoursPerWeekFilter.value,
            salary_per_hour: salaryPerHourFilter.value,
            department: departmentFilter.value
        }

        axios
            .post(`/api/employee/filter/${companyStore.company.id}/`, filter)
            .then(response => {
              filterEmployeeStore.setFiltertEmployees(response.data)
            })
            .catch(error => {
              console.log(error)
            })
    }
</script>

<template>
    <div class="mt-3">
        <div class="modal fade fixed top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto"
            id="filterEmployeesModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog relative w-auto pointer-events-none">
                <div
                    class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current">
                    <div
                        class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md">
                        <h5 class="text-xl font-medium leading-normal text-gray-800" id="exampleModalLabel">Filter employees</h5>
                        <button type="button"
                            class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
                            data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body relative p-4 text-gray-800">
                      <form @submit.prevent="filterEmployees">
                        <div class="mb-3 xl:w-96">
                            <label for="exampleFormControlInput1" class="form-label inline-block mb-2 text-gray-700"
                              >Firstname:</label
                            >
                            <input
                              v-model="firstNameFilter"
                              type="text"
                              class="
                                form-control
                                block
                                w-full
                                px-3
                                py-1.5
                                text-base
                                font-normal
                                text-gray-700
                                bg-white bg-clip-padding
                                border border-solid border-gray-300
                                rounded
                                transition
                                ease-in-out
                                m-0
                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
                              "
                            />
                        </div>

                          <div class="mb-3 xl:w-96">
                            <label for="exampleFormControlInput1" class="form-label inline-block mb-2 text-gray-700"
                              >Lastname:</label
                            >
                            <input
                              v-model="lastNameFilter"
                              type="text"
                              class="
                                form-control
                                block
                                w-full
                                px-3
                                py-1.5
                                text-base
                                font-normal
                                text-gray-700
                                bg-white bg-clip-padding
                                border border-solid border-gray-300
                                rounded
                                transition
                                ease-in-out
                                m-0
                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
                              "
                            />
                        </div>

                        <div class="mb-3 xl:w-96">
                            <label for="exampleFormControlInput1" class="form-label inline-block mb-2 text-gray-700"
                              >Salary per hour:</label
                            >
                            <input
                              v-model="salaryPerHourFilter"
                              type="number"
                              class="
                                form-control
                                block
                                w-full
                                px-3
                                py-1.5
                                text-base
                                font-normal
                                text-gray-700
                                bg-white bg-clip-padding
                                border border-solid border-gray-300
                                rounded
                                transition
                                ease-in-out
                                m-0
                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
                              "
                            />
                        </div>

                        <div class="mb-3 xl:w-96">
                            <label for="exampleFormControlInput1" class="form-label inline-block mb-2 text-gray-700"
                              >Hours per week:</label
                            >
                            <input
                              v-model="hoursPerWeekFilter"
                              type="number"
                              class="
                                form-control
                                block
                                w-full
                                px-3
                                py-1.5
                                text-base
                                font-normal
                                text-gray-700
                                bg-white bg-clip-padding
                                border border-solid border-gray-300
                                rounded
                                transition
                                ease-in-out
                                m-0
                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
                              "
                            />
                        </div>

                        <div class="mb-3 xl:w-96">
                            <label for="exampleFormControlInput1" class="form-label inline-block mb-2 text-gray-700"
                              >Department:</label
                            >
                            <input
                              v-model="departmentFilter"
                              type="text"
                              class="
                                form-control
                                block
                                w-full
                                px-3
                                py-1.5
                                text-base
                                font-normal
                                text-gray-700
                                bg-white bg-clip-padding
                                border border-solid border-gray-300
                                rounded
                                transition
                                ease-in-out
                                m-0
                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
                              "
                            />
                        </div>

                        <button class="bg-green-700 rounded-md p-3">Filter</button>
                      </form>
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
    </div>
</template>

<style>
</style>