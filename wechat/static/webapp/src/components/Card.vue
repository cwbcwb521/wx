<!-- Card -->
<template>
  <div class="card">
    <md-card class="card-box">
      <!-- header -->
      <md-card-header class="card-header">
        <md-avatar>
          <img src="../assets/avatar/testpic画板 1.png" alt="tester" />
        </md-avatar>
        <md-card-header-text class="card-header-text">
          <div class="md-title">cwbcwb521</div>
          <div class="md-subhead">东京</div>
        </md-card-header-text>

        <md-menu md-size="auto" md-direction="bottom-start" md-align-trigger>
          <md-button class="md-icon-button" md-menu-trigger>
            <md-icon>more_vert</md-icon>
          </md-button>
          <md-menu-content>
            <md-menu-item>
              <span>复制链接</span>
            </md-menu-item>

            <md-menu-item>
              <span>举报</span>
            </md-menu-item>

            <md-menu-item>
              <span>取消</span>
            </md-menu-item>
          </md-menu-content>
        </md-menu>
      </md-card-header>
      <!-- content -->
      <md-card-content class="text-wrapper">{{txt_content}}</md-card-content>
      <!-- action -->
      <md-card-actions md-alignment="left" class="card-action">
        <md-button class="md-icon-button">
          <md-icon>favorite_border</md-icon>
        </md-button>

        <md-button class="md-icon-button">
          <md-icon>message</md-icon>
        </md-button>

        <md-button class="md-icon-button">
          <md-icon>share</md-icon>
        </md-button>
      </md-card-actions>
      <!-- like -->
      <Like></Like>
      <!-- comment -->
      <Comment></Comment>
    </md-card>
  </div>
</template>

<script>
//这里可以导入其他文件（比如：组件，工具js，第三方插件js，json文件，图片文件等等）
//例如：import 《组件名称》 from '《组件路径》';
import Like from "./widgets/Like";
import Comment from "./widgets/Comment";

export default {
  //import引入的组件需要注入到对象中才能使用
  components: {
    Like,
    Comment
  },
  data() {
    //这里存放数据
    return {
      txt_content: ""
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
  mounted() {
    this.txt_content =
      "1.发现喜欢的人好像永远不会喜欢自己\n" +
      "2.体重秤上越来越上涨的数字\n" +
      "3.想吃的那家外卖今日休息\n" +
      "4.看中的鞋子卖光了自己的尺码\n" +
      "5.银行卡的余额越来越少\n" +
      "6.钥匙在家，被锁在门外，只能等待开锁师傅\n" +
      "7.几个人一起走，蹲下来系鞋带，没有人等\n" +
      "8.情敌好像要比自己优秀\n";
  },
  beforeCreate() {}, //生命周期 - 创建之前
  beforeMount() {}, //生命周期 - 挂载之前
  beforeUpdate() {}, //生命周期 - 更新之前
  updated() {}, //生命周期 - 更新之后
  beforeDestroy() {}, //生命周期 - 销毁之前
  destroyed() {}, //生命周期 - 销毁完成
  activated() {} //如果页面有keep-alive缓存功能，这个函数会触发
};
</script>
<style lang="scss" scoped>
.card {
  margin-top: 3rem;
  display: flex;
  justify-content: center;
}

.card-box {
  width: 60rem;
}

.card-header {
  border-bottom: 1px solid #ccc;
  padding: 10px !important;
  height: 5rem;
}
.card-header-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
}

.md-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-top: -0.1rem !important;
}
.md-subhead {
  font-size: 0.8rem;
  margin-top: -0.5rem !important;
}
.text-wrapper {
  white-space: pre-wrap;
  padding: 1.5rem 3rem 1.5rem 3rem;
  font-size: 1.8rem;
  line-height: 150%;
  border-bottom: 1px solid #ccc;
}
.card-action {
  margin-left: 0.8rem;
}
.md-icon {
  color: #000 !important;
}
</style>