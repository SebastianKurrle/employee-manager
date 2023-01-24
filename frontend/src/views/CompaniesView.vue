<script setup lang="ts">
    import { RouterLink } from 'vue-router';
</script>

<template>
    <div>
        <h1 class="text-lg text-center font-semibold">My Companies</h1>

        <RouterLink to="/company/create">
            <div class="absolute top-20 right-5 bg-green-600 p-3 w-20 text-center rounded-full hover:scale-110 duration-200 cursor-pointer">
                <font-awesome-icon icon="fa-solid fa-plus" /> Add
            </div>
        </RouterLink>
    </div>
</template>