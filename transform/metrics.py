import pandas as pd

def taxa_falha_por_tipo(df: pd.DataFrame) -> pd.DataFrame:
    resultado = df.groupby("tipo_qualidade")["falha_maquina"].mean().reset_index()
    resultado.columns = ["tipo", "taxa_falha"]
    return resultado

def causas_mais_comuns(df: pd.DataFrame) -> pd.DataFrame:
    causas = ["falha_desgaste_ferramenta", "falha_dissipacao_calor", "falha_energia", "falha_sobrecarga", "falha_aleatoria"]
    return df[causas].sum().sort_values(ascending=False)