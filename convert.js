var readline = require("readline");
var fs = require("fs");

var ws = fs.createWriteStream(__dirname + "/imdb.tsv", {
  flags: "r+",
  defaultEncoding: "utf8"
});

var rl = readline.createInterface({
  input: fs.createReadStream(__dirname + "/imdb.csv")
});

ws.write(`Review\tType\n`);
rl.on("line", function(line) {
  let review = line.split("',");
  ws.write(`${review[0].substring(1)}\t${review[1]}\n`);
});

rl.on("close", function() {
  ws.close();
});
