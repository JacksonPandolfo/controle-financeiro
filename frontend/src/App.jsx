import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useState } from "react";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Transacoes from "./pages/Transacoes";
import { Toaster } from "react-hot-toast"

function App() {
  const [logado, setLogado] = useState(!!localStorage.getItem("usuario"));
  const [registrado, setRegistrado] = useState(false);

   return (
     <>
       <Toaster
         toastOptions={{
           duration: 3000,
           style: {
             borderRadius: "12px",
             padding: "12px",
           },
         }}
       />
       <BrowserRouter>
         <Routes>
           <Route
             path="/login"
             element={
               logado ? (
                 <Navigate to="/transacoes" />
               ) : (
                 <Login setLogado={setLogado} />
               )
             }
           />

           <Route
             path="/register"
             element={
               logado ? (
                 <Navigate to="/transacoes" />
               ) : (
                 <Register setRegistrado={setRegistrado} />
               )
             }
           />

           <Route
             path="/transacoes"
             element={
               logado ? (
                 <Transacoes setLogado={setLogado} />
               ) : (
                 <Navigate to="/login" />
               )
             }
           />

           <Route
             path="*"
             element={<Navigate to={logado ? "/transacoes" : "/login"} />}
           />
         </Routes>
       </BrowserRouter>
     </>
   );
}

export default App;
