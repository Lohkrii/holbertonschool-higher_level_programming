#!/usr/bin/nodejs
exports.callMeMoby = function (moby, whale) {
  for (let idx = 0; idx < moby; idx++) {
    whale();
  }
};
