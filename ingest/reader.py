import pandas as pd

MAPEAMENTO_COLUNAS = {
    "UDI": "id",
    "Product ID": "id_produto",
    "Type": "tipo_qualidade",
    "Air temperature [K]": "temp_ar_k",
    "Process temperature [K]": "temp_processo_k",
    "Rotational speed [rpm]": "velocidade_rpm",
    "Torque [Nm]": "torque_nm",
    "Tool wear [min]": "desgaste_ferramenta_min",
    "Machine failure": "falha_maquina",
    "TWF": "falha_desgaste_ferramenta",
    "HDF": "falha_dissipacao_calor",
    "PWF": "falha_energia",
    "OSF": "falha_sobrecarga",
    "RNF": "falha_aleatoria"
}

def carregar_dados_manutencao(filepath: str = "data/dados.csv") -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df = df.rename(columns=MAPEAMENTO_COLUNAS)
    return df
