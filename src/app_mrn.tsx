import { AppRegistry, Text, TextInput } from '@mrn/react-native';
import App from './pages/Home/index';

// 设置Text字体不随系统字体大小改变
try {
  // @ts-ignore
  Text.defaultProps = Text.defaultProps || {};
  // @ts-ignore
  Text.defaultProps.allowFontScaling = false;
} catch (error) {
  console.log(error);
}

// 设置TextInput字体不随系统字体大小改变
try {
  // @ts-ignore
  TextInput.defaultProps = TextInput.defaultProps || {};
  // @ts-ignore
  TextInput.defaultProps.allowFontScaling = false;
} catch (error) {
  console.log(error);
}

// 这里注册的 'max_test-max' 可以是全公司不冲突的任意名字
AppRegistry.registerComponent('max_test-max', () => App);
