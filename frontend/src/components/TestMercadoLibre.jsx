import { useState } from "react";
import { searchMercadoLibre } from "../api/mercadoLibre.js";

export default function TestMercadoLibre() {
  const [query, setQuery] = useState("");
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setError(null);
    setProducts([]);

    try {
      const data = await searchMercadoLibre(query);

      if (data.status === "success" && Array.isArray(data.products)) {
        // Filtra productos con datos válidos
        const validProducts = (Array.isArray(data.products) ? data.products : [])
          .filter((p) => p && (p.title || p.id))
          .map((p) => ({
              id: p.id ?? Math.random().toString(36).slice(2, 9),
              title: p.title ?? "Sin título",
              price: p.price ?? null,
              thumbnail: (() => {
                // intenta usar secure_url de pictures, luego url, luego thumbnail, y fuerza https
                const candidate =
                  p.pictures?.[0]?.secure_url ||
                  p.pictures?.[0]?.url ||
                  p.thumbnail ||
                  "https://via.placeholder.com/300x150?text=Sin+imagen";
                if (candidate.startsWith("//")) return "https:" + candidate;
                if (candidate.startsWith("http:")) return candidate.replace(/^http:/, "https:");
                return candidate;
              })(),
              productUrl:
                p.permalink ??
                p.productUrl ??
                `https://www.mercadolibre.com.ar/search?q=${encodeURIComponent(
              query
                )}`,
            }));
        setProducts(validProducts);
      } else {
        setError("No se encontraron resultados o la API no respondió correctamente.");
      }
    } catch (err) {
      console.error(err);
      setError("Error al obtener productos. Intenta nuevamente.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🛒 Búsqueda en Mercado Libre</h2>

      <div style={styles.searchBox}>
        <input
          type="text"
          placeholder="Buscar producto..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={styles.input}
        />
        <button onClick={handleSearch} style={styles.button}>
          Buscar
        </button>
      </div>

      {loading && <p style={styles.loading}>Cargando resultados...</p>}
      {error && <p style={styles.error}>{error}</p>}

      <div style={styles.grid}>
        {products.map((p, i) => (
          <div key={i} style={styles.card}>
            <img
              src={p.thumbnail}
              alt={p.title}
              style={styles.image}
              loading="lazy"
            />
            <h3 style={styles.cardTitle}>{p.title}</h3>
            <p style={styles.price}>
              {p.price ? `$${p.price}` : "Precio no disponible"}
            </p>
            <a href={p.productUrl} target="_blank" rel="noopener noreferrer" style={styles.link}>
              Ver en Mercado Libre
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: "2rem",
    backgroundColor: "#0d1117",
    color: "#f0f6fc",
    minHeight: "100vh",
    fontFamily: "Arial, sans-serif",
  },
  title: {
    fontSize: "1.8rem",
    textAlign: "center",
    marginBottom: "1rem",
  },
  searchBox: {
    display: "flex",
    justifyContent: "center",
    gap: "0.5rem",
    marginBottom: "1rem",
  },
  input: {
    padding: "0.5rem",
    fontSize: "1rem",
    borderRadius: "6px",
    border: "1px solid #30363d",
    backgroundColor: "#161b22",
    color: "#f0f6fc",
    width: "250px",
  },
  button: {
    padding: "0.5rem 1rem",
    backgroundColor: "#238636",
    color: "white",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
    fontWeight: "bold",
  },
  loading: {
    textAlign: "center",
    color: "#58a6ff",
  },
  error: {
    textAlign: "center",
    color: "#f85149",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
    gap: "1rem",
    marginTop: "1rem",
  },
  card: {
    backgroundColor: "#161b22",
    borderRadius: "10px",
    padding: "1rem",
    textAlign: "center",
    boxShadow: "0 2px 5px rgba(0,0,0,0.2)",
  },
  image: {
    width: "100%",
    height: "150px",
    objectFit: "contain",
    borderRadius: "6px",
  },
  cardTitle: {
    fontSize: "1rem",
    margin: "0.5rem 0",
    minHeight: "40px",
  },
  price: {
    color: "#58a6ff",
    fontWeight: "bold",
  },
  link: {
    display: "inline-block",
    marginTop: "0.5rem",
    color: "#f0f6fc",
    textDecoration: "underline",
  },
};
