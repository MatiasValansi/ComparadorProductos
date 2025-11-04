import axios from "axios";

const API_URL = "https://mercado-libre8.p.rapidapi.com/search/";

const options = {
  headers: {
    "X-RapidAPI-Key": import.meta.env.VITE_X_RAPID_KEY_RAPID_API,
    "X-RapidAPI-Host": "mercado-libre8.p.rapidapi.com",
  },
};

export async function searchMercadoLibre(query) {
  try {
    const response = await axios.get(`${API_URL}${query}`, options);
    return response.data;
  } catch (error) {
    console.error("Error buscando en Mercado Libre:", error);
    return [];
  }
}
