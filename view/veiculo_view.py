import tkinter as tk
from tkinter import messagebox
from controller.veiculo_controller import VeiculoController

class VeiculoView:
    def __init__(self, root):
        self.controller = VeiculoController()
        self.root = root
        self.root.title("Cadastro de Veículos")

        # Campos de entrada
        tk.Label(root, text="Marca").grid(row=0, column=0)
        self.marca_entry = tk.Entry(root)
        self.marca_entry.grid(row=0, column=1)

        tk.Label(root, text="Modelo").grid(row=1, column=0)
        self.modelo_entry = tk.Entry(root)
        self.modelo_entry.grid(row=1, column=1)

        tk.Label(root, text="Ano").grid(row=2, column=0)
        self.ano_entry = tk.Entry(root)
        self.ano_entry.grid(row=2, column=1)

        tk.Label(root, text="Placa").grid(row=3, column=0)
        self.placa_entry = tk.Entry(root)
        self.placa_entry.grid(row=3, column=1)

        # Botões
        tk.Button(root, text="Cadastrar", command=self.cadastrar_veiculo).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Listar", command=self.listar_veiculos).grid(row=5, column=0, columnspan=2)

    def cadastrar_veiculo(self):
        marca = self.marca_entry.get()
        modelo = self.modelo_entry.get()
        ano = self.ano_entry.get()
        placa = self.placa_entry.get()
        self.controller.adicionar_veiculo(marca, modelo, ano, placa)
        messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
        self.marca_entry.delete(0, tk.END)
        self.modelo_entry.delete(0, tk.END)
        self.ano_entry.delete(0, tk.END)
        self.placa_entry.delete(0, tk.END)

    def listar_veiculos(self):
        veiculos = self.controller.listar_veiculos()
        lista = "\n".join(str(v) for v in veiculos)
        messagebox.showinfo("Veículos Cadastrados", lista if lista else "Nenhum veículo cadastrado.")