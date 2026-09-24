import pandas as pd

def taxa_falha_por_tipo(df: pd.DataFrame) -> pd.DataFrame:
    resultado = df.groupby("Type")["Machine failure"].mean().reset_index()
    resultado.columns = ["tipo", "taxa_falha"]
    return resultado