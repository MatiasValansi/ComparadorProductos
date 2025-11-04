import { useState } from "react";
import { searchMercadoLibre } from "../api/mercadoLibre.js";

export default function TestMercadoLibre() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setError(null);

    const data = await searchMercadoLibre(query);

    if (data && Array.isArray(data.results)) {
      setResults(data.results);
    } else {
      setResults([]);
      setError("No se encontraron resultados o hubo un error con la API.");
    }

    setLoading(false);
  };

  return (
    <div className="p-4 text-center">
      <h2 className="text-2xl font-bold mb-4">Búsqueda en Mercado Libre</h2>

      <div className="flex justify-center gap-2 mb-4">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Buscar producto..."
          className="border p-2 rounded"
        />
        <button
          onClick={handleSearch}
          className="bg-yellow-400 text-black font-bold px-4 py-2 rounded hover:bg-yellow-500"
        >
          Buscar
        </button>
      </div>

      {loading && <p>Cargando resultados...</p>}
      {error && <p className="text-red-500">{error}</p>}

      <ul className="grid grid-cols-2 md:grid-cols-3 gap-4 justify-center">
        {results.map((item) => (
          <li key={item.id} className="border p-2 rounded shadow">
            <img
              src={item.thumbnail || item.image}
              alt={item.title}
              className="mx-auto mb-2"
              width={120}
            />
            <p className="font-semibold">{item.title}</p>
            <p className="text-green-600">${item.price}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
