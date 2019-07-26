<!--  -->
<template>
  <div class="navigation-bar">
    <div class="md-layout md-gutter">
      <div class="md-layout-item">
        <i class="material-icons md-36">home</i>
        <div class="split-line"></div>
        <span class="wb-name">一只小确丧</span>
      </div>
      <div class="md-layout-item"></div>
      <div class="md-layout-item">
        <i class="material-icons md-36">explore</i>
        <i class="material-icons md-36">favorite</i>
        <i class="material-icons md-40">person</i>
      </div>
    </div>
  </div>
</template>

<script>
//这里可以导入其他文件（比如：组件，工具js，第三方插件js，json文件，图片文件等等）
//例如：import 《组件名称》 from '《组件路径》';

export default {
  //import引入的组件需要注入到对象中才能使用
  components: {},
  data() {
    //这里存放数据
    return {};
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
.material-icons.md-36 {
  font-size: 3rem;
}
.material-icons.md-40 {
  font-size: 3.2rem;
}

.navigation-bar{
  border-bottom: 1px solid #ccc;
}
.md-layout-item {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
}
.md-layout-item i{
  margin-left: 1.5rem;
}
.wb-name {
  font-size: 2rem;
  font-weight: bold;
  font-family: serif;
}
.split-line {
    background-color: rgba(117, 111, 111, 0.527);
    width: 1px;
    height: 60%;
    margin: 0 1.5rem;
}
</style>