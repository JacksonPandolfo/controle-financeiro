import { useNavigate, Link } from "react-router-dom";
import { useState } from "react";
import { login } from "../services/usuarioApi";
import toast from "react-hot-toast"

export default function Login({ setLogado }) {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const navigate = useNavigate();
  
  async function handleLogin() {
    const user = await toast.promise(login({ email, senha }), {
      loading: "Entrando...",
      success: "Login autorizado",
      error: (err) => err.message
    });
    if (user) {
      localStorage.setItem("usuario", JSON.stringify(user));

      setLogado(true)
      navigate("/transacoes");
    } else {
      alert("Login inválido");
    }
  }

  return (
    <div className="flex h-screen items-center justify-center bg-gray-100">
      <div className="w-full max-w-sm rounded-2xl bg-white p-8 shadow-lg">
        <h2 className="mb-6 text-center text-3xl font-bold text-gray-800">
          Login
        </h2>

        <div className="flex flex-col gap-4">
          <input
            className="rounded-lg border border-gray-300 p-3 outline-none transition focus:border-blue-500"
            placeholder="Email"
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            className="rounded-lg border border-gray-300 p-3 outline-none transition focus:border-blue-500"
            placeholder="Senha"
            onChange={(e) => setSenha(e.target.value)}
          />

          <button
            onClick={handleLogin}
            className="mt-2 rounded-lg bg-blue-500 p-3 font-semibold text-white transition hover:bg-blue-600"
          >
            Entrar
          </button>
        </div>
        <p className="mt-4 text-center text-sm text-gray-500">
          Não possui uma conta?{" "}
          <Link
            to="/register"
            className="cursor-pointer text-blue-500"
          >
            Cadastrar
          </Link>
        </p>
      </div>
    </div>
  );
}
