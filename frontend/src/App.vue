<script setup lang="ts">
import { RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue';
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
