import requests

base_url = 'http://localhost:5000/contatos'

def criar_contato(nome, telefone, email):
    novo_contato = {'nome': nome, 'telefone': telefone, 'email': email}
    response = requests.post(base_url, json=novo_contato)
    
    if response.status_code == 201:
        print('Contato criado com sucesso!\n')
    else:
        print(f'Erro ao criar o contato. Status code: {response.status_code}')

def listar_contatos():
    response = requests.get(base_url)
    
    if response.status_code == 200:
        contatos = response.json().get('contatos', [])
        if contatos:
            print('Lista de Contatos:\n')
            for contato in contatos:
                print(f"ID: {contato['id']}, Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
        else:
            print('Nenhum contato encontrado.')
    else:
        print(f'Erro ao obter a lista de contatos. Status code: {response.status_code}')

def atualizar_contato(contato_id, nome, telefone, email):
    contato_atualizado = {'nome': nome, 'telefone': telefone, 'email': email}
    response = requests.put(f'{base_url}/{contato_id}', json=contato_atualizado)
    
    if response.status_code == 200:
        print('Contato atualizado com sucesso!\n')
    elif response.status_code == 404:
        print('Contato não encontrado.')
    else:
        print(f'Erro ao atualizar o contato. Status code: {response.status_code}')

def excluir_contato(contato_id):
    response = requests.delete(f'{base_url}/{contato_id}')
    
    if response.status_code == 200:
        print('Contato excluído com sucesso!\n')
    elif response.status_code == 404:
        print('Contato não encontrado.')
    else:
        print(f'Erro ao excluir o contato. Status code: {response.status_code}')


criar_contato('Luana', '123456789', 'luana@email.com')
criar_contato('Maria', '987654321', 'maria@email.com')
listar_contatos()


atualizar_contato(1, 'Luana Silva', '123456789', 'luana.silva@email.com')
listar_contatos()

excluir_contato(1)
listar_contatos()
