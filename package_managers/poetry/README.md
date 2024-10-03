# Guia de Uso do Poetry

## Índice

1. [Introdução ao Poetry](#1-introdução-ao-poetry)
2. [Instalação do Poetry](#2-instalação-do-poetry)
3. [Inicializando um Novo Projeto](#3-inicializando-um-novo-projeto)
4. [Gerenciando Dependências](#4-gerenciando-dependências)
   - [Adicionar Dependências](#41-adicionar-dependências)
   - [Remover Dependências](#42-remover-dependências)
   - [Especificando Versões](#43-especificando-versões)
5. [Ambientes Virtuais](#5-ambientes-virtuais)
   - [Gerenciamento Automático](#51-gerenciamento-automático)
   - [Ativando o Ambiente Virtual](#52-ativando-o-ambiente-virtual)
6. [Executando Scripts e Testes](#6-executando-scripts-e-testes)
7. [Publicando o Projeto](#7-publicando-o-projeto)
8. [Comandos Comuns do Poetry](#8-comandos-comuns-do-poetry)

---

## 1. Introdução ao Poetry

**Poetry** é uma ferramenta de gerenciamento de dependências e pacotes para projetos Python. Ele facilita a criação de ambientes isolados, a instalação de pacotes, e também oferece um fluxo de trabalho simples para publicar bibliotecas.

**Principais características**:
- Gerenciamento de dependências sem precisar de arquivos separados (`requirements.txt` e `setup.py`).
- Criação e controle de ambientes virtuais automáticos.
- Publicação de pacotes no PyPI com comandos simples.
- Arquivo de configuração centralizado (`pyproject.toml`) para dependências e configurações.

---

## 2. Instalação do Poetry

A instalação do Poetry pode ser feita diretamente via script oficial. Execute o seguinte comando:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Após a instalação, adicione o Poetry ao seu `PATH` (se necessário), e verifique se foi instalado corretamente:

```bash
poetry --version
```

---

## 3. Inicializando um Novo Projeto

Para começar um novo projeto com Poetry, use o comando:

```bash
poetry new nome-do-projeto
```

Isso cria uma estrutura de pastas com a seguinte organização:

```
nome-do-projeto/
├── pyproject.toml
├── README.rst
├── nome_do_projeto
│   └── __init__.py
└── tests
    └── __init__.py
```

Se você já tem um projeto existente e quer apenas adicionar o Poetry, use:

```bash
poetry init
```

O comando interativo irá guiar você para configurar dependências e o arquivo `pyproject.toml`.

---

## 4. Gerenciando Dependências

### 4.1. Adicionar Dependências

Para adicionar uma dependência ao projeto, utilize o comando:

```bash
poetry add nome-da-dependencia
```

Isso instalará a dependência e a registrará automaticamente no arquivo `pyproject.toml`.

Exemplo:

```bash
poetry add requests
```

Para adicionar dependências apenas para desenvolvimento (por exemplo, pacotes para testes), use a flag `--dev`:

```bash
poetry add pytest --dev
```

### 4.2. Remover Dependências

Para remover uma dependência, use o seguinte comando:

```bash
poetry remove nome-da-dependencia
```

Isso removerá a dependência do projeto e a eliminará do `pyproject.toml`.

### 4.3. Especificando Versões

Você pode especificar a versão de uma dependência diretamente:

```bash
poetry add requests@^2.25
```

Isso adiciona a versão `2.25` ou superior, desde que seja compatível com a API da versão `2.x`.

---

## 5. Ambientes Virtuais

Por padrão, o Poetry gerencia automaticamente ambientes virtuais para isolar dependências entre projetos. Quando você executa o comando `poetry install`, ele cria e ativa um ambiente virtual automaticamente.

### 5.1. Gerenciamento Automático

O ambiente virtual é criado automaticamente na primeira instalação de dependências:

```bash
poetry install
```

Este comando cria o ambiente virtual e instala todas as dependências listadas no `pyproject.toml`.

### 5.2. Ativando o Ambiente Virtual

Se o ambiente virtual não for ativado automaticamente, você pode forçar sua ativação:

```bash
poetry shell
```

Para sair do ambiente virtual, simplesmente use o comando `exit`.

---

## 6. Executando Scripts e Testes

Você pode executar scripts Python dentro do ambiente virtual gerenciado pelo Poetry usando o comando `run`:

```bash
poetry run python script.py
```

Isso garante que o script seja executado com as dependências corretas do projeto.

Para rodar testes (assumindo que o `pytest` esteja instalado como dependência de desenvolvimento), execute:

```bash
poetry run pytest
```

---

## 7. Publicando o Projeto

Se você estiver desenvolvendo uma biblioteca e quiser publicá-la no PyPI, o Poetry simplifica esse processo.

1. Autentique-se no PyPI (ou PyPI Test) com:

   ```bash
   poetry config pypi-token.pypi SEU_TOKEN_AQUI
   ```

2. Gere o arquivo de distribuição:

   ```bash
   poetry build
   ```

3. Publique o pacote:

   ```bash
   poetry publish
   ```

---

## 8. Comandos Comuns do Poetry

Aqui estão alguns comandos comuns do Poetry para referência rápida:

- **Criar um novo projeto**: `poetry new nome-do-projeto`
- **Instalar dependências**: `poetry install`
- **Adicionar dependências**: `poetry add nome-da-dependencia`
- **Remover dependências**: `poetry remove nome-da-dependencia`
- **Iniciar um shell no ambiente virtual**: `poetry shell`
- **Rodar um script no ambiente virtual**: `poetry run python script.py`
- **Atualizar dependências**: `poetry update`
- **Publicar um pacote**: `poetry publish`
- **Verificar a versão do Poetry**: `poetry --version`