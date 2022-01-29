var axios = require("axios").default;

var options = {
  method: 'GET',
  url: 'https://justdial-jd-unofficial.p.rapidapi.com/search',
  params: {search_term: 'plumber', location: 'Kolkata', page_number: '1'},
  headers: {
    'x-rapidapi-host': 'justdial-jd-unofficial.p.rapidapi.com',
    'x-rapidapi-key': 'de80e4bc55msh646e07e0d6d3364p1daba0jsn6a650b1a16a4'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});