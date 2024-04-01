import pandas as pd

bases = ['pib.csv', 'fbkf_maq.csv', 'FBKF.csv', 'fbkf_constru.csv', 'PIB_comercio.csv', 'PIB_constucaocivil.csv', 'PIB_demanda_familias.csv', 'PIB_eletrico.csv', 'pib_exportacoes.csv', 'pib_importacoes.csv', 'PIB_ind_extrativa_mineral.csv', 'pib_ind_transformacao.csv', 'IGPM.csv', 'IPCA.csv']

#Vamos fazer a análise descritiva dos dados

#Extraímos os dados estatísticos mais elementares com .describe()
for i in bases:
    base = pd.read_csv(i, sep = ",")
    base = base.iloc[:, 1]
    print(base.describe())

base.plot(x = base.columns[0], y = base.columns[1])
plt.show()

df_final = pd.read_csv("base_tratada.csv")
