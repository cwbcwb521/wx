<!--  -->
<template>
  <div class="index">
    <NavigationBar></NavigationBar>
    <router-view></router-view>
    <div class="root">© 2019-2029 xiaoquesang.com 一只小确丧 版权所有 <a href="http://www.beian.miit.gov.cn">辽ICP备19011953号-1</a></div>
  </div>
</template>

<script>
//这里可以导入其他文件（比如：组件，工具js，第三方插件js，json文件，图片文件等等）
//例如：import 《组件名称》 from '《组件路径》';
import NavigationBar from "../components/NavigationBar";

export default {
  //import引入的组件需要注入到对象中才能使用
  components: {
    NavigationBar,
  },
  data() {
    //这里存放数据
    return {
    };
  },
  //监听属性 类似于data概念
  computed: {},
  //监控data中的数据变化
  watch: {},
  //方法集合
  methods: {},
  //生命周期 - 创建完成（可以访问当前this实例）
  created() {},
  //生命周期 - 挂载完成（可以访问DOM元素）
  mounted() {},
  beforeCreate() {}, //生命周期 - 创建之前
  beforeMount() {}, //生命周期 - 挂载之前
  beforeUpdate() {}, //生命周期 - 更新之前
  updated() {}, //生命周期 - 更新之后
  beforeDestroy() {}, //生命周期 - 销毁之前
  destroyed() {}, //生命周期 - 销毁完成
  activated() {} //如果页面有keep-alive缓存功能，这个函数会触发
};
</script>
<style lang='scss' scoped>
.root{
  display: flex;
  justify-content: center;
  margin-top: 30px;
}
.root a{
  margin-left: 10px;
}
</style>