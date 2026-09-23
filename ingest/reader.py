import pandas as pd

def carregar_dados_manutencao(filepath: str = "data/dados.csv") -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df
