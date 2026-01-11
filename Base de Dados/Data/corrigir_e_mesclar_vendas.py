import pandas as pd
import os

# Caminho da pasta onde estão os CSVs
# pasta = "C:/users/jaime/documentos/trabalho/projetos/obuc/Base de Dados/sales"
pasta = os.path.dirname(os.path.abspath(__file__))

# Lista para armazenar os DataFrames
dfs = []

# Arquivos de vendas
arquivos = [
    "Sales2017.csv",
    "Sales2018.csv",
    "Sales2019.csv",
    "Sales2020.csv"
]

for arquivo in arquivos:
    caminho = os.path.join(pasta, arquivo)
    
    df = pd.read_csv(
        caminho,
        sep=",",        # separador de colunas
        decimal=".",    # separador decimal correto
        encoding="utf-8"
    )
    
    # (opcional) Criar coluna de ano
    df["Sales Year"] = arquivo[-8:-4]
    
    dfs.append(df)

# Mesclar todos os anos
df_final = pd.concat(dfs, ignore_index=True)

# Exportar CSV final no padrão brasileiro
saida = os.path.join(pasta, "Sales.csv")

df_final.to_csv(
    saida,
    sep=";",        # padrão Power BI pt-BR
    decimal=",",    # padrão Power BI pt-BR
    index=False,
    encoding="utf-8"
)

print("Arquivo gerado com sucesso:", saida)
