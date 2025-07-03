def trocar(vet, i, j):
    """Função para trocar os elementos vet[i] e vet[j]."""
    temp = vet[i]
    vet[i] = vet[j]
    vet[j] = temp

vet = []
for i in range(5):
    resp = int(input(f"Digite o número {i+1}: "))
    vet.append(resp)

for i in range(4):  # ou len(vet) - 1
    for j in range(4 - i):  # ou len(vet) - 1 - i
        if vet[j] > vet[j + 1]:
            trocar(vet, j, j + 1)

print("Vetor ordenado:", vet)

