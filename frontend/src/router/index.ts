import { createRouter, createWebHistory } from 'vue-router'
import { useAuthenitacedStore } from '@/stores/authenticated'

// Router views
import HomeViewVue from '@/views/HomeView.vue'
import CompaniesView from '@/views/CompaniesView.vue'
import MyAccountView from '@/views/MyAccountView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInViewVue from '@/views/SignInView.vue'

const authenticatedStore = useAuthenitacedStore()

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
      path: '/sign-in',
      name: 'sign-in',
      component: SignInViewVue
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



router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !authenticatedStore.authenticated) {
    next({name: 'sign-in', query: { to: to.path }})
  } else {
    next()
  }
})

export default router
