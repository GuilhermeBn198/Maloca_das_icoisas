import os
import time

class Remedio:
    def __init__(self, nome, valor, estado='ativo'):
        self.nome = nome
        self.valor = valor
        self.estado = estado

class Farmacia:
    def __init__(self):
        self.array_remedios = [
            Remedio('Paracetamol', 10.50),
            Remedio('Ritalina', 30.25),
            Remedio('Zolpidem', 15.75)
        ]

    def menu(self):
        print("--- Farmaloca ---")
        print("--- 1. Cadastrar remédio ---")
        print("--- 2. Listar Remédio ---")
        print("--- 3. Alterar estado do remédio ---")
        print("--- 4. Sair ---")

    def exibir_opcoes(self):
        try:
            escolha = int(input("Escolha uma opção: "))
            print(f"Você escolheu {escolha}!")  
            if escolha == 1:
                self.cadastrar_remedio()
            elif escolha == 2:
                self.listar_remedios()
            elif escolha == 3:
                self.alterar_estado_remedio()
            elif escolha == 4:
                print("Sair")
                return False
            return True
        except ValueError:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            return True

    def cadastrar_remedio(self):
        print("Cadastrar remédio")
        nome = input("Digite o nome do remédio: ")
        valor = float(input("Digite o valor do remédio: "))
        novo_remedio = Remedio(nome, valor)
        self.array_remedios.append(novo_remedio)
        print(f"\n\nO remédio {nome} foi adicionado com sucesso!")
        time.sleep(2)

    def listar_remedios(self):
        print("Listar remédios:")
        for i, remedio in enumerate(self.array_remedios, start=1):
            print(f"{i}. Nome: {remedio.nome}, Valor: R$ {remedio.valor:.2f}, Estado: {remedio.estado}")

    def alterar_estado_remedio(self):
        print("Alterar estado do remédio")
        self.listar_remedios()
        try:
            indice = int(input("Digite o número do remédio para alterar estado: ")) - 1
            if 0 <= indice < len(self.array_remedios):
                novo_estado = input("Digite o novo estado do remédio (ativo/inativo): ").strip().lower()
                if novo_estado == 'ativo' or novo_estado == 'inativo':
                    self.array_remedios[indice].estado = novo_estado
                    print(f"Estado do remédio '{self.array_remedios[indice].nome}' alterado para {novo_estado}.")
                else:
                    print("Estado inválido. Use 'ativo' ou 'inativo'.")
            else:
                print("Índice fora dos limites.")
        except ValueError:
            print("Índice inválido. Use um número válido.")

    def iniciar(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.menu()
            continuar = self.exibir_opcoes()
            if not continuar:
                break
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    farmacia = Farmacia()
    farmacia.iniciar()
