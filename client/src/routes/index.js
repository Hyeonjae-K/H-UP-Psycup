import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/index',
    },
    {
      path: '/index',
      component: () => import ('@/views/IndexPage.vue'),
    },
    {
      name: 'detail',
      path: '/detail/:id',
      component: () => import('@/views/DetailPage.vue'),
    }
  ]
});

export default router;