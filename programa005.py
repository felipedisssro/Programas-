produtos = {}

print("Bem-vindo à lista de vendas da festa junina do IFSP!")
print("Digite os produtos e seus preços. Digite 'sair' para encerrar.\n")

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        print("\nPrograma encerrado. Obrigado!")
        break

    preco = input("Digite o preço do produto: ")

    produtos[nome] = preco

    print("\nLista de produtos atualizada:")
    for item in produtos:
        print("- " + item + ": R$" + produtos[item])
    print()
