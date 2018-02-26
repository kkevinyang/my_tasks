import Vue from 'vue'
import Router from 'vue-router'
// import ElementUI from 'element-ui'
// import HelloWorld from '@/components/HelloWorld'
// import Home from '@/components/Home'

Vue.use(Router);

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'Home',
    //   component: Home
    // },
    {
      path: '/',
      redirect: '/task'
    },
    {
      path: '/task',
      component: resolve => require(['../components/common/Home.vue'], resolve),
      children:[
                {
                    path: '/',
                    component: resolve => require(['../components/page/task.vue'], resolve)
                },
                {
                    path: '/metric',
                    component: resolve => require(['../components/page/metric.vue'], resolve)
                },
        ]
    },
  ]
})
