import { defineStore } from "pinia";
import { ref } from "vue";

interface Company {
    id:Number,
    name:String,
    description:String,
    get_absolute_url:String
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