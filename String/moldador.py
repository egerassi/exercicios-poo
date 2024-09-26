import pandas as pd

# Carrega a planilha
def carregar_planilha(caminho):
    return pd.read_excel(caminho)

# Formata a mensagem conforme o molde
def formatar_mensagem(dados):
    return f"""*Título:* {dados['Título']}
*Tipo:* {dados['Tipo']}
*Remuneração:* {dados['Remuneração']}
*Auxílio:* {dados['Auxílio']}
*Período:* {dados['Período']}
*Carga Horária:* {dados['Carga Horária']}
*Requisitos:* {dados['Requisitos']}
*Local:* {dados['Local']}
*Link:* {dados['Link']}
*Contato:* {dados['Contato']}
"""

def main():
    caminho = "C:\\Users\\egera\\Downloads\\Vagas copia.xlsx"
    planilha = carregar_planilha(caminho)
    
    # Supõe que as colunas estão nomeadas conforme o esperado no molde
    for index, row in planilha.iterrows():
        mensagem = formatar_mensagem({
            'Título': row['Título'],
            'Tipo': row['Tipo'],
            'Remuneração': row['Remuneração'],
            'Auxílio': row['Auxílio'],
            'Período': row['Período'],
            'Carga Horária': row['Carga Horária'],
            'Requisitos': row['Requisitos'],
            'Local': row['Local'],
            'Link': row['Link'],
            'Contato': row['Contato']
        })
        print(mensagem)

if __name__ == "__main__":
    main()