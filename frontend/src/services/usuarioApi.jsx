import { API } from "../config";

export async function register(data) {
  const res = await fetch(`${API}/usuario`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });
  const dataResponse = await res.json()

  if (!res.ok) {
    throw new Error(dataResponse?.detail || "Erro ao cadastrar o usuário");
  }
  return dataResponse;
}

export async function login(data) {
  const res = await fetch(`${API}/usuario/login`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  })
  const dataResponse = await res.json()
  
  if (!res.ok) {
    throw new Error(dataResponse?.detail || "Email ou senha incorretos");
  }
  return dataResponse;
}