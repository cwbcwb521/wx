<!--  -->
<template>
  <div class="jisuan">
    <div class="text_input" >
        <span>房产总价：</span>
        <input type="text" name="price" value="7400000" id="price">
        <span>日元</span>
    </div>
    <div class="text_input" >
        <span>每月房租收入：</span>
        <input type="text" name="rent" value="57000" id="rent">
        <span>日元</span>
    </div>
    <div class="text_input" >
        <span>每月管理费：</span>
        <input type="text" name="kannrihi" value="9640" id="kannrihi">
        <span>日元</span>
    </div>
    <div class="text_input" >
        <span>每月修缮积立金：</span>
        <input type="text" name="shuuzenn" value="10000" id="shuuzenn">
        <span>日元</span>
    </div>
    <div class="text_input" >
        <input type="button" name="calculate" value="计算" id="cal" @click="jisuan()">
        <input type="button" name="qingkong" value="清空" id="clean" @click="qingkong()">
    </div>
    <div id="result" class="text_input" >

    </div>
  </div>
</template>

<script>
//这里可以导入其他文件（比如：组件，工具js，第三方插件js，json文件，图片文件等等）
//例如：import 《组件名称》 from '《组件路径》';

export default {
  //import引入的组件需要注入到对象中才能使用
  components: {
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
  methods: {
    qingkong : function(){
        var result = document.getElementById('result');
        //清除result中内容
        result.innerHTML = "";
        document.getElementById("price").value = "";
        document.getElementById("rent").value = "";
        document.getElementById("kannrihi").value = "";
        document.getElementById("shuuzenn").value = "";
    },
    jisuan : function(){

        var price = Number(document.getElementById("price").value);
        var rent = Number(document.getElementById("rent").value);
        var kannrihi = Number(document.getElementById("kannrihi").value);
        var shuuzenn = Number(document.getElementById("shuuzenn").value);
        var result = document.getElementById('result');

        //清除result中内容
        result.innerHTML = "";

        // 管理修缮总和
        var cost = kannrihi + shuuzenn;
        //一年房租减修善管理费,100%在租
        var rent_100 = (rent-cost-(rent*5/100))*12;
        //一年房租减修善管理费,95%在租
        var rent_95 = rent_100*0.95;
        //每年固定资产税,1%
        //assetsTax = price*1/100;
        var assetsTax = 30000;
        //一年利润
        var lirun = rent_100 - assetsTax;
        //总取得费用，房价，中介费，登记费，保险费，不动产取得税，8%
        var totalPrice = price*1.08;
        //实际回报(含初期)(95%租)，((房租-花费)/总费用)*100%
        var getRate_95 = ((rent_95-assetsTax)/totalPrice)*100;
        //实际回报(含初期)(满租)，((房租-花费)/总费用)*100%
        var getRate_100 = ((rent_100-assetsTax)/totalPrice)*100;
        //实际回报(不含初期)(95%租)，((房租-花费)/总费用)*100%
        var dreamRate_95 = ((rent_95-assetsTax)/price)*100;
        //实际回报(不含初期)(满租)，((房租-花费)/总费用)*100%
        var dreamRate_100 = ((rent_100-assetsTax)/price)*100;
        //表回（中介）
        var biaohui = (rent*12/price)*100;
        //实回（中介）
        var shihui = ((rent-cost)*12/price)*100;

        //添加计算结果div
        var shuoming_div = document.createElement('div');
        shuoming_div.id = 'shuoming_div';
        shuoming_div.innerText = '----------------------------------';
        result.appendChild(shuoming_div);

        var totalPrice_div = document.createElement('div');
        totalPrice_div.id = 'totalPrice_div';
        totalPrice_div.innerText = '房产取得总价: ' + totalPrice + '日元';
        result.appendChild(totalPrice_div);

        var lirun_div = document.createElement('div');
        lirun_div.id = 'lirun_div';
        lirun_div.innerText = '一年利润: ' + lirun + '日元';
        result.appendChild(lirun_div);

        var getRate_95_div = document.createElement('div');
        getRate_95_div.id = 'getRate_95_div';
        getRate_95_div.innerText = '实际回报率(含初期费用)(95%在租): ' + getRate_95 + '%';
        result.appendChild(getRate_95_div);

        var getRate_100_div = document.createElement('div');
        getRate_100_div.id = 'getRate_100_div';
        getRate_100_div.innerText = '实际回报率(含初期费用)(100%在租): ' + getRate_100 + '%';
        result.appendChild(getRate_100_div);

        var dreamRate_95_div = document.createElement('div');
        dreamRate_95_div.id = 'getRate_100_div';
        dreamRate_95_div.innerText = '实际回报率(不含初期费用)(95%在租): ' + dreamRate_95 + '%';
        result.appendChild(dreamRate_95_div);

        var dreamRate_100_div = document.createElement('div');
        dreamRate_100_div.id = 'getRate_100_div';
        dreamRate_100_div.innerText = '实际回报率(不含初期费用)(100%在租): ' + dreamRate_100 + '%';
        result.appendChild(dreamRate_100_div);

        var biaohui_div = document.createElement('div');
        biaohui_div.id = 'getRate_100_div';
        biaohui_div.innerText = '表回(中介): ' + biaohui + '%';
        result.appendChild(biaohui_div);

        var shihui_div = document.createElement('div');
        shihui_div.id = 'getRate_100_div';
        shihui_div.innerText = '实回(中介): ' + shihui + '%';
        result.appendChild(shihui_div);

    }
  },
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
    .jisuan{
        padding-top: 6rem;
    }
    .text_input{
        margin-left: 5rem;
        margin-top: 1.5rem;
    }
    #clean{
      margin-left: 2rem;
    }
</style>