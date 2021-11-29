<!--  -->
<template>
  <div class="navigation-bar">
    <div class="nav-bar">
      <div class="md-layout md-gutter">
        <div class="md-layout-item nav-title">
          <router-link tag="i" class="material-icons md-36" to="/">home</router-link> 
          <div class="split-line md-xsmall-hide"></div>
          <span class="wb-name md-xsmall-hide">一只小确丧</span>
        </div>
        <div class="md-layout-item"></div>
        <div class="md-layout-item nav-action">
          <router-link tag="i" class="material-icons md-36" to="/jisuan">explore</router-link> 
          <i class="material-icons md-36">favorite</i>
          <i class="material-icons md-40" @click="btn_person" v-show="!hasUserInfo">person</i> 
          <router-link tag="i" class="material-icons md-40" to="/user"  v-show="hasUserInfo">person</router-link> 
        </div>
      </div>
    </div>
    <Login :loginStatus="loginStatus"
     @loginCancel="loginCancel"
     ></Login>
    <Register :registerStatus="registerStatus" @registeCancel="registeCancel"></Register>
  </div>
</template>

<script>
//这里可以导入其他文件（比如：组件，工具js，第三方插件js，json文件，图片文件等等）

import Login from "./widgets/Login"
import Register from "./widgets/Register"

export default {
  //import引入的组件需要注入到对象中才能使用
  components: {
    Login,
    Register
  },
  data() {
    //这里存放数据
    return {
      // 是否已经登录
      hasUserInfo : true,
      // 登录界面开关
      loginStatus: false,
      // 注册界面开关
      registerStatus:false,
    };
  },
  //监听属性 类似于data概念
  computed: {},
  //监控data中的数据变化
  watch: {},
  //方法集合
  methods: {
    /** 点击个人图标 */
    btn_person : function(){
      this.loginStatus = true;
    },
    /** 登录页面取消 */
    loginCancel:function(isCancel=false,isRegiste=false){
      this.loginStatus = isCancel;
      this.registerStatus = isRegiste;
    },
    /** 注册页面取消 */
    registeCancel:function(isCancel=false,isLogin=false){
      this.registerStatus = isCancel;
      this.loginStatus = isLogin;
    },
  },
  //生命周期 - 创建完成（可以访问当前this实例）
  created() {},
  //生命周期 - 挂载完成（可以访问DOM元素）
  mounted() {
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
<style lang='scss' scoped>
.nav-bar {
  position: fixed;
  top: 0;
  width: 100%;
  height: 4rem;
  z-index: 1000;
  border-bottom: 1px solid #ccc;
}

.material-icons.md-36 {
  font-size: 3rem;
}
.material-icons.md-40 {
  font-size: 3.2rem;
}

.md-layout-item {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
}
.nav-title{
  display: flex;
  justify-content: left;
}
.md-layout-item i {
  margin-left: 1.5rem;
}
.nav-action{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-right: 1rem;
}
.wb-name {
  font-size: 2rem;
  font-weight: bold;
  font-family: serif;
}
.split-line {
  background-color: #ccc;
  width: 1px;
  height: 60%;
  margin: 0 1.5rem;
}
.nav-bar::after{
  content: " ";
  background-color: #fff;
  position: fixed;
  top: 0;
  width: 100%;
  height: 4rem;
  z-index: -1;
  opacity: 0.9;
  filter: blur(5px)
}
</style>