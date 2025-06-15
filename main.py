import config
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def menu_principal():
    console.clear()
    console.print("""[green bold]
    __  ____   ____  ____   ______   ___    ____  ____    ____  _____  ____   ____ 
   /  ]|    \ |    ||    \ |      | /   \  /    ||    \  /    ||     ||    | /    |
  /  / |  D  ) |  | |  o  )|      ||     ||   __||  D  )|  o  ||   __| |  | |  o  |
 /  /  |    /  |  | |   _/ |_|  |_||  O  ||  |  ||    / |     ||  |_   |  | |     |
/   \_ |    \  |  | |  |     |  |  |     ||  |_ ||    \ |  _  ||   _]  |  | |  _  |
\     ||  .  \ |  | |  |     |  |  |     ||     ||  .  \|  |  ||  |    |  | |  |  |
 \____||__|\_||____||__|     |__|   \___/ |___,_||__|\_||__|__||__|   |____||__|__|
[/]          
  By: Brun0dutra :)                                                                                 
""")
    console.print(Panel("[bold blue]MENU PRINCIPAL[/]", expand=False))
    console.print("[1] [green]Criptografar Mensagem[/]")
    console.print('[2] [green]Descriptografar[/]')
    console.print('[3] [green]Sair[/]')
    print('')
    escolha = Prompt.ask("[bold yellow]Escolha uma opção[/bold yellow]", choices=["1", "2", "3"], show_choices=False)

    if escolha == "1":
        opcao_um()
    elif escolha == "2":
        opcao_dois()
    elif escolha == "3":
        console.print("[bold red]Saindo...[/bold red]")
        exit()
    else:
        console.print("Por Favor, Escolha uma das opções !")

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

    try:
        msgoriginal = config.descriptografar_mensagem(msg,chave)
    except:
        console.print('[red bold]Chave de acesso INCORRETA. ACESSO NEGADO ![/]')
        input('Aperte ENTER para continuar')
        menu_principal()    

    console.clear()
    console.print(Panel(msgoriginal, style='bold blue', expand=False, border_style='green'))
    console.input('[yellow bold]Aperter ENTER para continuar[/]')
    menu_principal()

if __name__ == "__main__":
    menu_principal()