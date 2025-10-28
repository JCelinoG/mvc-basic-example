from model.veiculo_model import Veiculo, VeiculoRepository
from model.conexao_db import conectar

class VeiculoController:
    def __init__(self):
        conexao = conectar()
        if conexao:
            self.repositorio = VeiculoRepository(conexao)
        else:
            self.repositorio = None

    def adicionar_veiculo(self, marca, modelo, ano, placa):
        if self.repositorio:
            veiculo = Veiculo(marca, modelo, ano, placa)
            self.repositorio.salvar(veiculo)

    def listar_veiculos(self):
        if self.repositorio:
            return self.repositorio.listar()
        return []

    def editar_veiculo(self, placa, nova_marca, novo_modelo, novo_ano):
        if self.repositorio:
            return self.repositorio.editar(placa, nova_marca, novo_modelo, novo_ano)
        return False

    def excluir_veiculo(self, placa):
        if self.repositorio:
            return self.repositorio.excluir(placa)
        return False