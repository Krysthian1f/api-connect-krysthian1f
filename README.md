# API Connect

## Descrição

A API Connect é uma API REST desenvolvida em Python utilizando Flask. O projeto tem como objetivo realizar o gerenciamento de usuários através das operações CRUD (Create, Read, Update e Delete).

## Tecnologias Utilizadas

- Python
- Flask
- JSON
- Git
- GitHub
- Thunder Client

## Execução do Projeto

1. Clone o repositório:

```bash
git clone https://github.com/Krysthian1f/api-connect-krysthian1f.git
```

2. Acesse a pasta:

```bash
cd api-connect-krysthian1f
```

3. Crie o ambiente virtual:

```bash
python -m venv venv
```

4. Ative o ambiente:

```bash
venv\Scripts\activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

6. Execute a API:

```bash
python app.py
```

## Endpoints

### Listar usuários
GET /usuarios

### Buscar usuário por ID
GET /usuarios/{id}

### Cadastrar usuário
POST /usuarios

### Atualizar usuário
PUT /usuarios/{id}

### Remover usuário
DELETE /usuarios/{id}

## Autor

Krysthian Felipe
