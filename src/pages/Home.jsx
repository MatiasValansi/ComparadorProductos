export default function Home() {
    return (
        <div style={{ padding: 20, fontFamily: 'Arial, sans-serif' }}>
            <h1>Comparador de Productos</h1>
            <p>Introduce algo en la búsqueda (no funciona):</p>
            <input
                type="search"
                placeholder="Buscar..."
                style={{
                    width: '100%',
                    maxWidth: 400,
                    padding: '8px 10px',
                    fontSize: 16,
                    boxSizing: 'border-box',
                }}
                onChange={() => {}}
            />
        </div>
    );
}
