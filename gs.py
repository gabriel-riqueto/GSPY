'''
Gabriel Riqueto RM98685 
Lucas Vinicius de Almeida Brigida RM99094 
'''

import json
import os

def carregar_pacientes():
    if os.path.exists('pacientes.json'):
        with open('pacientes.json', 'r') as file:
            pacientes = json.load(file)
        return pacientes
    else:
        return []

def salvar_pacientes(pacientes):
    with open('pacientes.json', 'w') as file:
        json.dump(pacientes, file, indent=2)

def adicionar_paciente(pacientes):
    novo_id = obter_novo_id(pacientes)
    nome = input("Digite o nome do paciente: ")
    anotacoes = input("Digite as anotações sobre o paciente: ")
    print("----------")

    paciente = {
        'id': novo_id,
        'nome': nome,
        'anotacoes': anotacoes
    }

    pacientes.append(paciente)
    salvar_pacientes(pacientes)
    print(f"Paciente {novo_id} adicionado com sucesso!")
    print("----------")

def obter_novo_id(pacientes):
    if not pacientes:
        return "001"

    ids_existentes = [int(paciente['id']) for paciente in pacientes]
    novo_id = max(ids_existentes) + 1
    return f"{novo_id:03d}"

def mostrar_pacientes(pacientes):
    if not pacientes:
        print("Nenhum paciente registrado.")
        print("----------")
    else:
        print("Lista de Pacientes:")
        print("----------")
        for paciente in pacientes:
            print(f"ID: {paciente['id']}, Nome: {paciente['nome']}")

def mostrar_anotacoes(pacientes, paciente_id=None):
    if not pacientes:
        print("Nenhum paciente registrado.")
        print("----------")
        
    elif paciente_id is not None and paciente_id != 'T':
        paciente = encontrar_paciente(pacientes, paciente_id)
        if paciente:
            print(f"Anotações do Paciente {paciente['nome']} (ID: {paciente['id']}):")
            print(paciente['anotacoes'])
            print("----------")
        else:
            print("Paciente não encontrado.")
            print("----------")
    else:
        print("Anotações de Todos os Pacientes:")
        print("----------")
        for paciente in pacientes:
            print(f"\nID: {paciente['id']}, Nome: {paciente['nome']}")
            print(paciente['anotacoes'])


def modificar_anotacoes(pacientes, paciente_id):
    paciente = encontrar_paciente(pacientes, paciente_id)
    if paciente:
        print("----------")
        print(f"Anotações atuais do Paciente {paciente['nome']} (ID: {paciente['id']}):")
        print(paciente['anotacoes'])
        print("----------")

        opcao = input("Pressione A para adicionar anotações ou M para modificar as anotaçoes do zero: ").upper()

        if opcao == 'A':
            novas_anotacoes = input("Digite as novas anotações: ")
            paciente['anotacoes'] += '\n' + novas_anotacoes
        elif opcao == 'M':
            novas_anotacoes = input("Digite as novas anotações: ")
            paciente['anotacoes'] = novas_anotacoes
        else:
            print("Opção inválida. Nenhuma modificação realizada.")
            print("----------")

        salvar_pacientes(pacientes)
        print("Anotações modificadas com sucesso!")
        print("----------")
    else:
        print("Paciente não encontrado.")
        print("----------")
def excluir_paciente(pacientes, paciente_id):
    paciente = encontrar_paciente(pacientes, paciente_id)
    if paciente:
        pacientes.remove(paciente)
        salvar_pacientes(pacientes)
        print(f"Paciente {paciente_id} excluído com sucesso!")
        print("----------")
    else:
        print("Paciente não encontrado.")
        print("----------")

def encontrar_paciente(pacientes, paciente_id):
    for paciente in pacientes:
        if paciente['id'] == paciente_id:
            return paciente
    return None

def main():
    pacientes = carregar_pacientes()

    while True:
        print("\n")
        print("Sistema de Gerenciamento de Pacientes\n")
        print("1. Adicionar Paciente")
        print("2. Verificar Pacientes")
        print("3. Mostrar Anotações de Paciente")
        print("4. Modificar Anotações de Paciente")
        print("5. Excluir Paciente")
        print("6. Encerrar Programa")
        print("----------")

        escolha = input("Escolha uma opção (1-6): ")

        if escolha == '1':
            adicionar_paciente(pacientes)
        elif escolha == '2':
            mostrar_pacientes(pacientes)
        elif escolha == '3':
             paciente_id = input("Digite o ID do paciente ou 'T' para mostrar todos: ")
             mostrar_anotacoes(pacientes, paciente_id)
        elif escolha == '4':
            paciente_id = input("Digite o ID do paciente: ")
            modificar_anotacoes(pacientes, paciente_id)
        elif escolha == '5':
            paciente_id = input("Digite o ID do paciente que deseja excluir: ")
            excluir_paciente(pacientes, paciente_id)
        elif escolha == '6':
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            print("----------")

if __name__ == "__main__":
    main()
