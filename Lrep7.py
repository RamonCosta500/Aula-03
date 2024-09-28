
lista = []
# numero = int(input("Digite os numeros que deseja que sejam ordenados: "))
# lista.append(numero)

numero = 1
while numero != 0:
    numero = int(input("Digite outro numero que deseja que sejam ordenados: "))
    lista.append(numero)
   
ordem = input("Deseja ordem crescente ou decrescente ? :")

if ordem == "decrescente":
    contato = range(len(lista)):
        if lista[i] <= lista[i + 1]:
            c = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = c



