# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:59:44 2022

Auhtor: Damián E. Quijano A.
Orcid: https://orcid.org/0000-0002-1531-3902
email: damian.quijano@udelas.ac.pa

Panama Case

Generator of representative random samples.


"""

import pandas as pd

pais="PA"# NI:Nicaragua, PA: Panamá, CR: Costa Rica
carpeta='D:\\OperacionesTwitterArticuloSpyder\\Etapa4Analisis\\Datos\\'
print("Start")


df=pd.read_csv(carpeta+'classifiedUsersPA_D2.csv', sep=",",encoding='mbcs')


# Confidence level 95%, sampling error 5%, p=0.5,result =385 records. Quantitative values, for proportion.
dfrevueltos2=df.sample(frac=1,random_state=5).reset_index(drop=True)# Shuffle all the data
dfsample2=dfrevueltos2.sample(385,random_state=5)# randomly select 365 records
dfsample2.to_csv(carpeta+'sampleUsersPA_D2.csv',index=False)

print("Finished")
