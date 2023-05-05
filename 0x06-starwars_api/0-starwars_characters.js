#!/usr/bin/node
// This scripts prints all characters of a Star Wars Movie Using the `star wars api`

const request = require('request');
const MovieID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${MovieID}`;
request.get(url, function (err, response, body) {
  if (err) { console.log(err); } else { body = JSON.parse(body); }
  const characters = body.characters;
  getCharacters(characters, 0, characters.length);
});

function getCharacters (characters, idx, max) {
  if (!characters || idx === max) { return; }

  request.get(characters[idx], function (err, response, body) {
    if (err) { console.log(err); } else { body = JSON.parse(body); }
    console.log(body.name);
    idx++;
    getCharacters(characters, idx, max);
  });
}
