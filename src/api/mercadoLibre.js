import axios from "axios";

const ML_BASE = "https://api.mercadolibre.com";
const SITE = import.meta.env.VITE_ML_SITE || "MLA";

/**
 * Normalized product shape:
 * {
 *  id: string,
 *  title: string,
 *  price: number,
 *  currency: string,
 *  image: string,
 *  link: string,
 *  source: 'mercadolibre'
 * }
 */

export async function fetchMercadoLibre(query, limit = 20) {
  if (!query) return { results: [] };

  const url = `${ML_BASE}/sites/${SITE}/search`;
  const { data } = await axios.get(url, { params: { q: query, limit } });

  // data.results -> array of items (ML response)
  const results = (data.results || []).map((item) => ({
    id: item.id,
    title: item.title,
    price: Number(item.price ?? 0),
    currency: item.currency_id || "ARS",
    image: (item.thumbnail || item.pictures?.[0]?.url) || "",
    link: item.permalink || `https://www.mercadolibre.com.ar/p/${item.id}`,
    source: "mercadolibre",
  }));

  return { original: data, results };
}