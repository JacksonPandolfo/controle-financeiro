import { API } from "../config";

export async function create(data) {
  const usuario = JSON.parse(localStorage.getItem("usuario"))
  try {
    
    const res = await fetch(`${API}/transacoes`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "usuario-id": usuario.id,
      },
      body: JSON.stringify(data),
    });
    
    const dataResponse = await res.json();
    
    if (!res.ok) {
      throw new Error(dataResponse?.detail || "Erro ao criar a transação");
    }

    return dataResponse;
  } catch (error) {
    return error
  }
}

export async function get_all() {
  const usuario = JSON.parse(localStorage.getItem("usuario"));
  const res = await fetch(`${API}/transacoes`, {
    method: "GET",
    headers: {
      "usuario-id": usuario.id,
    },
  });
  const data = await res.json();

  if(!res.ok){
    throw new Error(data?.detail || "Erro ao buscar as transações");
  }

  return data
}

export async function update(id, data) {
  const usuario = JSON.parse(localStorage.getItem("usuario"));
  const res = await fetch(`${API}/transacoes/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "usuario-id": usuario.id,
    },
    body: JSON.stringify(data),
  });

  const dataResponse = await res.json();
  
  if (!res.ok) {
    throw new Error(dataResponse?.detail || "Erro ao atualiar a transação");
  }

  return dataResponse;
}

export async function remove(id) {
  const usuario = JSON.parse(localStorage.getItem("usuario"));

  await fetch(`${API}/transacoes/${id}`, {
    method: "DELETE",
    headers: {
      "usuario-id": usuario.id,
    }
  });
}