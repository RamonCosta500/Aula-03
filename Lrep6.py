nomes = [] # Cria uma lista vazia
locais = []
continua = "sim"

while continua == "sim":
    nome = input("Qual o nome da passageiro: ")
    nomes.append(nome) # Adiciona o nome na lista de nomes
    local = input("Qual local de viagem: ")
    locais.append(local)
    continua = input("Deseja continuar?: ")
 
for i in range(len(nomes)):
    print(f"{i + 1} - {nomes[i]} e {locais[i]} ")    

