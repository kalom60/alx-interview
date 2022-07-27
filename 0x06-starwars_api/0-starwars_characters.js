#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${url}/films/${process.argv[2]}/`, function (err, res, body) {
    if (err) {
      console.log(err);
    }
    const characters = JSON.parse(body).characters;
    const charsName = characters.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (proErr, proRes, proBody) => {
            if (proErr) {
              reject(proErr);
            }
            resolve(JSON.parse(proBody).name);
          });
        })
    );
    Promise.all(charsName)
      .then((names) => console.log(names.join('\n')))
      .catch((allErr) => console.log(allErr));
  });
}
