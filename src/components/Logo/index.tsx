import { createElement, memo } from '@max/max';
import Image from '@hfe/max-image';

import styles from './index.module.scss';

interface LogoProps {
  uri: string;
}

function Logo(props: LogoProps) {
  const { uri } = props;
  const source = { uri };
  return <Image className={styles.logo} source={source} />;
}

export default memo(Logo);
