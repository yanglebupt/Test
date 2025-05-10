
## Getting Started

### `mnpm run start`

Runs the app in development mode.

Open [http://localhost:3333](http://localhost:3333) to view it in the browser.

The page will reload if you make edits.
### `mnpm run build`

Builds the app for production to the `build` folder.

## 发布
- 页面工程请勿以「@max/max-app-template」名称在talos进行独立发布，可能会覆盖线上默认的模板。
- 可以接入FEDO进行发布，具体可以参考：[Max 接入SOP](https://km.sankuai.com/collabpage/1373627086)

## 文档
https://sky.sankuai.com/max/

## 其他说明
为满足方便Max构建基建的版本管理和node_modules体积优化的需求，我们将Max构建依赖拆分为以下几个包：

- @max/max-app@^1.1.1：构建工具主体，更新后build时若缺少相关构建插件会提示安装
- @max/build-mrn-dependencies@^1.0.3：MRN相关构建依赖，仅在需要构建MRN端产物时安装
- @max/build-web-dependencies@^1.0.0：Web端相关构建依赖，仅在需要构建Web端产物时安装
- @max/build-miniapp-dependencies@^1.0.0：小程序相关构建依赖，仅在需要构建小程序端产物时安装
- @max/build-plugin-max-component^2.0.0：组件构建插件，仅在需要构建组件产物时安装

可根据项目实际需要选择安装对应构建插件或剔除不需要的插件来减少依赖体积。
更细节的说明，请参考文档：https://km.sankuai.com/collabpage/1891880108

- 如果不需要构建小程序，包「@max/build-plugin-miniapp-publish」、「@max/eslint-plugin-max-compile-time-miniapp」和「@max/max-miniapp-build-error-helper-plugin」可以删除
- app.ts中的runApp若没有类型，请先运行yarn start:web
- 如果出现标签类型ts报错，可以尝试将编译器的ts版本设置为4.9.5并确保@types/react版本为17.0.30
- 如果MRN的二维码被遮挡，可以尝试独立启动「yarn start:mrn」，或者按【R】键刷新二维码。
- 建议使用pnpm7来运行项目，例如7.13.6。
