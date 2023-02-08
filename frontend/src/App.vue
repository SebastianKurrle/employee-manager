<script setup lang="ts">
import { RouterView } from 'vue-router'
import { onBeforeMount, onMounted } from 'vue';
import { useAuthenitacedStore } from './stores/authenticated';
import { useCompanyStore } from './stores/company';
import axios from 'axios';
import Navbar from './components/Navbar.vue';
import Loader from './components/Loader.vue'

// stores
const authenticatedStore = useAuthenitacedStore()
const companyStore = useCompanyStore()

onBeforeMount(() => {
  authenticatedStore.setAuthenticated()
  const token = authenticatedStore.token

  if (token) {
    axios.defaults.headers.common['Authorization'] = 'Token ' + token
  } else {
    axios.defaults.headers.common['Authorization'] = ''
  }
})

onMounted(() => {
      const compObj = JSON.parse(String(localStorage.getItem('company')))
      companyStore.setCompany(compObj)
})

</script>

<template>
  <div class="bg-gray-900 h-screen text-white">
    <header>
      <Navbar />
    </header>
    <div class="flex justify-center mt-3">
      <Loader />
    </div>

    <main class="container max-w-7xl m-auto mt-3">
      <RouterView />
    </main>
  </div>
</template>

<style>
</style>
