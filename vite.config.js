import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api-ml': { //Lo modifico para poder testear la API de MercadoLibre sin backend
        target: 'https://api.mercadolibre.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api-ml/, ''),
      },
    },
  },
})
