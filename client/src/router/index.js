import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import PartiesView from '../views/PartiesView.vue'
import RegisterView from '../views/RegisterView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/parties',
      name: 'parties',
      component: PartiesView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    }
  ]
})

export default router
