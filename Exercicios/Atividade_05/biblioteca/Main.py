from Biblioteca import Biblioteca
from Livros import Livro, LivroDigital
from User import User

class Main:
    
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.user = User("Eduardo", 777)
        
    def executarPrograma(self):

        while True:

            print("Bem vindo a Biblioteca da Fatec")
            print("Selecione uma das opções")
            print("1- Adicionar um livro")
            print("2- cadastrar o usuário")
            print("3- Realizar um empréstimo")
            print("4- Devolver o livro")
            print("5- Listar livros disponíveis")
            print("6- Listar livros emprestados")
            print("7- Sair do programa")

            opc = int(input("Escolha uma opção: "))

            if opc == 1:
                self.biblioteca.adicionarLivro()

            elif opc == 2:
                self.biblioteca.cadastrarUser()

            elif opc == 3:
                self.user.pegarEmprestado(self.biblioteca)

            elif opc == 4:
                self.user.devolverLivro(self.biblioteca)

            elif opc == 5:
                self.biblioteca.livrosDisponiveis()

            elif opc == 6:
                print("Programa encerrado")
                self.biblioteca.listarLivrosEmprestados()

            elif opc == 7:
                print("Encerrando o programa")
                exit()

            else:
                print("Opção inválida")


main = Main()
main.executarPrograma()