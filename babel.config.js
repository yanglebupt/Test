const config = {};

if (process.env.MAX_PLATFORM === 'MRN') {
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  config.presets = ['@mrn/mrn-babel-preset', '@max/babel-preset-max2mrn'];
}

module.exports = config;
