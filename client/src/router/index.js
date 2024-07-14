import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import PartiesView from '../views/PartiesView.vue'

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
    }
  ]
})

export default router
