class Livro:
    def __init__(self, titulo, autor, ano, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel
    
    livros = {
    "Harry Potter": {
        "autor": "JK Rowling",
        "ano": 2000,
        "disponivel": True
    },
    "1984": {
        "autor": "George Orwell",
        "ano": 1949,
        "disponivel": True
    },
    "O Hobbit": {
        "autor": "JRR Tolkien",
        "ano": 1937,
        "disponivel": True
    }
}

    def emprestar(self, biblioteca):
        print("Livros disponiveis na biblioteca: ")
        
        for livro in biblioteca.values():
            if livro.disponivel:
                print(f"- {livro.titulo} ,{livro.autor}, {livro.ano}")
        titulo = input("Qual livro deseja pegar? ")

        if titulo in biblioteca:
            livro = biblioteca[titulo]
            if livro.disponivel:
                livro.disponivel = False
            else:
                print(f"{titulo} ja foi emprestado, escolha outro livro para pegar")
        else: 
            print("Livro não encontrado")
            print()

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)

    def emprestarLivro(self, biblioteca):
        titulo = input("Digite o livro digital que deseja comprar: ")
        if titulo in biblioteca and biblioteca[titulo].disponivel:
            confere = input(f"Livro correto {titulo}? (S/N): ")
            if confere.lower() == "s":
                biblioteca[titulo].disponivel = False
                print("Livro digital adquirido")
            else:
                print("Erro na operação")
        else:
            print("Livro digital não encontrado ou indisponível")