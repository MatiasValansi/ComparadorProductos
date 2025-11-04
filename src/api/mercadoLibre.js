import axios from 'axios';

const options = {
  method: 'GET',
  url: 'https://mercado-libre8.p.rapidapi.com/search',
  params: {
    keyword: 'laptop',
    country: 'ar',
    page: '2',
    sort: 'price_low_to_high'
  },
  headers: {
    'x-rapidapi-key': '14b3c4584amshc969a09f0aaba19p1f0b6cjsnef9e38d2b7ec',
    'x-rapidapi-host': 'mercado-libre8.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}