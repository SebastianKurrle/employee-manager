<script setup lang="ts">
    import { RouterLink } from 'vue-router';
    import { useAuthenitacedStore } from '@/stores/authenticated';

    const authenticatedStore = useAuthenitacedStore()
</script>

<template>
    <div>
        <h1 class="text-3xl text-center font-bold">Employees Manager</h1>

        <div class="card mt-3">
            <h2>Welcome</h2>
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
    </div>
</template>

<style scoped>
.card {
    width: 100%;
    height: 254px;
    background: #07182E;
    position: relative;
    display: flex;
    place-content: center;
    place-items: center;
    overflow: hidden;
    border-radius: 20px;
  }
  
  .card h2 {
    z-index: 1;
    color: white;
    font-size: 2em;
  }
  
  .card::before {
    content: '';
    position: absolute;
    width: 100%;
    background-image: linear-gradient(180deg, rgb(0, 183, 255), rgb(255, 48, 255));
    height: 130%;
    animation: rotBGimg 3s linear infinite;
    transition: all 0.2s linear;
  }
  
  @keyframes rotBGimg {
    from {
      transform: rotate(0deg);
    }
  
    to {
      transform: rotate(360deg);
    }
  }
  
  .card::after {
    content: '';
    position: absolute;
    background: #0d3569;
    ;
    inset: 5px;
    border-radius: 15px;
  }

  .fancy {
    background-color: transparent;
    border: 2px solid #000;
    border-radius: 0;
    box-sizing: border-box;
    color: #fff;
    cursor: pointer;
    display: inline-block;
    font-weight: 700;
    letter-spacing: 0.05em;
    margin: 0;
    outline: none;
    overflow: visible;
    padding: 1.25em 2em;
    position: relative;
    text-align: center;
    text-decoration: none;
    text-transform: none;
    transition: all 0.3s ease-in-out;
    user-select: none;
    font-size: 13px;
   }
   
   .fancy::before {
    content: " ";
    width: 1.5625rem;
    height: 2px;
    background: black;
    top: 50%;
    left: 1.5em;
    position: absolute;
    transform: translateY(-50%);
    transform-origin: center;
    transition: background 0.3s linear, width 0.3s linear;
   }
   
   .fancy .text {
    font-size: 1.125em;
    line-height: 1.33333em;
    padding-left: 2em;
    display: block;
    text-align: left;
    transition: all 0.3s ease-in-out;
    text-transform: uppercase;
    text-decoration: none;
    color: black;
   }
   
   .fancy .top-key {
    height: 2px;
    width: 1.5625rem;
    top: -2px;
    left: 0.625rem;
    position: absolute;
    background: #e8e8e8;
    transition: width 0.5s ease-out, left 0.3s ease-out;
   }
   
   .fancy .bottom-key-1 {
    height: 2px;
    width: 1.5625rem;
    right: 1.875rem;
    bottom: -2px;
    position: absolute;
    background: #e8e8e8;
    transition: width 0.5s ease-out, right 0.3s ease-out;
   }
   
   .fancy .bottom-key-2 {
    height: 2px;
    width: 0.625rem;
    right: 0.625rem;
    bottom: -2px;
    position: absolute;
    background: #e8e8e8;
    transition: width 0.5s ease-out, right 0.3s ease-out;
   }
   
   .fancy:hover {
    color: white;
    background: black;
   }
   
   .fancy:hover::before {
    width: 0.9375rem;
    background: white;
   }
   
   .fancy:hover .text {
    color: white;
    padding-left: 1.5em;
   }
   
   .fancy:hover .top-key {
    left: -2px;
    width: 0px;
   }
   
   .fancy:hover .bottom-key-1,
    .fancy:hover .bottom-key-2 {
    right: 0;
    width: 0;
   }
</style>
