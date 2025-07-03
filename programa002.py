listaTimes = []
seguir = 1

while seguir == 1:
    time = input("Digite o nome do time (ou 'sair' para encerrar): ")
    if time.lower() == "sair":
        print("Até logo!")
        break

    ano_de_fundacao = input("Digite o ano de fundação: ")
    jogador = input("Digite um jogador que atua no time: ")

    futbol = {"clube": time, "fundação": ano_de_fundacao, "jogador": jogador}
    listaTimes.append(futbol)

    seguir = int(input("Digite 1 para seguir, 0 para sair, ou 2 para excluir um time da lista: "))

    if seguir == 2:
        if len(listaTimes) == 0:
            print("A lista está vazia, nada para excluir.")
            seguir = 1
            continue

        print("\nTimes cadastrados:")
        for i, item in enumerate(listaTimes):
            print(f"{i}: {item}")

        try:
            indice = int(input("Digite o número do time que deseja excluir: "))
            if 0 <= indice < len(listaTimes):
                excluido = listaTimes.pop(indice)
                print(f"Time excluído: {excluido}")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
        
        seguir = int(input("Digite 1 para seguir ou 0 para sair: "))

print("\nLista final de times cadastrados:")
for time in listaTimes:
    print(time)
