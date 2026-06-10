
from Modelos.avaliacao import Avaliacao
from Modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
        '''Classe que representa um restaurante, com nome, categoria, status e avaliações.'''

        restautantes = []

        '''
        Inicializa uma Instância da classe Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.

        '''
        def __init__(self, nome, categoria):
            self._nome = nome.title()
            self._categoria = categoria.upper()
            self._ativo = False
            self._avaliacao = []
            self._cardapio = []
            Restaurante.restautantes.append(self)

        def __str__(self):
            """Retorna uma representação em string do restaurante."""
            return f'{self._nome} - {self._categoria}'
        
        @classmethod
        def listar_restaurantes(cls):
            print(f"{'Nome do restaurante'.ljust(25)} - {'Avaliação'.ljust(25)} - {'Categoria'.ljust(25)} | {'Status'}")
            for restaurante in cls.restautantes:
                print(f'{restaurante._nome.ljust(25)} - {str(restaurante.media_avaliacao).ljust(25)} - {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

        
        
        @property
        def ativo(self):
             return '✅' if self._ativo else '❎'
        
        def alterar_status(self):
             self._ativo = not self._ativo

        def adicionar_avaliacao(self, cliente, nota):
            
            if 0 < avaliacao._nota < 5:
                avaliacao = Avaliacao(cliente, nota)
                self._avaliacao.append(avaliacao)
            else:
                print('Nota inválida. A nota deve ser entre 1 e 5.')

        @property
        def media_avaliacao(self):
            if not self._avaliacao:
                 return 'Restaurante sem avaliações'
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            media = round(soma_das_notas/len(self._avaliacao), 1)
            return media
        

        def adicionar_item_cardapio(self, item):
             if isinstance(item,ItemCardapio):
                self._cardapio.append(item)    
        
        def exibir_itens_cardapio(self):
            print(f'Cardapio do restaurante {self._nome}\n')
            for i,item in enumerate(self._cardapio,start=1):
                if hasattr(item, 'descricao'):
                    mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                    print(mensagem_prato)
                else:
                    mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                    print(mensagem_bebida)