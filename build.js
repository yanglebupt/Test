// 配置指南：https://sky.sankuai.com/max/instruction/basic/config#buildjson
const { defineConfigForMaxAir } = require('@max/kit-lib-build-config-helper');

const targets = process.env.MAX_TARGET_ENV ? [process.env.MAX_TARGET_ENV] : ['mrn', 'web'];


// web端独立配置项
const webConf = targets.includes('web')
  ? {
    hash: 'contenthash',
  }
  : {};

const buildConf = defineConfigForMaxAir({
  targets,
  dslType: 'max', // mrn或max，默认max
  buildVersion: 'v2', // 默认v1，表示目前现有的构建类型，v2表示新的构建类型，在h5端，新的构建类型底层从rax-web切换成了rn-web，并且支持使用MRN的基础组件和API
  // 定义全局变量
  define: {
    owl: {
      // TODO:【必填】OWL和ELink初始化需要使用这个字段，用作业务方appKey，能在 SC 平台上查到
      catKey: '',
      // 【选填】web 侧 catKey，如果填了，web 侧将优先使用WebCatKey
      // WebCatKey: '',
    },
  },
  // 默认使用 webpack5 作为编译工具，或删除以下配置来使用webpack4
  compiler: 'webpack5',
  ...webConf,
});

console.log('当前构建配置，注意配置中的TODO，部分需要手动填写：', buildConf);

module.exports = buildConf;
