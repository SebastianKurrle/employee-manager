<script setup lang="ts">
import { RouterView } from 'vue-router'
import { onBeforeMount } from 'vue';
import { useAuthenitacedStore } from './stores/authenticated';
import axios from 'axios';
import Navbar from './components/Navbar.vue';

const authenticatedStore = useAuthenitacedStore()

onBeforeMount(() => {
  authenticatedStore.setAuthenticated()
  const token = authenticatedStore.token

  if (token) {
    axios.defaults.headers.common['Authorization'] = 'Token ' + token
  } else {
    axios.defaults.headers.common['Authorization'] = ''
  }
})

</script>

<template>
  <div class="bg-gray-900 h-screen text-white">
    <header>
      <Navbar />
    </header>

    <main class="container max-w-7xl m-auto mt-3">
      <RouterView />
    </main>
  </div>
</template>

<style>
</style>
