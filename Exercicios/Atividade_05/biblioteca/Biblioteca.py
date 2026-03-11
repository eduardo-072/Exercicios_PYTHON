from Livros import Livro, LivroDigital
class Biblioteca:
        
    def __init__ (self):
        self.livros = {}
        self.listaUser = {}

        for titulo, info in Livro.livros.items():
            self.livros[titulo] = {
                "autor": info["autor"],
                "ano": info["ano"],
                "disponivel": info["disponivel"]
            }

    def adicionarLivro(self):
        livroADD = input("Digite o nome do livro: ")
        if livroADD in self.livros:
            print("Livro ja cadastrado")
        else:
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano de publicação do livro: "))

            self.livros[livroADD] = {
                "autor": autor,
                "ano": ano,
                "disponivel": True,
            }
            print(f'O Livro {livroADD} foi adicionado na biblioteca')
    
    def cadastrarUser(self):
        nomeUser = input("Digite o nome a ser cadastrado")
        idade = int(input("Digite a idade do usuário (mínimo 16 anos): "))
        
        if idade < 16:
            print("Idade não aceita para cadastro")
        else:
            self.listaUser[nomeUser] = idade
            print(f'Usuario {nomeUser} foi cadastrado')

    
    def livrosDisponiveis(self):
        print("Livros catalogados da biblioteca")

        for titulo, info in self.livros.items():
            print("Titulo: ", titulo)
            print("Autor: ",info["autor"])
            print("Disponibilidade: ", info["disponivel"])
            print("---------------------------")

    def listarLivrosEmprestados(self):
        print()
        print("Livros emprestados") 

        emprestados = False

        for titulo, info in self.livros.items():
            if not info["disponivel"]:
                print(f'¬ {titulo} ({info["autor"]}, {info["ano"]})')
                emprestados = True
        if not emprestados:
            print("Nenhum livro está emprestado")
        print()
