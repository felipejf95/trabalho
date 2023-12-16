import pandas as pd 

# url do dataset
dados_url = "https://raw.githubusercontent.com/felipejf95/trabalho/main/UNSW_NB15_testing-set.csv"


# colunas de interesse
colunas_interessantes = ['dur', 'proto', 'service', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate',
                          'sttl', 'dttl', 'ct_srv_src', 'ct_srv_dst', 'ct_dst_ltm', 'is_ftp_login',
                          'attack_cat', 'label']

# leitura arquivo
dados = pd.read_csv(dados_url, sep=",", usecols=colunas_interessantes)

# remoção linhas nulas
dados = dados.dropna()

print(dados.head())


