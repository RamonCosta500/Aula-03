lista = []
contador = 0
soma = 0

while contador != 5 :
    numero = int(input("Digite numeros que deseja que sejam somados: "))
    lista.append(numero)
    contador += 1
    
for i in range(len(lista)):
    soma += lista[i]

print(soma)