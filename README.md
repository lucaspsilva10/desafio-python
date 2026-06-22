# Desafio Python

Projeto desenvolvido em Python que lê três contatos cadastrados no Supabase e envia mensagens pelo WhatsApp usando Z-API.

## Tecnologias
- Python
- Supabase
- Z-API
- python-dotenv
- requests

## Passo a passo para a execução da aplicação
## 1- Clonar o repositório 

Clone o repositório ou baixe o arquivo .zip, caso baixe o arquivo .zip, descompacte o arquivo e com um compilador da sua preferência abra a pasta desafio-python.

---

## 2- Crie o arquivo `.env`
Dentro da pasta desafio-python crie o arquivo .env e cole as seguintes variáveis de ambiente:
    
    SUPABASE_URL=
    SUPABASE_KEY=

    ZAPI_INSTANCE_ID=
    ZAPI_INSTANCE_TOKEN=
    ZAPI_CLIENT_TOKEN=

---

## 3- Configurar as variáveis de ambiente
Preencha as variáveis com os dados do seu projeto Supabase e da sua instância Z-API.

---

## 4- Instalar as dependências
Instale as dependências usando o comando:

    pip install -r requirements.txt

---

## 5- Criar a tabela no Supabase
No SQL Editor do Supabase, execute a seguinte query:

    create table contatos (
        id bigint primary key generated always as identity,
        nome text not null,
        telefone text not null,
        ativo boolean default true,
        created_at timestamp with time zone default now()
    );

---

## 6- Inserir registros para teste
Insira alguns clientes na tabela usando o comando abaixo:

    insert into contatos (nome, telefone) values
    ('Lucas', '5511999999999'),
    ('Maria', '5511888888888'),
    ('Lucia', '5511777777777');

---

## 7- Executar a aplicação
Após concluir todas as etapas anteriores, execute o projeto através do terminal:

    python main.py

Também é possível executar o arquivo main.py diretamente pela sua IDE.
