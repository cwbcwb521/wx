<!-- Comment -->
<template>
  <div class="comment">
    <ul class="cmt-list">
      <li v-for="item in cmtList" :key="item.id" class="cmt-item">
        <md-avatar class="md-small cmt-avatar">
          <img :src="item.avatar" alt="People" />
        </md-avatar>

        <div class="cmt-text">
          <span class="cmt-name">{{item.name}}</span>
          <span class="cmt-comment">{{item.comment}}</span>
        </div>

        <md-icon class="cmt-btn">favorite_border</md-icon>
      </li>

      <!-- <md-divider class="md-inset"></md-divider> -->
    </ul>
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
    return {
      cmtList: [
        {
          id: 0,
          avatar: "https://placeimg.com/40/40/people/1",
          name: "burger",
          comment: "来我这吃汉堡吧！"
        },
        {
          id: 1,
          avatar: "https://placeimg.com/40/40/people/2",
          name: "松屋",
          comment: "来我这牛肉盖饭吧！"
        }
      ]
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
<style scoped>
.cmt-list {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
}
.cmt-item {
  display: flex;
  align-items: center;
  width: 100%;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}
.cmt-avatar {
  margin: 1rem 0.8rem 1rem 2rem;
}
.cmt-text {
  margin-left: 1rem;
  display: flex;
  flex-direction: column;
}
.cmt-name {
  font-size: 1.4rem;
  font-weight: bold;
}
.cmt-comment {
  font-size: 0.8rem;
}
.cmt-btn {
  margin-right: 1.5rem;
  color: #ccc !important;
  font-size: 2rem !important;
}
</style>