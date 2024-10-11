import config
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def menu_principal():
    console.clear()
    console.print(Panel("[bold blue]MENU PRINCIPAL[/]", expand=False))
    console.print("[1] [green]Criptografar Mensagem[/]")
    console.print('[2] [green]Descriptografar[/]')
    console.print('[3] [green]Sair[/]')
    
    escolha = Prompt.ask("[bold yellow]Escolha uma opção[/bold yellow]", choices=["1", "2", "3"], show_choices=False)

    if escolha == "1":
        opcao_um()
    elif escolha == "2":
        opcao_dois()
    elif escolha == "6":
        console.print("[bold red]Saindo...[/bold red]")
        exit()

def opcao_um():
    console.clear()
    msg = str(input('Mensagem: '))
    chave = str(input('Chave: '))
    msgcripto = config.criptografar_mensagem(msg,chave)
    print(msgcripto)
    console.input('[yellow bold]Aperter ENTER para continuar[/]')
    menu_principal()

def opcao_dois():
    console.clear()
    msg = str(input('Mensagem: '))
    chave = str(input('Chave: '))
    msgoriginal = config.descriptografar_mensagem(msg,chave)
    console.clear()
    console.print(msgoriginal, style='bold blue')
    console.input('[yellow bold]Aperter ENTER para continuar[/]')
    menu_principal()

if __name__ == "__main__":
    menu_principal()