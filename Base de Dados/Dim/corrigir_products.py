import pandas as pd
import os

# Pasta onde o script está localizado (dim)
pasta = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo Products
arquivo_entrada = os.path.join(pasta, "Products.csv")

# Leitura correta do CSV (decimal com ponto)
df = pd.read_csv(
    arquivo_entrada,
    sep=",",
    decimal=".",
    encoding="utf-8"
)

# Campos que estavam perdendo casas decimais
campos_numericos = ["Weight", "Unit Cost", "Unit Price"]

for campo in campos_numericos:
    df[campo] = pd.to_numeric(df[campo], errors="coerce")

# Exportar CSV corrigido
arquivo_saida = os.path.join(pasta, "Products_ok.csv")

df.to_csv(
    arquivo_saida,
    sep=";",
    decimal=",",
    index=False,
    encoding="utf-8"
)

print("Products corrigido com sucesso:")
print(arquivo_saida)