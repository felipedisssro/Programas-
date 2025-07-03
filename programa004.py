alfabeto = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def troca(pl, chave):
    cripto = []
    for letra in pl:
        if letra in alfabeto:
            i = alfabeto.index(letra)
            i = (i + chave) % 26
            cripto.append(alfabeto[i])
        else:
            cripto.append(letra)
    return cripto

palavra = input("Digite uma palavra: ").lower()
chave = int(input("Digite a chave de criptografia (ex: 3): "))

lista = troca(palavra, chave)

print("Palavra criptografada:")
print("".join(lista))
