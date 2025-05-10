const { getStylelintConfig } = require('@max/max-spec');

module.exports = getStylelintConfig('max', {
  extends: '@hfe/stylelint-config-max-rn',
  // custom config it will merge into main config
  rules: {},
});
