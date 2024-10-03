import click

# Dicionário simples para armazenar as tarefas
tarefas = {}

@click.group()
def cli():
    """Sistema simples de cadastro de tarefas."""
    pass

@cli.command()
@click.argument('titulo')
@click.argument('descricao')
def adicionar(titulo, descricao):
    """Adiciona uma nova tarefa ao sistema."""
    id_tarefa = len(tarefas) + 1
    tarefas[id_tarefa] = {'titulo': titulo, 'descricao': descricao}
    click.echo(f"Tarefa '{titulo}' adicionada com sucesso!")

@cli.command()
def listar():
    """Lista todas as tarefas cadastradas."""
    if not tarefas:
        click.echo("Nenhuma tarefa cadastrada.")
    else:
        for id_tarefa, tarefa in tarefas.items():
            click.echo(f"{id_tarefa}: {tarefa['titulo']} - {tarefa['descricao']}")

@cli.command()
@click.argument('id_tarefa', type=int)
def remover(id_tarefa):
    """Remove uma tarefa pelo ID."""
    if id_tarefa in tarefas:
        tarefa = tarefas.pop(id_tarefa)
        click.echo(f"Tarefa '{tarefa['titulo']}' removida com sucesso!")
    else:
        click.echo("Tarefa não encontrada.")

if __name__ == "__main__":
    cli()
