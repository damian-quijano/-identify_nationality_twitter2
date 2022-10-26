# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 22:52:46 2022

Auhtor: Damián E. Quijano A.
Orcid: https://orcid.org/0000-0002-1531-3902
email: damian.quijano@udelas.ac.pa

Panama Case

It is divided into two parts.
-First part: Generates the module based on the characteristics and parameters of the best result that we have in the
resultsPA table (generated from randomTreeAnalysis.py) in the first row SELECT [num],[TN],[FP],[ FN],[TP],[cols],[best]
FROM resultsPA where FP=0 order by TP desc.

-The second part: applies the model to usersPA_D2.txt and generates the file classifiedUsersPA_D2.csv, which is the same as usersPA_D2
 but with three more columns: prob0, prob1 and pred.


"""

#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime as dt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV



pd.set_option('expand_frame_repr', False) # despliega todas las columnas
pd.set_option("display.max_rows",None)

pais="PA" # Panama Case

# *********************Segmento 1. Carga del conjunto de datos
dsUsuarios = pd.read_csv('D:\\OperacionesTwitterArticuloSpyder\\Etapa4Analisis\Datos\\sampleUsersPA_D2.csv')

# Below all the features that a model can use
#["author_id","username","created_at","verified",
# "followers","following","tweet_count","listed_count",
# "cant_tweets_muestra","rt","vreplicas","likes","rtquotes",
# "menciones_a_In","menciones_a_Out","menciones_de_In",
# "rt_a_In","rt_a_Out","rt_de_In",
# "rp_a_In","rp_a_Out","rp_de_In",
# "rq_a_In","rq_a_Out","rq_de_In",
# "Actividad","paisSN"]

columnas=["author_id","username","created_at","verified",
         "followers","following","tweet_count","listed_count",
          "cant_tweets_muestra","rt","vreplicas","likes","rtquotes",
          "Actividad",
          "menciones_a_In","menciones_a_Out","menciones_de_In",
          "rt_a_In","rt_a_Out","rt_de_In",
          "rp_a_In","rp_a_Out","rp_de_In",
          "rq_a_Out"
          ]
    
        

dsUsuariosRecortado= dsUsuarios.drop(columns= columnas, axis=1)
datos=dsUsuariosRecortado

# País it means Country in english

cad="datos.drop(columns = 'paisSN'),datos['paisSN'],test_size=0.20,random_state = 123"
X_train, X_test, y_train, y_test = train_test_split(
                                    datos.drop(columns = 'paisSN'),
                                    datos['paisSN'],
                                    test_size=0.20,
                                    random_state = 123,
                                    #stratify=datos['paisSN']
                                )
#{'n_estimators': [10], 'criterion': ['gini'], 'class_weight': ['balanced_subsample']}
param_grid = {'n_estimators': [10],
         
          'criterion'   : ['entropy'] ,#['gini','entropy']
          'class_weight' :['balanced_subsample']# ['balanced','balanced_subsample'],default=None
          }

#GridSearchCV(estimator=RandomForestClassifier(random_state=123),n_jobs=-1,param_grid={'class_weight':['balanced_subsample'],'criterion':['gini'],'n_estimators':[10]})
grid = GridSearchCV(
        estimator  = RandomForestClassifier(random_state = 123),
        param_grid = param_grid,
        n_jobs=-1,
        refit=True,
        return_train_score = True
        )

grid.fit(X = X_train, y = y_train)

   
modelo_final = grid.best_estimator_


predicciones = modelo_final.predict(X = X_test)
predicciones_prob = modelo_final.predict_proba(X = X_test)


dfresult = pd.DataFrame(list(zip(y_test,predicciones,predicciones_prob[:,0],predicciones_prob[:,1])), columns = ['y_test','y_Pred','prob0','prob1'])


mat_confusion = confusion_matrix(
                    y_true    = y_test,
                    y_pred    = predicciones
                )

precision = precision_score(
            y_true    = y_test,
            y_pred    = predicciones
            #normalize = True
           )
print("Confusion matrix")
print("-------------------")
print(mat_confusion)
print("")
print(f"The test precision is: {100 * precision} %")


# The model is then applied to all the data.
dsUsuariosCompleto = pd.read_csv('D:\\OperacionesTwitterArticuloSpyder\\Etapa4Analisis\Datos\\UsersPA_D2.txt')
dsUsuariosCompletoRecortado= dsUsuariosCompleto.drop(columns= columnas, axis=1)

prediccionesCompleto = modelo_final.predict(X = dsUsuariosCompletoRecortado)
prediccionesCompleto_prob = modelo_final.predict_proba(X = dsUsuariosCompletoRecortado)

dsUsuariosClasificado=dsUsuariosCompleto.copy()
dsUsuariosClasificado['pred']=prediccionesCompleto
dsUsuariosClasificado['prob0']=prediccionesCompleto_prob[:,0]
dsUsuariosClasificado['prob1']=prediccionesCompleto_prob[:,1]

dsUsuariosClasificado.to_csv('D:\\OperacionesTwitterArticuloSpyder\\Etapa4Analisis\Datos\\classifiedUsersPA_D2.csv')



















