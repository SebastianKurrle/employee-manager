<script setup lang="ts">
    import { RouterLink } from 'vue-router';
    import { useResponsiveStore } from '@/stores/responsive';

    const props = defineProps(['url'])

    //stores
    const responsiveStore = useResponsiveStore()
</script>

<template>
    <RouterLink :to="props.url" v-if="!responsiveStore.isToggeld">
        <div class="absolute top-20 left-5 bg-red-800 p-3 z-10 w-20 text-center rounded-full hover:scale-110 duration-200 cursor-pointer">
            <font-awesome-icon icon="fa-solid fa-arrow-left" />
        </div>
    </RouterLink>
</template>

<script>
</script>