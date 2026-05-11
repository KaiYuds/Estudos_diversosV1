from livro import Livro


livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
livro2 = Livro('1984', 'George Orwell', 1949)
livro1.emprestar()



def main():
    Livro.listar_livros()
        

if __name__ == "__main__":
    main()