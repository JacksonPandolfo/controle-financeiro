import { API } from "../config";

export async function create(data) {
  const usuario = JSON.parse(localStorage.getItem("usuario"))
  const res = await fetch(`${API}/categoria`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "usuario-id": usuario.id,
    },
    body: JSON.stringify(data),
  });

  const dataResponse = await res.json()
  if(!res.ok){
    throw new Error(dataResponse?.detail || "Erro ao criar a categoria")
  }

  return dataResponse;
}

export async function get_all() {
  const usuario = JSON.parse(localStorage.getItem("usuario"));
  const res = await fetch(`${API}/categoria`, {
    method: "GET",
    headers: {
      "usuario-id": usuario.id,
    },
  });
  
  const dataResponse = await res.json();
  
  if (!res.ok) {
    throw new Error(dataResponse?.detail || "Erro ao buscar as categorias");
  }

  return dataResponse;
}