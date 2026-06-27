import React, { useEffect, useState } from "react";
import { get_all } from "../services/categoriaApi";
import { create, update } from "../services/transacaoApi";
import CategoriaModal from "./CategoriaModal";
import { NumericFormat } from 'react-number-format'
import toast from "react-hot-toast";

export default function TransacaoModal({ onCancel, onSave, editing }) {
  const [transacaoId, setTransacaoId] = useState("")
  const [descricao, setDescricao] = useState("");
  const [valor, setValor] = useState("");
  const [tipo, setTipo] = useState("");
  const [categoriaId, setCategoriaId] = useState("")
  const [categorias, setCategorias] = useState([])
  const [showModal, setShowModal] = useState(false)
  
  // 🔥 carrega dados quando for edição
  useEffect(() => {
    if (editing) {
      setTransacaoId(editing.id || "");
      setDescricao(editing.descricao || "");
      setValor(editing.valor || "");
      setTipo(editing.tipo || "");
      setCategoriaId(editing.categoria.id || "");
    } else {
      setTransacaoId("")
      setDescricao("");
      setValor("");
      setTipo("");
      setCategoriaId("");
    }
  }, [editing]);

  useEffect(() => {
    get_categorias();
  }, [])

  async function get_categorias() {
    try {
      const data = await toast.promise(get_all(), {
        loading: "Carregando...",
        error: "Erro ao buscar as transações",
      });
      setCategorias(data)
    } catch (error) {
      console.log(error)
    }
  }

  const isEdit = !!editing;

  async function handleSave() {
    const data = {
      valor: valor,
      tipo,
      descricao,
      categoria_id: categoriaId,
    };
    if (
      data.valor != "" &&
      data.valor != null &&
      data.tipo != "" &&
      data.tipo != null &&
      data.descricao != "" &&
      data.descricao != null &&
      data.categoria_id != "" &&
      data.categoria_id != null
    ) {
        if (isEdit) {
          if(editing.descricao != data.descricao || 
            editing.valor != data.valor || 
            editing.tipo != data.tipo || 
            editing.categoria.id != data.categoria_id){
            const req = await toast.promise(update(transacaoId, data), {
              loading: "Atualizando...",
              success: "Transação atualizada com sucesso",
              error: (err) => err.message ||  "Erro ao editar a transação",
            });
            onSave()
          } else {
            toast.error("Não existem alterações");
          }
        } else {
            const req = await toast.promise(create(data), {
              loading: "Salvando...",
              success: "Transação registrada com sucesso",
              error: (err) => err.message || "Erro ao registrar a transação",
            });
            onSave();
          } 
      } else {
        toast.error("Os campos não podem ser vazios");
      }
  }

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black/50">
      <div className="w-96 rounded-xl bg-white p-6">
        <h2 className="mb-4 text-xl font-bold">
          {isEdit ? "Editar transação" : "Nova transação"}
        </h2>

        <label className="mb-1 block text-sm font-medium text-gray-700">
          Descrição:
        </label>
        <input
          className="mb-2 w-full rounded border p-2"
          placeholder="Descrição"
          value={descricao}
          onChange={(e) => setDescricao(e.target.value)}
        />

        <label className="mb-1 block text-sm font-medium text-gray-700">
          Valor:
        </label>
        <NumericFormat
          className="mb-2 w-full rounded border p-2"
          placeholder="Valor"
          value={valor}
          thousandSeparator="."
          decimalSeparator=","
          prefix="R$"
          decimalScale={2}
          fixedDecimalScale
          onValueChange={(values) => {
            setValor(values.floatValue)
          }}
        />

        <label className="mb-1 block text-sm font-medium text-gray-700">
          Categoria:
        </label>

        <div className="flex justify-between gap-2">
          <select
            className="w-48 rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 shadow-sm"
            value={categoriaId}
            onChange={(e) => setCategoriaId(e.target.value)}
          >
            <option value="">Selecione</option>
            {categorias.length == 0 ? (
              <option disabled value="">
                Sem categoria
              </option>
            ) : (
              categorias.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.nome}
                </option>
              ))
            )}
          </select>
          <button
            onClick={() => setShowModal(true)}
            className="rounded bg-green-500 px-3 py-1 text-white"
          >
            Nova categoria
          </button>
        </div>

        <label className="mb-1 block text-sm font-medium text-gray-700">
          Tipo de movimentação:
        </label>

        <select
          className="w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-700 shadow-sm"
          value={tipo}
          onChange={(e) => setTipo(e.target.value)}
        >
          <option value="">Selecione</option>
          <option value="entrada">Entrada</option>
          <option value="saida">Saída</option>
        </select>

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
            {isEdit ? "Atualizar" : "Salvar"}
          </button>
        </div>
      </div>
      {showModal && (
        <CategoriaModal
          onCancel={() => {
            setShowModal(false);
          }} 
          onSave={() => {
            setShowModal(false);
            get_categorias();
          }}
        />
      )}
    </div>
  );
}
