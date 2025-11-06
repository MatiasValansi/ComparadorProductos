import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import TestMercadoLibre from "../components/TestMercadoLibre";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/test-mercado-libre" element={<TestMercadoLibre />} />
      </Routes>
    </BrowserRouter>
  );
}
