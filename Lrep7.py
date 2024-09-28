
lista = []
# numero = int(input("Digite os numeros que deseja que sejam ordenados: "))
# lista.append(numero)

numero = 1
while numero != 0:
    numero = int(input("Digite outro numero que deseja que sejam ordenados: "))
    lista.append(numero)
   
ordem = input("Deseja ordem crescente ou decrescente ? :")

if ordem == "decrescente":
    for i in range(len(lista)):
        print(lista[i])
        print("___")
        for j in range(i + 1, len(lista)):
            print(lista[j])
            print("***")
            if lista[i] <= lista[j]:
                c = lista[i]
                lista[i] = lista[j]
                lista[j] = c

print(lista)


