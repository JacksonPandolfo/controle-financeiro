import { useState } from "react";
import { create } from "../services/categoriaApi";
import toast from "react-hot-toast";

export default function CategoriaModal({ onCancel, onSave }) {
  const [nome, setNome] = useState("");

  async function handleSave() {
    try {
      if (nome != "" && nome != null) {
        const data = { nome };
        const req = await toast.promise(create(data), {
          loading: "Salvando...",
          success: "Categoria registrada com sucesso",
          error: (err) => err.message,
        });
        onSave();
      } else {
        toast.error("Nome da categoria não pode ser vazio");
      }
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black/50">
      <div className="w-96 rounded-xl bg-white p-6">
        <h2 className="mb-4 text-xl font-bold">Nova Categoria</h2>

        <label className="mb-1 block text-sm font-medium text-gray-700">
          Nome:
        </label>
        <input
          className="mb-2 w-full rounded border p-2"
          placeholder="Nome da categoria"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />

        <div className="mt-4 flex justify-end gap-2">
          <button
            onClick={onCancel}
            className="rounded bg-gray-400 px-3 py-1 text-white"
          >
            Cancelar
          </button>

          <button
            onClick={handleSave}
            className="rounded bg-green-500 px-3 py-1 text-white"
          >
            Salvar
          </button>
        </div>
      </div>
    </div>
  );
}