import os
import pandas as pd
os.chdir("C:\\Users\\megal\\Desktop\\KeysData\\TestJoinsPython")
tax = pd.read_csv('taxonomic_data.csv')
obs = pd.read_csv('fk2018.csv')

new = pd.merge(obs, tax, on='SPECIES_CD', how='left')
new2 = pd.DataFrame(new)
columns = ['LEN', 'NUM', 'LC', 'LM', 'WLEN_A','WLEN_B']
new2.drop(columns, axis=1, inplace=True)

new2.to_csv('FK2018Final.csv')