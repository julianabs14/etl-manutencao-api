from ingest.reader import carregar_dados_manutencao

df = carregar_dados_manutencao()
print(df.shape)
print(df.head())