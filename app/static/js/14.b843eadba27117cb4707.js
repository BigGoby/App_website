webpackJsonp([14],{x0JW:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var i=s("mtWM"),e=s.n(i),n=s("GQaK"),c={name:"design",data:function(){return{listInfo:[]}},watch:{listInfo:function(){var t=this;this.BScroll&&this.$nextTick(function(){t.BScroll.refresh()})}},methods:{handleGetDataSucc:function(t){console.log(t),t.data&&(t=t.data),this.listInfo=t.data.findDesign},handleGetDataErr:function(){console.log("返回信息错误")}},mounted:function(){e.a.get("/design/").then(this.handleGetDataSucc.bind(this)).catch(this.handleGetDataErr),this.scroll=new n.a(this.$refs.wrapper)}},l={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",[s("div",{staticClass:"header border-bottom"},[s("router-link",{staticClass:"iconfont back",attrs:{to:"/index"}},[t._v("")]),t._v("\n    找设计\n  ")],1),t._v(" "),s("div",{ref:"wrapper",staticClass:"wrapper"},[s("div",{staticClass:"list"},t._l(t.listInfo,function(a){return s("div",{key:a.id,staticClass:"item"},[s("div",{staticClass:"img-con"},[s("img",{directives:[{name:"lazy",rawName:"v-lazy",value:a.imgUrl,expression:"item.imgUrl"}],staticClass:"img"})]),t._v(" "),s("div",{staticClass:"company"},[s("div",{staticClass:"title"},[t._v(t._s(a.title))]),t._v(" "),s("span",{staticClass:"name"},[t._v(t._s(a.company))]),t._v(" "),s("span",{staticClass:"city"},[t._v(t._s(a.address))]),t._v(" "),s("img",{staticClass:"headImg",attrs:{src:a.logo}})])])}))])])},staticRenderFns:[]},r=s("VU/8")(c,l,!1,function(t){s("zOLo")},"data-v-6aacb01e",null);a.default=r.exports},zOLo:function(t,a){}});
//# sourceMappingURL=14.b843eadba27117cb4707.js.map