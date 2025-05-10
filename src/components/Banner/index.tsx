/* eslint-disable no-console */
import { createElement, PureComponent } from '@max/max';
import Text from '@hfe/max-text';

// 这里仅作为一种可用写法的展示，相比这种，更推荐使用 CSS Modules 写法
// 即 import styles from './index.module.scss'，然后使用 className={styles.banner} 引用
// 参见 https://sky.sankuai.com/max/instruction/basic/style
import './index.scss';

interface Props {
  uri: string;
}

interface State {
  name: string;
  age: number;
}

export default class Banner extends PureComponent<Props, State> {
  constructor(props: Readonly<Props>) {
    super(props);
    this.state = { name: 'Max 官网', age: 0 };
  }

  componentDidMount() {
    console.log('Banner componentDidMount');
  }

  componentWillUnmount() {
    console.log('Banner componentWillUnmount');
  }

  componentDidCatch(error: Error, errorInfo: Max.ErrorInfo) {
    console.log('Banner componentDidCatch', error, errorInfo);
  }

  getSnapshotBeforeUpdate(prevProps: Readonly<Props>, prevState: Readonly<State>): any | null {
    console.log('Banner getSnapshotBeforeUpdate', prevProps, prevState);
    return null;
  }

  componentDidUpdate(prevProps: Readonly<Props>, prevState: Readonly<State>, snapshot?: any) {
    console.log('Banner componentDidUpdate', prevProps, prevState, snapshot);
  }

  updateName = () => {
    this.setState((prevState) => {
      const nameNew = prevState.name === 'Max 官网' ? 'MAX 官网' : 'Max 官网';
      const ageNew = prevState.age + 1;
      return {
        name: nameNew,
        age: ageNew,
      };
    });
  };

  render(): Max.MaxNode {
    console.log('Render Banner', this.state.name, this.state.age);
    const str = `${this.state.name}: ${this.props.uri}, age ${this.state.age}`;
    return (
      <Text className="banner" onClick={this.updateName}>
        {str}
      </Text>
    );
  }
}
