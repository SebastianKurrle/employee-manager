<script setup lang="ts">
    import { RouterLink } from 'vue-router';
    import { ref } from 'vue'

    const props = defineProps(['employee'])

    const employee = ref(props.employee)
</script>

<template>
    <div>
        <div class="card rounded-md">
            <div class="card-border-top">
            </div>
            <div class="img">
                <img :src="employee.get_image">
            </div>
            <span> {{ `${employee.first_name} ${employee.last_name}` }}</span>
            <p class="job">{{ employee.department }}</p>
            <RouterLink class="link" :to="`/employee/${employee.id}/update`"><font-awesome-icon icon="fa-solid fa-pen-to-square" /></RouterLink>
            <RouterLink class="link" :to="`/employee/${employee.id}`" data-popover-target="empPop"><font-awesome-icon icon="fa-solid fa-circle-info" /></RouterLink>
        </div>
    </div>
</template>

<style scoped>
.card {
    width: 190px;
    height: 254px;
    background-image: linear-gradient(144deg,#8608b4, #492fed 60%,#bd6fda);
    border: none;
    position: relative;
    margin: auto;
    font-family: inherit;
    padding: 5px;
   }
   
   .card span {
    font-weight: 600;
    color: white;
    text-align: center;
    display: block;
    padding-top: 10px;
    font-size: 1.3em;
   }
   
   .card .job {
    font-weight: 400;
    color: white;
    display: block;
    text-align: center;
    padding-top: 5px;
    font-size: 1em;
   }
   
   .card .img {
    width: 70px;
    height: 70px;
    background: #e8e8e8;
    border-radius: 100%;
    margin: auto;
    margin-top: 20px;
   }
   
   .img img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 100%;
    }

   .link {
    padding: 8px 15px;
    display: block;
    margin: auto;
    border-radius: 8px;
    border: none;
    background: #e8e8e8;
    color: #111111;
    font-weight: 600;
    text-align: center;
    margin-bottom: 5px;
   }
   
   .link:hover {
    background: #212121;
    color: #ffffff;
   }
</style>