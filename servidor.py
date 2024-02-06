from flask import Flask, request, jsonify

app = Flask(__name__)

agenda = []
proximo_id = 1


@app.route('/contatos', methods=['POST'])
def criar_contato():
    global proximo_id
    novo_contato = request.json
    novo_contato['id'] = proximo_id
    proximo_id += 1
    agenda.append(novo_contato)
    return jsonify({'mensagem': 'Contato criado com sucesso!\n'}), 201


@app.route('/contatos', methods=['GET'])
def listar_contatos():
    return jsonify({'contatos': agenda})


@app.route('/contatos/<int:contato_id>', methods=['PUT'])
def atualizar_contato(contato_id):
    contato_atualizado = request.json
    for contato in agenda:
        if contato['id'] == contato_id:
            contato.update(contato_atualizado)
            return jsonify({'mensagem': 'Contato atualizado com sucesso!\n'})
    return jsonify({'erro': 'Contato não encontrado'}), 404


@app.route('/contatos/<int:contato_id>', methods=['DELETE'])
def excluir_contato(contato_id):
    for contato in agenda:
        if contato['id'] == contato_id:
            agenda.remove(contato)
            return jsonify({'mensagem': 'Contato excluído com sucesso!\n'})
    return jsonify({'erro': 'Contato não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
