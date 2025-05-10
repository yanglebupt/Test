declare module '*.module.scss' {
  const classes: { [key: string]: string };
  export default classes;
}
declare module '@max/max' {
  import * as Max from '@hfe/max-types';

  export = Max;
}
declare module '@hfe/max' {
  import * as Max from '@hfe/max-types';

  export = Max;
}