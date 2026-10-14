#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const count = data.results.filter((film) =>
      film.characters.some((character) => /\/18\/?$/.test(character))
    ).length;

    console.log(count);
  } catch (err) {
    console.log(err);
  }
});
