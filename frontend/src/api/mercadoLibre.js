// src/api/mercadoLibre.js
import axios from 'axios';

export async function searchMercadoLibre(query) {
  const options = {
    method: 'GET',
    url: 'https://mercado-libre8.p.rapidapi.com/search',
    params: {
      keyword: query,   
      country: 'ar',
      page: '1'
    },
    headers: {
      'x-rapidapi-key': import.meta.env.X_RAPID_KEY_RAPID_API || '14b3c4584amshc969a09f0aaba19p1f0b6cjsnef9e38d2b7ec',
      'x-rapidapi-host': 'mercado-libre8.p.rapidapi.com'
    }
  };

  try {
    const response = await axios.request(options);
    console.log('Datos obtenidos:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error buscando en Mercado Libre:', error);
    return { results: [] };
  }
}
