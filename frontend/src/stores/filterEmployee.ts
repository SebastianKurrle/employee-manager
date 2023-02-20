import { defineStore } from "pinia";
import { ref, reactive } from "vue";

export const useFilterEmployeeStore = defineStore('filterEmployeeStore', () => {
    const filtertEmployees = reactive(Array())

    // to check if the user have filtert employees
    const isFiltert = ref(false)

    // sets the filtertEmployees to the filter result
    const setFiltertEmployees = (filtertEmps:any) => {
        filtertEmployees.length = 0
        filtertEmps.map((emp:object) => {
            filtertEmployees.push(emp)
        })

        isFiltert.value = true
    }

    const clearFilter = () => {
        filtertEmployees.length = 0
        isFiltert.value = false
    }

    return { filtertEmployees, isFiltert, setFiltertEmployees, clearFilter }
})
