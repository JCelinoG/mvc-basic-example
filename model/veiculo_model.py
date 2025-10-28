class Veiculo:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa}"


class VeiculoRepository:
    def __init__(self, conexao):
        self.conexao = conexao
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS veiculos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                marca VARCHAR(100),
                modelo VARCHAR(100),
                ano VARCHAR(10),
                placa VARCHAR(20) UNIQUE
            )
        """)
        self.conexao.commit()
        cursor.close()

    def salvar(self, veiculo):
        try:
            cursor = self.conexao.cursor()
            sql = "INSERT INTO veiculos (marca, modelo, ano, placa) VALUES (%s, %s, %s, %s)"
            valores = (veiculo.marca, veiculo.modelo, veiculo.ano, veiculo.placa)
            cursor.execute(sql, valores)
            self.conexao.commit()
        except Exception as e:
            print(f"Erro ao salvar veículo: {e}")
        finally:
            cursor.close()

    def listar(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT marca, modelo, ano, placa FROM veiculos")
            resultados = cursor.fetchall()
            return [Veiculo(*r) for r in resultados]
        except Exception as e:
            print(f"Erro ao listar veículos: {e}")
            return []
        finally:
            cursor.close()

    def buscar_por_placa(self, placa):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT marca, modelo, ano, placa FROM veiculos WHERE placa = %s", (placa,))
            resultado = cursor.fetchone()
            return Veiculo(*resultado) if resultado else None
        except Exception as e:
            print(f"Erro ao buscar veículo: {e}")
            return None
        finally:
            cursor.close()

    def editar(self, placa, nova_marca, novo_modelo, novo_ano):
        try:
            cursor = self.conexao.cursor()
            sql = "UPDATE veiculos SET marca = %s, modelo = %s, ano = %s WHERE placa = %s"
            valores = (nova_marca, novo_modelo, novo_ano, placa)
            cursor.execute(sql, valores)
            self.conexao.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao editar veículo: {e}")
            return False
        finally:
            cursor.close()

    def excluir(self, placa):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM veiculos WHERE placa = %s", (placa,))
            self.conexao.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao excluir veículo: {e}")
            return False
        finally:
            cursor.close()