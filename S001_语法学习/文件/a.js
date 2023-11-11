const fs = require('fs')

let content = fs.readFileSync('a.txt', {encoding: 'utf8'})
console.log(content)

