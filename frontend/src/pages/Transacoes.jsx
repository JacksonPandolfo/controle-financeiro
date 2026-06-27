import { useEffect, useState } from "react";
import { create, get_all, remove } from "../services/transacaoApi"
import TransacaoModal from "../components/TransacaoModal";
import { NumericFormat } from "react-number-format";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import ConfirmaModal from "../components/ConfirmaModal";

export default function Transacoes({setLogado}) {
  const [transacoes, setTransacoes] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [editing, setEditing] = useState(null);
  const [openConfirm, setOpenConfirm] = useState(false);
  const [selectedId, setSelectedId] = useState(null)
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const user = JSON.parse(localStorage.getItem("usuario"))
  
  function logout() {
    localStorage.removeItem("usuario");
    setLogado(false)
    navigate("/login")
  }

  async function carregarTransacoes() {
    try {
      const data = await toast.promise(get_all(), {
        loading: "Buscando...",
        error: "Erro ao buscar as transações"
      });
      setTransacoes(data);
    } catch (error) {
      console.error("Erro ao buscar transações", error);
    }
    calculaSaldo()
  }

  function handleEdit(transacao) {
    setEditing(transacao);
    setShowModal(true);
  }

  async function handleDelete(id) {
    console.log(id)
    await toast.promise(remove(id), {
      loading: "Excluindo",
      success: "Transação excluida com sucesso",
      error: "Erro ao excluir a transação"
    });
    setOpenConfirm(false)
    carregarTransacoes();
  }

  function calculaSaldo(){
    let total = 0.00
    for (let index = 0; index < transacoes.length; index++) {
      const element = transacoes[index];
      if(element.tipo == "entrada"){
        total += element.valor;
      } else {
        total -= element.valor;
      }
      
    }
    return total
  }

  useEffect(() => {
    carregarTransacoes();
  }, []);

  return (
    <div className="flex h-screen flex-col bg-gray-100 p-6">
      <div className="mb-6 flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-800">
          Controle Financeiro - {user.nome}
        </h1>
        <div className="flex gap-3">
          <button
            onClick={() => {
              setEditing(null);
              setShowModal(true);
            }}
            className="rounded-lg bg-green-500 px-4 py-2 text-white transition hover:bg-green-600"
          >
            Nova transação
          </button>
          <button
            onClick={logout}
            className="rounded-lg bg-red-500 px-4 py-2 text-white transition hover:bg-red-600"
          >
            Logout
          </button>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto pr-2">
        <div className="grid gap-4">
          {transacoes.length === 0 ? (
            <p className="text-gray-500">Nenhuma transação encontrada</p>
          ) : (
            transacoes.map((t) => (
              <div
                key={t.id}
                className="flex items-center justify-between rounded-xl bg-white p-4 shadow"
              >
                <div>
                  <p className="font-semibold text-gray-800">{t.descricao}</p>

                  <p className="text-sm text-gray-500">
                    Categoria: {t.categoria.nome}
                  </p>

                  <p className="text-sm text-gray-500">
                    Responsável: {t.usuario.nome}
                  </p>

                  <p className="text-sm text-gray-500">
                    Data: {new Date(t.data_hora).toLocaleString("pt-BR")}
                  </p>
                </div>
                <div className="flex items-center gap-4">
                  <NumericFormat
                    className={`text-2xl font-bold ${
                      t.tipo === "entrada" ? "text-green-600" : "text-red-600"
                    }`}
                    displayType="text"
                    placeholder="Valor"
                    value={t.tipo == "entrada" ? t.valor : -t.valor}
                    thousandSeparator="."
                    decimalSeparator=","
                    prefix="R$ "
                    decimalScale={2}
                    fixedDecimalScale
                  />

                  <button
                    onClick={() => handleEdit(t)}
                    className="rounded bg-blue-500 px-3 py-1 text-white hover:bg-blue-600"
                  >
                    Editar
                  </button>

                  <button
                    onClick={() => {
                      setOpenConfirm(true);
                      setSelectedId(t.id)
                    }}
                    className="rounded bg-red-500 px-3 py-1 text-white hover:bg-red-600"
                  >
                    Excluir
                  </button>
                  <ConfirmaModal
                    isOpen={openConfirm}
                    onClose={() => setOpenConfirm(false)}
                    onConfirm={() => handleDelete(selectedId)}
                    loading={loading}
                  />
                </div>
              </div>
            ))
          )}
        </div>
      </div>
      <div className="mb-6 flex items-center justify-end gap-2">
        <h1 className="text-2xl font-bold text-gray-800">Saldo atual:</h1>
        <NumericFormat
          className={`${calculaSaldo() < 0 ? "text-red-600" : "text-green-600"} text-2xl font-bold`}
          displayType="text"
          placeholder="Valor"
          value={calculaSaldo()}
          thousandSeparator="."
          decimalSeparator=","
          prefix="R$ "
          decimalScale={2}
          fixedDecimalScale
        />
      </div>
      {showModal && (
        <TransacaoModal
          editing={editing}
          onCancel={() => {
            setShowModal(false);
            setEditing(null);
          }}
          onSave={() => {
            setShowModal(false);
            setEditing(null);
            carregarTransacoes();
          }}
        />
      )}
    </div>
  );
}
