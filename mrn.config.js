// mrn.config.js 配置文档
// http://mrn.sankuai.com/docs/guide/conf.html#mrn-config-js

let iconfont;
try {
  iconfont = require('@max/leez-icon/font.js').fonts;
} catch (e) {
  console.error('fail load @max/leez-icon iconfont');
}

module.exports = {
  name: 'max-test-max',
  fonts: {
    ...iconfont, // 新增的icon
  },
  main: 'src/app_mrn.tsx',
  biz: 'travel',
  bundleType: 1,
  bundleDependencies: ['@mrn/mrn-base'],
  debugger: {
    moduleName: 'max_test-max',
    initialProperties: {
      hideNavigationBar: true,
    },
  },
};
