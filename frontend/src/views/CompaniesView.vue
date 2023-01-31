<script setup lang="ts">
    import { RouterLink } from 'vue-router';
    import { reactive } from 'vue'
    import { useLoaderStore } from '@/stores/loader';
    import axios from 'axios';

    const loaderStore = useLoaderStore()

    // Datatype for the companies
    interface Company {
        id:Number,
        name:String,
        description:String,
        get_absolute_url:String
    }

    const companies = reactive(Array<Company>())

    const getCompanies = async () => {
        loaderStore.setIsLoading()

        // gets the companies from the user from the api
        await axios
            .get('/api/company/all/')
            .then(response => {
                // pushes the companies in the array
                response.data.map((comp:Company) => {
                    companies.push(comp)
                })
            })
            .catch(error => {
                console.log(error)
            })
        
        loaderStore.setIsLoading()
    }

    getCompanies()
</script>

<template>
    <div>
        <h1 class="text-lg text-center font-semibold">My Companies</h1>

        <RouterLink to="/company/create">
            <div class="absolute top-20 right-5 bg-green-600 p-3 w-20 text-center rounded-full hover:scale-110 duration-200 cursor-pointer">
                <font-awesome-icon icon="fa-solid fa-plus" /> Add
            </div>
        </RouterLink>

        <div class="flex justify-center mt-3">
            <div class="grid lg:grid-cols-3 md:grid-cols-2 gap-1">
                <div class="flip-card col-span-1" v-for="comp in companies" :key="Number(comp.id)">
                    <RouterLink :to="String(comp.get_absolute_url)">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                <p class="title">{{ comp.name }}</p>
                                <p>Hover Me</p>
                            </div>
                            <div class="flip-card-back">
                                <p class="font-bold text-lg">{{ comp.description }}</p>
                                <p class="text-gray-800 font-semibold">CLICK TO MANAGE</p>
                            </div>
                        </div>
                    </RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.flip-card {
    background-color: transparent;
    width: 190px;
    height: 254px;
    perspective: 1000px;
    font-family: sans-serif;
  }
  
  .title {
    font-size: 1.5em;
    font-weight: 900;
    text-align: center;
    margin: 0;
  }
  
  .flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s;
    transform-style: preserve-3d;
  }
  
  .flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
  }
  
  .flip-card-front, .flip-card-back {
    box-shadow: 0 8px 14px 0 rgba(0,0,0,0.2);
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border: 1px solid coral;
    border-radius: 1rem;
  }
  
  .flip-card-front {
    background: linear-gradient(120deg, bisque 60%, rgb(255, 231, 222) 88%,
       rgb(255, 211, 195) 40%, rgba(255, 127, 80, 0.603) 48%);
    color: coral;
  }
  
  .flip-card-back {
    background: linear-gradient(120deg, rgb(255, 174, 145) 30%, coral 88%,
       bisque 40%, rgb(255, 185, 160) 78%);
    color: white;
    transform: rotateY(180deg);
  }
</style>