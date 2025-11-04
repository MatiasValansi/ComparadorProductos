//Creo este componente solo para testear que funciona correcatemente la API de MercadoLibre

import { useState } from 'react'
import { fetchMercadoLibre } from '../api/mercadoLibre.js'

export default function TestMercadoLibre() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)

  const handleSearch = async () => {
    setLoading(true)
    const data = await fetchMercadoLibre(query)
    setResults(data)
    setLoading(false)
  }

  return (
    <div style={{ padding: '20px' }}>
      <h2>Buscar en Mercado Libre</h2>

      <input
        type="text"
        placeholder="Ej: notebook"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Buscar</button>

      {loading && <p>Cargando...</p>}

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {results.map((item) => (
          <li key={item.id} style={{ marginBottom: '15px' }}>
            <img src={item.thumbnail} alt={item.title} width="50" />
            <a href={item.link} target="_blank" rel="noopener noreferrer">
              {item.title}
            </a>
            <p>💲{item.price}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}
