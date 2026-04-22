
tarefas = []

def exibir_menu():
      print('--- Gerenciador de Tarefas ---\n')
      print('1. Adicionar tarefa'
            '\n2. Visualizar tarefas'
            '\n3. Remover tarefa'
            '\n4. Sair')
      
def voltar_ao_menu():
      input('\nPressione Enter para continuar...')
      main()  

def adicionar_tarefa():
      tarefa = input('Digite a tarefa que deseja adicionar: ')
      tarefas.append(tarefa)
      print(f'Tarefa "{tarefa}" adicionada com sucesso!')
      voltar_ao_menu()



def escolher_opção():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Opção escolhida: {opcao_escolhida}')
        if opcao_escolhida == 1:
            print('Adicionar tarefa')
            adicionar_tarefa()

        elif opcao_escolhida == 2:
            print('Visualizar tarefas')
            visualizar_tarefas()

        elif opcao_escolhida == 3:
            print('Remover tarefa')
            remover_tarefa()

        elif opcao_escolhida == 4:
            print('Saindo do gerenciador de tarefas. Até logo!')
            exit()

        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

    except ValueError:
        print('Erro: Por favor, digite um número válido.')

def main():
      while True:
            exibir_menu()
            escolher_opção()   

if __name__ == "__main__":
      main()