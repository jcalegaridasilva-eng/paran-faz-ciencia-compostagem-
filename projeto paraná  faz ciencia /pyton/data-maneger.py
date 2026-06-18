import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

DB_PATH = 'instance/database.sqlite'

def exportar_para_excel():
    """ Lê o banco SQLite e exporta os dados de compostagem para .xlsx """
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM compostagem", conn)
        
        caminho_arquivo = 'relatorio_compostagem.xlsx'
        df.to_excel(caminho_arquivo, index=False, engine='openpyxl')
        print(f"Relatório exportado com sucesso para {caminho_arquivo}")
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao exportar: {e}")
        return False

def gerar_grafico_residuos():
    """ Gera um gráfico usando Matplotlib e salva como imagem """
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT tipo_residuo, peso_kg FROM compostagem", conn)
    conn.close()

    if not df.empty:
        # Agrupa por tipo de resíduo e soma o peso
        df_agrupado = df.groupby('tipo_residuo')['peso_kg'].sum()
        
        plt.figure(figsize=(8, 6))
        # Cores baseadas na identidade visual
        cores = ['#2E7D32', '#81C784', '#FBC02D', '#8D6E63'] 
        df_agrupado.plot(kind='bar', color=cores)
        plt.title('Total de Resíduos Processados por Tipo (kg)')
        plt.xlabel('Tipo de Resíduo')
        plt.ylabel('Peso (kg)')
        plt.tight_layout()
        plt.savefig('static/img/grafico_residuos.png')