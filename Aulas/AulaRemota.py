#Em python o conteudo da lista n tem distinção de tipo, ou seja, pode conter elementos de tipos diferentes
#mostrarndo uma lista de números
lista = [20, 56, 48, 69]
print(lista)
print("Quantidade de elementos na lista: ", len(lista))

#pegando o último elemento da lista de forma decrescente
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

#modificando valores da lista
#lista[-2] = 50

#insere um numero na posição -2
lista.insert(-2, 50)
print(lista)

#adiciona um numero na lista
lista.append(80)
print(lista)

#juntando duas listas
lista2 = ['a', 'b', 'c']
lista.extend(lista2)
print(lista)

#removendo um elemento da lista

#removendo elemento
lista.remove('b')
print(lista)

#removendo por posição
lista.pop(-1)
print(lista)

del lista[-1]
print(lista)

#limpa a lista, mas não exclui a variável
lista.clear()
print(lista)

for item in lista2:
    print(item)

listas = [['a', 'b'], 10, 20]
print(listas[0][1])

#Dicionário é uma estrutura de dados que armazena pares de chave-valor, onde cada chave é única e é usada para acessar o valor correspondente.

Aluno = {
    "id": '0001',
    "nome": 'Eduardo'
}

aluno = {
    'aluno1' : {
        "id": '0002',
        "nome": 'Duda'
    },
    'aluno2' : {
        'id' : '0003',
        'nome' : 'Maria'
    }
}

#Pegando valores dentro do dicionário
print(aluno)
print(aluno['aluno2']['nome'])

#atualizando um valor com um campo novo
aluno.update({"sobrenome": "Gonçalves"})   

#nessa função ele cria uma lista
print(aluno.values())

#mostra as chaves do dicionário, ou seja, os nomes dos campos
print(aluno.keys())

print(aluno.items())

print()

for chave,valor in aluno.items():
    print(f'{chave} = {valor}')

aluno['curso'] = "DSM"
print(aluno)

del aluno['curso']
print(aluno)

if 'id' in aluno:
    print("Encontrado")
else: 
    print("Não encontrado")


