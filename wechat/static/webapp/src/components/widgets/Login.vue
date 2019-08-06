<!--  -->
<template>
  <div class="login">
    <md-dialog
      :md-active.sync="dlg_status"
      :md-close-on-esc="false"
      :md-click-outside-to-close="false"
      class="lgi-dlg"
    >
      <md-dialog-title>登录</md-dialog-title>
      <div class="lgi-ipt">
        <md-field class="lgi-account" :md-counter="false">
          <label>账号</label>
          <md-input :maxlength="30"></md-input>
        </md-field>
        <md-field class="lgi-pwd" :md-counter="false">
          <label>密码</label>
          <md-input type="password" :maxlength="30"></md-input>
        </md-field>
        <div class="lgi-register">还没有账号？立即注册</div>
        <div class="lgi-btn">
          <md-button class="md-raised lgi-login">登录</md-button>
          <md-button class="md-raised lgi-cancel" @click="dlg_status = false">取消</md-button>
        </div>
      </div>
    </md-dialog>
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
      dlg_status: false
    };
  },
  props: {
    hasUserInfo: {
      type: Boolean
    },
    dlgStatusChange:{
      type: Boolean
    }
  },
  //监听属性 类似于data概念
  computed: {},
  //监控data中的数据变化
  watch: {
    dlgStatusChange: function() {
      this.dlg_status = true;
    }
  },
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
.lgi-dlg {
  width: 40rem;
  height: 40rem;
}
.lgi-ipt {
  margin: 2rem 0 1rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.lgi-account,
.lgi-pwd {
  width: 80%;
}
.lgi-register {
  align-self: flex-end;
  margin-right: 4rem;
  text-decoration: underline;
}
.lgi-btn {
  margin: 10rem 0 1rem 0;
}
.lgi-login,
.lgi-cancel {
  width: 15rem;
}
</style>