from flask import Flask, jsonify, request, abort

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
def obter_tarefa_por_id_util(id):
    tarefa = next((t for t in tarefas if t.get('id') == id), None)
    return tarefa

# Obtenção de tarefa por ID.
@app.route('/tarefas/<int:id>', methods=['GET'])
def obter_tarefa_por_id(id):
    tarefa = obter_tarefa_por_id_util(id)
    if tarefa:
        return jsonify(tarefa)
    else:
        abort(404, description="Tarefa não encontrada")
    
# Editar tarefa por id
@app.route('/tarefas/<int:id>', methods=['PUT'])
def editar_tarefa_por_id(id):
    tarefa_alterada = request.get_json()
    for indice, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            tarefas[indice].update(tarefa_alterada)
            return jsonify(tarefas[indice])
        
#Validação de dados para tarefas
def validar_tarefa(dados):
    if 'titulo' not in dados or 'status' not in dados:
        abort(400, description="Campos 'titulo' e 'status' são obrigatórios.")
    if not isinstance(dados['titulo'], str) or not isinstance(dados['status'], str):
        abort(400, description="Campos 'titulo' e 'status' devem ser strings.")

# Criar nova tarefa
@app.route('/tarefas', methods=['POST'])
def incluir_nova_tarefa():
    nova_tarefa = request.get_json()
    validar_tarefa(nova_tarefa)
    tarefas.append(nova_tarefa)
    return jsonify(tarefas)

# Excluir tarefa por id
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa_por_id(id):
    for indice, tarefa in enumerate(tarefas):
        if tarefa.get('id') == id:
            del tarefas[indice]
            return jsonify(tarefas)

app.run(port=5000, host='localhost', debug=True)