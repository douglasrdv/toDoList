from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {
        'id': 1,
        'titulo': 'Estudar Python',
        'status': 'Pendente'
    },
    {
        'id': 2,
        'titulo': 'Fazer exercícios de Flask',
        'status': 'Concluída'
    },
    {
        'id': 3,
        'titulo': 'Preparar apresentação',
        'status': 'Em andamento'
    },
]

# Consultar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    return jsonify(tarefas)

# Consultar tarefa por id
@app.route('/tarefas/<int:id>', methods=['GET'])
def obter_tarefa_por_id(id):
    for tarefa in tarefas:
        if tarefa.get('id') == id:
        	return jsonify(tarefa)

# Editar tarefa por id
@app.route('/tarefas/<int:id>', methods=['PUT'])
def editar_tarefa_por_id(id):
    tarefa_alterada = request.get_json()
    for indice, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            tarefas[indice].update(tarefa_alterada)
            return jsonify(tarefas[indice])

# Criar nova tarefa
@app.route('/tarefas', methods=['POST'])
def incluir_nova_tarefa():
    nova_tarefa = request.get_json()
    tarefas.append(nova_tarefa)
    return jsonify(tarefas)

# Excluir tarefa por id
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    for indice, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            del tarefas[indice]
    return jsonify(tarefas)

app.run(port=5000, host='localhost', debug=True)