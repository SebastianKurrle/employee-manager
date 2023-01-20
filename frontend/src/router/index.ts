import { createRouter, createWebHistory } from 'vue-router'

// Router views
import HomeViewVue from '@/views/HomeView.vue'
import CompaniesView from '@/views/CompaniesView.vue'
import MyAccountView from '@/views/MyAccountView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeViewVue
    },
    {
      path: '/sign-up',
      name: 'sign-up',
      component: SignUpView
    },
    {
      path: '/companies',
      name: 'companies',
      component: CompaniesView
    },

    {
      path: '/my-account',
      name: 'my-account',
      component: MyAccountView
    }
  ]
})

export default router
