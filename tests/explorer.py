from ingest.reader import carregar_dados_manutencao

df = carregar_dados_manutencao()
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df["Machine failure"].value_counts())