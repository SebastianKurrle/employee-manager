<script setup lang="ts">
import { RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue';
</script>

<template>
  <div class="bg-gray-900 h-screen">
    <header>
      <Navbar />
    </header>

    <main>
      <RouterView />
    </main>
  </div>
</template>

<style>
</style>
