import { createRouter, createWebHistory } from 'vue-router'

// Router views
import HomeViewVue from '@/views/HomeView.vue'
import CompaniesView from '@/views/CompaniesView.vue'
import MyAccountView from '@/views/MyAccountView.vue'
import SignUpView from '@/views/SignUpView.vue'
import SignInViewVue from '@/views/SignInView.vue'
import { useAuthenitacedStore } from '@/stores/authenticated'

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
      component: CompaniesView,
      meta: {
        requireLogin: true
      },
    },

    {
      path: '/my-account',
      name: 'my-account',
      component: MyAccountView,
      meta: {
        requireLogin: true
      },
    }
  ]
})


router.beforeEach((to, from, next) => {
  const authenticatedStore = useAuthenitacedStore()

  if (to.matched.some(record => record.meta.requireLogin) && !authenticatedStore.authenticated) {
    next({name: 'sign-in', query: { to: to.path }})
  } else {
    next()
  }
})

export default router
