## Guia de Uso da API com Postman

Este guia fornecerá instruções passo a passo sobre como clonar o código do Git, configurar um ambiente virtual, e usar a API Flask resultante através do Postman para realizar operações CRUD (Create, Read, Update, Delete) em tarefas.

### Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em seu ambiente:

1. [Git](https://git-scm.com/)
2. [Python](https://www.python.org/downloads/)
3. [Postman](https://www.postman.com/)

### Clonando o Repositório do Git

1. Abra o terminal.

2. Navegue até o diretório onde você deseja clonar o repositório usando o comando `cd`:

    ```bash
    cd caminho/do/seu/diretorio
    ```

3. Clone o repositório executando o seguinte comando:

    ```bash
    git clone https://github.com/Douglas-DRS/toDoList
    ```
4. Após o clone, entre no diretório do projeto:

    ```bash
    cd nome-do-repositorio
    ```

### Configurando o Ambiente Virtual e Instalando Dependências

1. Crie um ambiente virtual para o projeto (certifique-se de estar no diretório do projeto):

    ```bash
    python3 -m venv venv
    ```

2. Ative o ambiente virtual:

    - No Windows:

        ```bash
        venv\Scripts\activate
        ```

    - No MacOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação Flask

1. Certifique-se de que o ambiente virtual está ativado.

2. Execute a aplicação Flask:

    ```bash
    python3 nome-do-arquivo.py
    ```

    Isso iniciará o servidor Flask na porta 5000.

### Testando a API com Postman

1. Abra o Postman.

2. Crie uma nova solicitação:

    - Método: **GET**
    - URL: `http://localhost:5000/tarefas`

3. Envie a solicitação e verifique se você recebe a lista de tarefas como resposta.

4. Experimente outras operações CRUD (POST, PUT, DELETE) usando endpoints como `http://localhost:5000/tarefas/<id>`.

    Certifique-se de ajustar o corpo da solicitação de acordo com o formato esperado pelo servidor.