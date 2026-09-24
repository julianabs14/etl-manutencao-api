from ingest.reader import carregar_dados_manutencao
from transform.metrics import taxa_falha_por_tipo

df = carregar_dados_manutencao()
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df["Machine failure"].value_counts())

print(taxa_falha_por_tipo(df))
