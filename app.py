import os
import pandas as pd
from openpyxl.utils.exceptions import IllegalCharacterError
import re

# Função para remover caracteres não permitidos pelo Excel
def limpar_caracteres_invalidos(valor):
    if isinstance(valor, str):
        # Remove todos os caracteres de controle ASCII (menos os comuns como tab, nova linha)
        return re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', valor)
    return valor

# Define as pastas
pasta_entrada = 'entrada'
pasta_saida = 'saida'
nome_arquivo = 'vw_consultas_pep.csv'

# Garante que a pasta de saída existe
os.makedirs(pasta_saida, exist_ok=True)

# Caminhos completos
csv_path = os.path.join(pasta_entrada, nome_arquivo)
xlsx_nome = nome_arquivo.replace('.csv', '.xlsx')
xlsx_path = os.path.join(pasta_saida, xlsx_nome)

# Leitura do CSV com todos os dados como texto
df = pd.read_csv(csv_path, dtype=str, low_memory=False)

# Aplica a limpeza em todo o DataFrame
df = df.applymap(limpar_caracteres_invalidos)

# Salva o Excel
df.to_excel(xlsx_path, index=False, engine='openpyxl')

print('✅ Conversão concluída com sucesso!')
print(f'📥 Entrada: {csv_path}')
print(f'📤 Saída: {xlsx_path}')
