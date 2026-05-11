class Livro:
    Coletania_de_Livros = []
    def __init__ (self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        self.Coletania_de_Livros.append(self)

    def __str__(self):
        return f'{self._titulo} - {self._autor} ({self._ano_publicacao})'
    
    @classmethod
    def verificar_disponibilidade(cls, Ano):
        print(f"Verificando disponibilidade do livros de um determinado ano: {Ano}")
        opcao = input("Escolha um ano de publicação para verificar a disponibilidade (1954 ou 1949): ")
        for livro in cls.Coletania_de_Livros:
            if livro._ano_publicacao == int(opcao):
                return f'O livro "{livro._titulo}" está disponível.'
        return f'Nenhum livro do ano {Ano} está disponível.'
    

    @classmethod
    def listar_livros(cls):
        print(f"{'Título'.ljust(30)} - {'Autor'.ljust(30)} - {'Ano de Publicação'.ljust(20)} | {'Disponibilidade'}")
        for livro in cls.Coletania_de_Livros:
            print(f'{livro._titulo.ljust(30)} - {livro._autor.ljust(30)} - {str(livro._ano_publicacao).ljust(20)} | {livro.disponibilidade}')


   
    def emprestar(self):
        self._disponivel = not self._disponivel

    @property
    def disponibilidade(self):
        return 'Disponível' if self._disponivel else 'Indisponível'
    
 
   