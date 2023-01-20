<script setup lang="ts">
    import { RouterLink } from 'vue-router';
</script>

<template>
    <div>
        <nav class="bg-indigo-500 text-white list-none p-3 flex justify-around font-semibold">
            <li class="hover:scale-110 duration-200 hover:text-gray-100 cursor-pointer"><RouterLink to="/"><font-awesome-icon icon="fa-solid fa-house-user" /></RouterLink></li>
            <li class="hover:scale-110 duration-200 hover:text-gray-100 cursor-pointer"><RouterLink to="/companies">Companies</RouterLink></li>
            <li class="hover:scale-110 duration-200 hover:text-gray-100 cursor-pointer"><RouterLink to="/my-account">MyAccount</RouterLink></li>
        </nav>
    </div>
</template>
