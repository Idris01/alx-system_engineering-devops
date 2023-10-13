const request = require("request");
const options = {url:'https://www.reddit.com/api/me.json',headers: {'User-Agent':'refidas'}};
request(options, (err, resp, body) =>{
		if (!err) console.log(JSON.parse(body));
	});
