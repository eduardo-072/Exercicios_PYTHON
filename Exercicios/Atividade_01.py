item = ""
peso_total = 0
itens = []

print("Olá mochileiro! Antes de embarcar, digite as informações abaixo.")
nome = input("Digite seu nome: ")
print(nome+ ", informe o conteúdo da sua mochila.\n*Um item de cada vez*")


while True:
    item = input("Nome do item (ou 'fim' para encerrar): ")
    if item == "fim":
        break
    
    peso_item = float(input("Peso (kg): "))
    
    if peso_total + peso_item <= 23:
        peso_total += peso_item
        itens.append((item, peso_item))
        print(f"Item adicionado {item} a mochila.\nLimite de 23kg | Restante: {23 - peso_total}kg\n")
    else:
        print("O item",item,"com peso",peso_item,"kg, ultrapassa o limite de 23kg e não pode ser adicionado a mochila.")
        print(f"Peso atual da mochila: {23 - peso_total}kg.\n")    

print("\n===== RESUMO DA MOCHILA =====")
print(f"Mochileiro: {nome}")
print(f"Peso total: {peso_total}kg")
print(f"Limite restante: {23 - peso_total}kg")
print("\nItens adicionados:")
for nome_item, peso_item in itens:
    print(f" - {nome_item}: {peso_item}kg")