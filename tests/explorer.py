from ingest.reader import carregar_dados_manutencao
from transform.metrics import taxa_falha_por_tipo
from transform.metrics import causas_mais_comuns


df = carregar_dados_manutencao()
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df["falha_maquina"].value_counts())

print(taxa_falha_por_tipo(df))

print(causas_mais_comuns(df))
