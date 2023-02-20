<script setup lang="ts">
    import { RouterLink } from 'vue-router';
    import { useAuthenitacedStore } from '@/stores/authenticated';

    const authenticatedStore = useAuthenitacedStore()
</script>

<template>
    <div>
        <h1 class="text-2xl text-center font-bold md:text-3xl">Employees Manager</h1>

        <div class="card mt-3">
            <h2 class="text-white text-2xl z-10 md:text-3xl">Welcome</h2>
        </div>

        <div class="mt-3" v-if="!authenticatedStore.authenticated">
            <RouterLink class="fancy" to="/sign-in">
                <span class="top-key"></span>
                <span class="text">Sign In</span>
                <span class="bottom-key-1"></span>
                <span class="bottom-key-2"></span>
            </RouterLink>
            <span class="mr-3"></span>
            <RouterLink class="fancy" to="/sign-up">
                <span class="top-key"></span>
                <span class="text">Sign Up</span>
                <span class="bottom-key-1"></span>
                <span class="bottom-key-2"></span>
            </RouterLink>
        </div>

        <div class="mt-3 p-3 rounded-md bg-gray-800" v-else>
          <h5 class="text-lg font-semibold text-center md:text-xl">Manage your employees easily</h5>

          <h6 class="text-md mb-2 md:text-lg mt-3"><font-awesome-icon icon="fa-solid fa-circle-info" /> Getting started</h6>
          <RouterLink to="/company/create" class="text-gray-400">1. Create Company</RouterLink>
          <br/>
          <RouterLink to="/companies" class="text-gray-400">2. Display my companies</RouterLink>
        </div>
    </div>
</template>

<style scoped>
  @import url('../assets/style/home.css');
</style>
