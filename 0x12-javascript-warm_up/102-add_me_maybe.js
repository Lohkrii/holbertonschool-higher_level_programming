#!/usr/bin/nodejs
exports.addMeMaybe = function (moby, whale) {
  return whale(moby++);
};
