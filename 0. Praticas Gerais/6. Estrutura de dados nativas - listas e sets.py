"""
6. Estrutura de dados nativas – Listas e sets
Desenvolva um programa que trabalhe com listas e sets para armazenar nomes de alunos em uma turma. Realize operações como adição, remoção e verificação de existência de um nome na lista.
"""
def main():

    def adicionar_aluno(alunos, nome):
        if nome not in alunos:
            alunos.append(nome)
            print(f'Alunos {nome} adicionadoc com sucesso.')
        else:
            print(f'Aluno consta no sistema.')

    def remover_aluno(alunos, nome):
        if nome in alunos:
            alunos.remove(nome)
            print(f'Aluno {nome} está sendo removido.')
        else:
            print(f'Aluno {nome} não encontrado.')

    def verificar_aluno(alunos, nome):
        if nome in alunos:
            print(f'Aluno {nome} verificado.')
        else:
            print(f'Aluno {nome} não encontrado.')

    def listar_aluno(alunos):
        if alunos:
            print('Lista de alunos na turma: ')
            for alunos in alunos:
                print(aluno)
            else:
                print('Turma está vazia.')
    def menu():
        alunos = [] #Lista pra armazenar os alunos

        while True:
            print('\nMenu:')
            print('1. Adicionar Aluno')
            print('2. Remover Aluno')
            print('3. Verificar Aluno')
            print('4. Listar Alunos')
            print('5. Sair')

            Opcao = input('Escolha a opção: ')

            if Opcao == '1':
                nome = input('Digite o nome do aluno a ser adicionado: ')
                adicionar_aluno(alunos, nome)
            elif Opcao == '2':
                nome = input('Digite o nome a ser removido: ')
                remover_aluno(alunos, nome)
            elif Opcao == '3':
                nome = input('Digite o nome a ser verificado: ')
                verificar_aluno(alunos, nome)
            elif Opcao == '4':
                turma.listar_aluno()
                break
            else:
                print('Opção inválida. Tente novamente.')
    menu()

if __name__ == '__main__':
    main()