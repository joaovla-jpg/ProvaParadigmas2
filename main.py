
class Sorvete:
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar(self, sorvete, quantidade):
        self.itens.append((sorvete, quantidade))

    def calcular_total(self):
        total = 0
        for sorvete, quantidade in self.itens:
            total += sorvete.preco * quantidade
        return total

    def mostrar(self):
        if not self.itens:
            print("\nO pedido está vazio.")
            return

        print("\nSeu pedido:")
        for sorvete, quantidade in self.itens:
            subtotal = sorvete.preco * quantidade
            print(f"{quantidade} x {sorvete.sabor} - R$ {subtotal:.2f}")

        print(f"Total: R$ {self.calcular_total():.2f}")


class Sorveteria:
    def __init__(self):
        self.cardapio = {
            1: Sorvete("Chocolate", 6.0),
            2: Sorvete("Morango", 5.0),
            3: Sorvete("Baunilha", 5.0),
            4: Sorvete("Flocos", 6.5)
        }
        self.pedido = Pedido()

    def mostrar_cardapio(self):
        print("\nCardápio da Elefantinho")
        for codigo, sorvete in sorted(self.cardapio.items()):
            print(f"{codigo} - {sorvete.sabor} - R$ {sorvete.preco:.2f}")

    def executar(self):
        print("Bem-vindo à Sorveteria Elefantinho!")

        while True:
            print("\n1 - Mostrar cardápio")
            print("2 - Adicionar sorvete")
            print("3 - Mostrar pedido e total")
            print("4 - Finalizar e sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.mostrar_cardapio()

            elif opcao == "2":
                self.mostrar_cardapio()

                try:
                    codigo = int(input("Código do sabor: "))
                    if codigo not in self.cardapio:
                        print("Sabor inválido.")
                        continue

                    quantidade = int(input("Quantidade: "))
                    if quantidade <= 0:
                        print("Quantidade inválida.")
                        continue

                    self.pedido.adicionar(self.cardapio[codigo], quantidade)
                    print("Sorvete adicionado ao pedido!")

                except ValueError:
                    print("Digite um número inteiro.")

            elif opcao == "3":
                self.pedido.mostrar()

            elif opcao == "4":
                self.pedido.mostrar()
                print("Obrigado pela visita à Elefantinho!")
                break

            else:
                print("Opção inválida.")


if __name__ == "__main__":
    sorveteria = Sorveteria()
    sorveteria.executar()
