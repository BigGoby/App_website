webpackJsonp([19],{"1DfJ":function(t,s){},oDx3:function(t,s,i){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var n=i("mvHQ"),o=i.n(n),a=i("8DN1"),e=i("mtWM"),r=i.n(e),c={name:"setting",components:{toast:a.a},methods:{handleLogout:function(){r.a.get("/user/logout/").then(this.handleLogoutSucc.bind(this))},handleLogoutSucc:function(t){if(1===t.data.data.start)try{window.localStorage.userInfo=o()({}),this.$refs.toast.toastShow("已退出登录"),this.$router.push("/login")}catch(t){console.log(t)}}}},l={render:function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"container"},[s("div",{staticClass:"header border-bottom"},[s("router-link",{staticClass:"back iconfont",attrs:{to:"/my"}},[this._v("")]),this._v("\n    设置\n  ")],1),this._v(" "),s("ul",{staticClass:"list"},[s("router-link",{staticClass:"item item-first border-bottom",attrs:{to:"/personalpage",tag:"li"}},[this._v("\n      编辑个人资料\n      "),s("span",{staticClass:"iconfont right-icon"},[this._v("")])]),this._v(" "),s("li",{staticClass:"bagcolor"}),this._v(" "),this._m(0),this._v(" "),this._m(1),this._v(" "),s("li",{staticClass:"bagcolor"}),this._v(" "),this._m(2),this._v(" "),this._m(3),this._v(" "),s("li",{staticClass:"btn-item",on:{click:this.handleLogout}},[this._v("退出登录")])],1),this._v(" "),s("toast",{ref:"toast"})],1)},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("li",{staticClass:"item item-first border-bottom"},[this._v("\n      账户绑定\n      "),s("span",{staticClass:"iconfont right-icon"},[this._v("")])])},function(){var t=this.$createElement,s=this._self._c||t;return s("li",{staticClass:"item item-first border-bottom"},[this._v("\n      消息设置\n      "),s("span",{staticClass:"iconfont right-icon"},[this._v("")])])},function(){var t=this.$createElement,s=this._self._c||t;return s("li",{staticClass:"item item-first border-bottom"},[this._v("\n      清除缓存\n      "),s("span",{staticClass:"iconfont right-icon"},[this._v("")])])},function(){var t=this.$createElement,s=this._self._c||t;return s("li",{staticClass:"item item-first border-bottom"},[this._v("\n      关于乐居\n      "),s("span",{staticClass:"iconfont right-icon"},[this._v("")])])}]},h=i("VU/8")(c,l,!1,function(t){i("1DfJ")},"data-v-3372a282",null);s.default=h.exports}});
//# sourceMappingURL=19.42fb9c7f4ee8c71a341f.js.map