import pandas as pd
from rich.console import Console

def carregar_planilha(caminho):
    return pd.read_excel(caminho)

def formatar_mensagem(console, dados):
    console.print(f"[bold]Título:[/bold] {dados['Título']}", style="bold yellow")
    console.print(f"[bold]Tipo:[/bold] {dados['Tipo']}", style="bold green")
    console.print(f"[bold]Remuneração:[/bold] {dados['Remuneração']}", style="bold red")
    console.print(f"[bold]Auxílio:[/bold] {dados['Auxílio']}", style="bold blue")
    console.print(f"[bold]Período:[/bold] {dados['Período']}", style="bold magenta")
    console.print(f"[bold]Carga Horária:[/bold] {dados['Carga Horária']}", style="bold cyan")
    console.print(f"[bold]Requisitos:[/bold] {dados['Requisitos']}", style="bold white")
    console.print(f"[bold]Local:[/bold] {dados['Local']}", style="bold green")
    if dados['Link'].startswith("http"):
        console.print(f"[link={dados['Link']}]Link[/link]", style="link")
    else:
        console.print("[bold]Link:[/bold] No link provided")
    if dados['Contato'].startswith("http"):
        console.print(f"[link={dados['Contato']}]Contato[/link]", style="link")
    else:
        console.print("[bold]Contato:[/bold] No contact link provided")

def main():
    caminho = r"C:\Users\egera\Downloads\Lista de Vagas.xlsx"  # Ajuste o caminho para o seu arquivo
    planilha = carregar_planilha(caminho)
    console = Console()
    
    for index, row in planilha.iterrows():
        console.print(f"\n[bold underline]Vaga {index+1}[/bold underline]")
        formatar_mensagem(console, row)

if __name__ == "__main__":
    main()
