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
    <ul style={{ listStyle: 'none', padding: 0 }}>
  {Array.isArray(results) && results.length > 0 ? (
    results.map((item) => (
      <li key={item.id} style={{ marginBottom: '15px' }}>
        <img src={item.thumbnail} alt={item.title} width="50" />
        <a href={item.permalink} target="_blank" rel="noopener noreferrer">
          {item.title}
        </a>
        <p>💲{item.price}</p>
      </li>
    ))
  ) : (
    !loading && <p>No se encontraron resultados</p>
  )}
</ul>
  )
}
