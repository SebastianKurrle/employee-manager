<script setup lang="ts">
    import { ref } from 'vue'

    const props = defineProps(['employee'])

    const employee = ref(props.employee)
</script>

<template>
    <table class="table-auto w-full text-center mt-3">
        <thead class="bg-gray-900 text-white">
          <tr>
            <th class="px-4 py-2">Fullname</th>
            <th class="px-4 py-2">Department</th>
            <th class="px-4 py-2">Birthday</th>
            <th class="px-4 py-2">Salary per hour</th>
            <th class="px-4 py-2">Hours per week</th>
            <th class="px-4 py-2">Absolute salary</th>
          </tr>
        </thead>
        <tbody>
          <tr class="">
            <td class="px-4 py-2">{{ `${employee.first_name} ${employee.last_name}` }}</td>
            <td class="px-4 py-2">{{ employee.department }}</td>
            <td class="px-4 py-2">{{ employee.birthday }}</td>
            <td class="px-4 py-2">{{ employee.salary_per_hour }} €</td>
            <td class="px-4 py-2">{{ employee.hours_per_week }}</td>
            <td class="px-4 py-2">{{ employee.get_absolute_salary }} €</td>
          </tr>
        </tbody>
    </table>      
</template>

<style scoped>
</style>