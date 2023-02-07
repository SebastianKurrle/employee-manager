<script setup lang="ts">
    import { RouterLink } from 'vue-router';

    const props = defineProps(['url'])
</script>

<template>
    <RouterLink :to="props.url">
        <div class="absolute top-20 right-5 bg-green-600 p-3 z-10 w-20 text-center rounded-full hover:scale-110 duration-200 cursor-pointer">
            <font-awesome-icon icon="fa-solid fa-plus" /> Add
        </div>
    </RouterLink>
</template>

<style scoped>
</style>