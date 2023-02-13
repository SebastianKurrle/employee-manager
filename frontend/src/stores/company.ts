import { defineStore } from "pinia";
import { ref } from "vue";

interface Company {
    id:number,
    name:string,
    description:string,
    get_absolute_url:string
}

// defines the start company for no errors
const startComp:Company = {
    id: -1,
    name: '',
    description: '',
    get_absolute_url: ''
}

export const useCompanyStore = defineStore('company', () => {
    const company = ref(startComp)

    const setCompany = (comp:Company) => {
        company.value = comp
    }

    return { company, setCompany }
})