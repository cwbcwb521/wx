<!--  -->
<template>
  <div class="register">
    <md-dialog
      :md-active.sync="dlg_status"
      :md-close-on-esc="false"
      :md-click-outside-to-close="false"
      :md-fullscreen="false"
      class="lgi-dlg"
    >
      <md-dialog-title>注册</md-dialog-title>
      <div class="lgi-ipt">
        <md-field class="lgi-account" :md-counter="false">
          <label>账号</label>
          <md-input :maxlength="30"></md-input>
        </md-field>
        <md-field class="lgi-pwd" :md-counter="false">
          <label>密码</label>
          <md-input type="password" :maxlength="30"></md-input>
        </md-field>
        <md-field class="lgi-pwd" :md-counter="false">
          <label>再次输入密码</label>
          <md-input type="password" :maxlength="30"></md-input>
        </md-field>
        <div class="lgi-register" @click="registeCancel(2)">已有账号，立即登录</div>
        <div class="lgi-btn">
          <md-button class="md-raised lgi-login">注册</md-button>
          <md-button class="md-raised lgi-cancel" @click="registeCancel(1)">取消</md-button>
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
    // 当前注册窗口打开状态
    registerStatus: {
      type: Boolean,
      default: false,
    },
  },
  //监听属性 类似于data概念
  computed: {},
  //监控data中的数据变化
  watch: {
    registerStatus: function() {
      this.dlg_status = this.registerStatus;
    }
  },
  //方法集合
  methods: {
    /**
     * @param type{number} 1:cancel/ 2:cancel&registe
     */
    registeCancel: function(type) {
      this.dlg_status = false;
      if (type === 1) {
        this.$emit("registeCancel", false);
      } else if (type === 2) {
        this.$emit("registeCancel", false, true);
      }
    }
  },
  //生命周期 - 创建完成（可以访问当前this实例）
  created() {},
  //生命周期 - 挂载完成（可以访问DOM元素）
  mounted() {
    this.registerStatus?this.dlg_status=true:this.dlg_status=false;
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
<style scoped>
.lgi-dlg {
  width: 40rem;
  /* height: auto; */
  overflow-y: scroll;
}
.lgi-ipt {
  margin: 1rem 0 1rem 0;
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
  margin: 6rem 0 1rem 0;
  display: flex;
  width: 80%;
}
.lgi-login,
.lgi-cancel {
  width: 50%;
}
</style>