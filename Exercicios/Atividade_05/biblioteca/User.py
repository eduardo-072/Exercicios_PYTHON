from Livros import Livro, LivroDigital

class User:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livrosEmprestados = []

    def pegarEmprestado(self, biblioteca):

        titulo = input("Digite o livro que deseja pegar: ")

        if titulo in biblioteca.livros and biblioteca.livros[titulo]["disponivel"]:

            confere = input(f"Livro correto {titulo}? (S/N): ")

            if confere.lower() == "s":
                biblioteca.livros[titulo]["disponivel"] = False
                self.livrosEmprestados.append(titulo)
                print("Livro emprestado com sucesso")

            else:
                print("Operação cancelada")

        else:
            print("Livro não encontrado ou indisponível")

    def devolverLivro(self, biblioteca):

        titulo = input("Qual livro deseja devolver? ")

        if titulo in self.livrosEmprestados:

            biblioteca.livros[titulo]["disponivel"] = True
            self.livrosEmprestados.remove(titulo)

            print(f"Livro {titulo} devolvido")

        else:
            print("Esse livro não está com o usuário")