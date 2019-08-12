<!-- user -->
<template>
  <div class="user">
    <div class="user-info">
      <div class="user-pic">
        <md-avatar class="md-large">
          <img src="../assets/avatar/testpic1.png" alt="User" />
        </md-avatar>
      </div>
      <dir class="user-txt">
        <div class="user-name">
          cwbcwb521
          <i class="material-icons md-36">settings</i>
        </div>
        <div class="user-ff">
          <div class="user-follow">
            关注:
            <span>100</span>
          </div>
          <div class="user-fans">
            粉丝:
            <span>88</span>
          </div>
        </div>
        <div class="user-desc">follow me !</div>
      </dir>
    </div>
    <div class="user-tabs">
      <md-tabs md-alignment="centered">
        <md-tab id="tab-home" md-label="帖子">
          <Card :cardList="cardList" class="tab-card"></Card>
        </md-tab>
        <md-tab id="tab-pages" md-label="收藏">
          <Card :cardList="cardList" class="tab-card"></Card>
        </md-tab>
      </md-tabs>
    </div>
  </div>
</template>

<script>
//这里可以导入其他文件（比如：组件，工具js，第三方插件js，json文件，图片文件等等）
//例如：import 《组件名称》 from '《组件路径》';
import Card from "../components/Card";
export default {
  //import引入的组件需要注入到对象中才能使用
  components: {
    Card
  },
  data() {
    //这里存放数据
    return {
      cardList: [
        {
          id: 0
        },
        {
          id: 1
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
.user {
  margin-top: 4rem;
  padding: 2rem;
}
.user-info {
  display: flex;
  flex-direction: row;
  border-bottom: 1px solid #ccc;
}
.user-pic {
  width: 30%;
  display: flex;
}
.user-pic div {
  margin-right: 0;
}
.user-txt {
  width: 70%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  line-height: 180%;
}
.user-ff {
  display: flex;
  flex-direction: row;
}
.user-ff span {
  font-weight: bold;
}
.tab-card {
  margin-top: -3rem;
}
.md-tab {
  padding: 1px !important;
}
@media screen and (max-width: 600px) {
  .user {
    padding: 0.5rem;
  }
  .md-large {
    width: 5rem;
    height: 5rem;
  }
  .user-txt {
    padding-left: 2.5rem;
  }
  .user-fans {
    margin-left: 1rem;
  }
  .user-name {
    font-size: 2rem;
  }
  .user-name i {
    margin-left: 1rem;
    font-size: 1.6rem;
  }
  .user-desc {
    font-size: 1.4rem;
  }
  .user-ff {
    font-size: 1.4rem;
  }
}
@media screen and (min-width: 600px) {
  .user {
    padding: 2rem;
  }
  .md-large {
    width: 13rem;
    height: 13rem;
  }
  .user-txt {
    padding-left: 7rem;
  }
  .user-fans {
    margin-left: 3rem;
  }
  .user-name {
    font-size: 3rem;
  }
  .user-name i {
    margin-left: 2rem;
  }
  .user-desc {
    font-size: 1.6rem;
  }
  .user-ff {
    font-size: 1.4rem;
  }
}
</style>