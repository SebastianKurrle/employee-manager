import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Fontawsome
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import './assets/main.css'

import 'flowbite/dist/flowbite.min.js'
import 'flowbite/dist/datepicker.js'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

library.add(fas)

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(createPinia())
app.use(router)

app.mount('#app')
