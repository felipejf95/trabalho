import pandas as pd 

# dataset
caminho_arquivo  = '/home/felipe/Documentos/VSCode/Segurança Redes/trabalho/UNSW_NB15_testing-set.csv'

# colunas de interesse
colunas_interessantes = ['dur', 'proto', 'service', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate',
                          'sttl', 'dttl', 'ct_srv_src', 'ct_srv_dst', 'ct_dst_ltm', 'is_ftp_login',
                          'attack_cat', 'label']

# leitura arquivo
dados = pd.read_csv(caminho_arquivo, usecols=colunas_interessantes)

# remoção linhas nulas
dados = dados.dropna()

print(dados.head())


