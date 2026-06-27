import { useState } from "react";
import { register } from "../services/usuarioApi";
import { useNavigate, Link } from "react-router-dom";
import toast from "react-hot-toast"

export default function Register({ setRegistrado }) {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const navigate = useNavigate()

  async function handleRegister() {
    const data = {nome, email, senha}
    
    if(data){
      await toast.promise(register(data), {
        loading: "Registrando usuário...",
        success: "Usuário cadastrado com sucesso",
        error: (err) => err.message,
      });
    }
    
    setRegistrado(true)
    navigate("/login")
  }

  return (
    <div className="flex h-screen items-center justify-center bg-gray-100">
      <div className="w-full max-w-sm rounded-2xl bg-white p-8 shadow-lg">
        <h2 className="mb-6 text-center text-3xl font-bold text-gray-800">
          Cadastro
        </h2>

        <div className="flex flex-col gap-4">
          <input
            className="rounded-lg border border-gray-300 p-3 outline-none transition focus:border-green-500"
            placeholder="Nome"
            onChange={(e) => setNome(e.target.value)}
          />

          <input
            className="rounded-lg border border-gray-300 p-3 outline-none transition focus:border-green-500"
            placeholder="Email"
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            className="rounded-lg border border-gray-300 p-3 outline-none transition focus:border-green-500"
            placeholder="Senha"
            onChange={(e) => setSenha(e.target.value)}
          />

          <button
            onClick={handleRegister}
            className="mt-2 rounded-lg bg-green-500 p-3 font-semibold text-white transition hover:bg-green-600"
          >
            Cadastrar
          </button>
        </div>
        <p className="mt-4 text-center text-sm text-gray-500">
          Já tem conta?{" "}
          <Link
            to="/login"
            className="cursor-pointer text-blue-500"
          >
            Voltar para login
          </Link>
        </p>
      </div>
    </div>
  );
}