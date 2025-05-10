import { createElement, useState, useCallback, memo, useMemo, useEffect } from '@max/max';
import View from '@hfe/max-view';
import Text from '@hfe/max-text';
import Logo from '../../components/Logo';
import Banner from '../../components/Banner';
// Leez接入： https://km.sankuai.com/collabpage/1744524702
import TopViewProvider from '@max/leez-top-view-provider';
import ToastManager from '@max/leez-toast-manager';
import DialogManager from '@max/leez-dialog-manager';
import LoadingManager from '@max/leez-loading-manager';
// import { hotelTheme, ticketTheme } from '@max/leez-theme-hotel';
// import { setCustomTheme } from '@max/leez-context';

import styles from './index.module.scss';
import { request } from '@max/meituan-uni-network';

function Home() {
  //  新增，设置主题(餐和综可省略这一步)
  useMemo(() => {
    // 使用 useMemo 可保证只执行一次，且在 mount 之前执行
    // 酒店业务：打开下面注释，设置成酒店的主题
    // setCustomTheme(hotelTheme);
    // 门票业务：打开下面注释， 设置门票主题
    // setCustomTheme(ticketTheme);
  }, []);
  const [name, setName] = useState('my friend');
  const onClick = useCallback(() => {
    // 更新 state 触发重新渲染
    setName('world');
  }, []);

  useEffect(() => {
    // 新版网络请求（版本 >= 2.0.0），MRN和WEB端默认会接入ELink, 并开启上报开关。文档：https://km.sankuai.com/collabpage/2193577916
    // 注意：web端上报，需要在build.js的define字段中定义owl: {catKey: 'xxx'}
    request({
      url: 'https://yapi.sankuai.com/mock/14789/trip/list',
      method: 'GET',
      _meituan: {
        // MRN端可以在这关闭ELink 日志上报
        // enableElinkLog: false,
        mrnChannel: 'travel',
        requestType: 'MRNUtils',
      },
      _web: {
        // Web端可以在这关闭ELink 日志上报
        // enableElinkLog: false,
      },
    }).then((res) => {
      console.log('请求数据成功', res);
    }).catch((err) => {
      console.log('请求数据失败', err);
    });
  }, []);

  // eslint-disable-next-line no-console
  console.log('Render Home');
  // render 函数的 return 语句只能有一个，建议所有的 JSX 标签都放在 return 语句中
  return (
    <>
      {/* 新增(不涉及到modal等弹窗可不加) */}
      <TopViewProvider supportWeb>
        <View className={styles.container}>
          <Logo uri="https://p0.meituan.net/travelcube/389994cd21a0dd717894ec905467fb86141781.png" />
          <View className={styles.textContainer}>
            <Text className={styles.title}>Hello, {name}.</Text>
            {/* 事件传递，参数名就必须以 on 开头，如 onClick */}
            <Text className={styles.info} onClick={onClick}>
              Welcome to start your max journey.
            </Text>
          </View>
          <Banner uri={'https://sky.sankuai.com/max/instruction'} />
        </View>
      </TopViewProvider>
      {/* 新增(没使用toast可不加) */}
      <ToastManager />
      {/* 新增(没使用dialog可不加) */}
      <DialogManager />
      {/* 新增(没使用loading可不加) */}
      <LoadingManager />
    </>
  );
}

// 函数式组件每次调用都会刷新，使用 memo 包裹，当 props 没有变化时可以避免重复刷新
// Component 必须是 default 导出，一个文件只能存在一个 Component
export default memo(Home);
