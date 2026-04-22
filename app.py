import subprocess
import os

restaurantes = [{'nome': 'Restaurante A', 'categoria': 'Italiano', 'ativo': False},
               {'nome': 'Restaurante B', 'categoria': 'Mexicana', 'ativo': False}]

def exibir_nome_do_programa():
      print("""
            ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
            ─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
            ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
            ─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
            ─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
            ─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
            ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
            ─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
            ─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
            ─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
            ─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
            ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n
      """)


def exibir_menu():
      print('Bem-vindo ao Sabor Express!')
      print('1. Cadastrar Restaurante'
            '\n2. Listar Restaurantes'
            '\n3. Ativar Restaurante'
            '\n4. Sair')

def finalizar_app():
      exibir_subtitulo('Saindo do Sabor Express. Até logo!')

def voltar_ao_menu():
      input('\nPressione Enter para continuar...')
      main()

def opcao_invalida():
      print('Opção inválida. Por favor, escolha uma opção válida.\n')
      voltar_ao_menu()
      
def exibir_subtitulo(subtitulo):
      os.system('cls')
      print(f'--- {subtitulo} ---\n')
            
def cadastrar_restaurante():
      exibir_subtitulo('Cadastro de Restaurante')
      nome_restaurante = input('Digite o nome do restaurante: ')
      categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
      print(f'Restaurante "{nome_restaurante}" cadastrado com sucesso!')
      dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
      restaurantes.append(dados_do_restaurante)
      voltar_ao_menu()

def listar_restaurantes():
      exibir_subtitulo('Lista de Restaurantes Cadastrados')
      if restaurantes:
            for restaurante in restaurantes:
                 nome_restaurante = restaurante['nome']
                 categoria = restaurante['categoria']
                 ativo = restaurante['ativo']
                 print(f'- {nome_restaurante} ({categoria}) - {"Ativo" if ativo else "Inativo"}')

      else:
            print('Nenhum restaurante cadastrado.')
      voltar_ao_menu()

def alterar_status_restaurante():
      exibir_subtitulo('Ativar Restaurante')
      if restaurantes:
            for restaurante in restaurantes:
                 nome_restaurante = restaurante['nome']
                 categoria = restaurante['categoria']
                 ativo = restaurante['ativo']
                 print(f'- {nome_restaurante} ({categoria}) - {"Ativo" if ativo else "Inativo"}')
      nome_restaurante = input('\nDigite o nome do restaurante que deseja ativar: ')
      for restaurante in restaurantes:
            if restaurante['nome'].lower() == nome_restaurante.lower():
                  restaurante['ativo'] = True
                  print(f'Restaurante "{restaurante["nome"]}" ativado com sucesso!')
                  break
      else:
            print(f'Restaurante "{nome_restaurante}" não encontrado.')
      voltar_ao_menu()


def escolher_opção():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            print(f'Opção escolhida: {opcao_escolhida}')

      
            if opcao_escolhida == 1:
                  print('Cadastrar Restaurante')
                  cadastrar_restaurante()

            elif opcao_escolhida == 2:
                  print('Listar Restaurantes')
                  listar_restaurantes()

            elif opcao_escolhida == 3:
                  alterar_status_restaurante()

            elif opcao_escolhida == 4:
                  finalizar_app()
            
      except:
            opcao_invalida()
            

def main():
      os.system('cls')
      exibir_nome_do_programa()
      exibir_menu()
      escolher_opção()

if __name__ == '__main__':
      main()