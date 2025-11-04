import axios from 'axios';

export async function fetchMercadoLibre(query) {
  if (!query) return [];
  const url = `https://api.mercadolibre.com/sites/MLA/search?q=${encodeURIComponent(query)}`;
  const { data } = await axios.get(url);
  return data.results.map(item => ({
    id: item.id,
    title: item.title,
    price: item.price,
    link: item.permalink,
    thumbnail: item.thumbnail,
    source: 'Mercado Libre'
  }));
}