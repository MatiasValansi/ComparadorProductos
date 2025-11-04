import { useState } from "react";
import { searchMercadoLibre } from "../api/mercadoLibreApi";

export default function TestMercadoLibre() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const data = await searchMercadoLibre(query);
    setResults(data.results || []);
  };

  return (
    <div className="p-4">
      <h2>Búsqueda en Mercado Libre</h2>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Buscar producto..."
      />
      <button onClick={handleSearch}>Buscar</button>

      <ul>
        {results.map((item) => (
          <li key={item.id}>
            <img src={item.thumbnail} alt={item.title} width={50} />
            {item.title} - ${item.price}
          </li>
        ))}
      </ul>
    </div>
  );
}
