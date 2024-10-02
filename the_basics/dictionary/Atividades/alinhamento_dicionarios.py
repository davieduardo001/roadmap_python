# Dicionário Aninhado: Crie um dicionário aninhado que contenha informações sobre dois livros, incluindo título, autor e ano de publicação. Exiba o autor do primeiro livro.

livros = {
    'livro1': {
        'titulo': 'A volta dos q nn forão',
        'Paginas': '123',
        'Ano de Publicação': '1923'
    },

    'livro2': {
        'titulo': 'A volta dos q já forão',
        'Paginas': '1432',
        'Ano de Publicação': '1943'
    }
}

print(livros['livro1']['titulo'])