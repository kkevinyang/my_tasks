<template>
    <div class="sidebar">
        <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" theme="dark" unique-opened router>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index">
                        <template slot="title"><i :class="item.icon"></i>{{ item.title }}</template>
                        <el-menu-item v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">{{ subItem.title }}
                        </el-menu-item>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index">
                        <i :class="item.icon"></i>{{ item.title }}
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                items: [
                    {
                        icon: 'el-icon-star-off',
                        index: 'home',
                        title: '当前任务'
                    },
                    {
                        icon: 'el-icon-menu',
                        index: '2',
                        title: 'SQL',
                        subs: [
                            {
                                index: 'metric',
                                title: '指标SQL'
                            },
                            {
                                index: 'middle',
                                title: '中间表SQL'
                            }
                        ]
                    },
                    {
                        icon: 'el-icon-setting',
                        index: '3',
                        title: '其他设置',
                        subs: [
                            {
                                index: 'biz',
                                title: '业务线设置'
                            },
                            {
                                index: 'type',
                                title: '测试类型设置'
                            },
                        ]
                    },
                ]
            }
        },
        computed:{
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        }
    }
</script>

<style scoped>
    .sidebar{
        display: block;
        position: absolute;
        width: 250px;
        left: 0;
        top: 70px;
        bottom:0;
        background: #2E363F;
    }
    .sidebar > ul {
        height:100%;
    }
</style>
