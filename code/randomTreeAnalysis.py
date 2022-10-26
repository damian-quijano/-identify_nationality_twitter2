# -*- coding: utf-8 -*-
"""
Auhtor: Damián E. Quijano A.
Orcid: https://orcid.org/0000-0002-1531-3902
email: damian.quijano@udelas.ac.pa
"""

import pandas as pd
import numpy as np
from datetime import datetime as dt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import sys
import warnings
warnings.filterwarnings("ignore")

pd.set_option('expand_frame_repr', False) 
pd.set_option("display.max_rows",None)
# Panama will be processed
pais="PA" # NI:Nicaragua, PA: Panamá, CR: Costa Rica



# CONSTRUCTION OF ACTIONS 4096

# mentions
menciones=[
        ["","",""],
        ["","menciones_a_Out",""],
        ["","menciones_a_Out","menciones_de_In"],
        ["","","menciones_de_In"],
        ["menciones_a_In","",""],
        ["menciones_a_In","","menciones_de_In"],
        ["menciones_a_In","menciones_a_Out",""],
        ["menciones_a_In","menciones_a_Out","menciones_de_In"]
    
    ]

retweets=[
        ["","",""],
        ["","rt_a_Out",""],
        ["","rt_a_Out","rt_de_In"],
        ["","","rt_de_In"],
        ["rt_a_In","",""],
        ["rt_a_In","","rt_de_In"],
        ["rt_a_In","rt_a_Out",""],
        ["rt_a_In","rt_a_Out","rt_de_In"]
    
    ]

replicas=[
        ["","",""],
        ["","rp_a_Out",""],
        ["","rp_a_Out","rp_de_In"],
        ["","","rp_de_In"],
        ["rp_a_In","",""],
        ["rp_a_In","","rp_de_In"],
        ["rp_a_In","rp_a_Out",""],
        ["rp_a_In","rp_a_Out","rp_de_In"]
    
    ]

rquotes=[
        ["","",""],
        ["","rq_a_Out",""],
        ["","rq_a_Out","rq_de_In"],
        ["","","rq_de_In"],
        ["rq_a_In","",""],
        ["rq_a_In","","rq_de_In"],
        ["rq_a_In","rq_a_Out",""],
        ["rq_a_In","rq_a_Out","rq_de_In"]
    
    ]


cadmenciones=""
cadrt=""
cadrp=""
cadrq=""
lista=[]
cont=0
cada1000=0
for m in menciones:
    cadmenciones=""
    if m[0]!="":
        cadmenciones=cadmenciones+m[0]+","
        
    if m[1]!="":
        cadmenciones=cadmenciones+m[1]+","
       
    if m[2]!="":
        cadmenciones=cadmenciones+m[2]+","
        
   
    for rt in retweets:
        cadrt=cadmenciones
        if rt[0]!="":
            cadrt=cadrt+rt[0]+","
        if rt[1]!="":
            cadrt=cadrt+rt[1]+","
        if rt[2]!="":
            cadrt=cadrt+rt[2]+","
        for rp in replicas:
            cadrp=cadrt
            if rp[0]!="":
                cadrp=cadrp+rp[0]+","
            if rp[1]!="":
                cadrp=cadrp+rp[1]+","
            if rp[2]!="":
                cadrp=cadrp+rp[2]+","
            for rq in rquotes:
                cadrq=cadrp
                if rq[0]!="":
                    cadrq=cadrq+rq[0]+","
                if rq[1]!="":
                    cadrq=cadrq+rq[1]+","
                if rq[2]!="":
                    cadrq=cadrq+rq[2]+","
                lista.append(cadrq[:-1])
             
                cont=cont+1
              

dfrelaciones=pd.DataFrame(lista,columns=["columnas"])      
# 4096 registers 

#CONSTRUCTION OF EXTERNAL, INTERNAL AND ACTIVITIES AND UNION WITH ACTIONS
#external metrics
metricas_externas=[[],["followers","following","tweet_count","listed_count"]]
 
#internal metrics
metricas_internas=[[],["cant_tweets_muestra","rt","vreplicas","likes","rtquotes"]]

#activity
actividad=["","Actividad"]
               
   
cadme=""
cadmi=""
cada=""
cadcrit=""
cadbal=""
cadrel=""    
lista2=[]
cont=0
for me in metricas_externas:
    cadme=""
    if len(me)!=0:
        cadme=cadme+','.join(me)+","
 
    for mi in metricas_internas:
        cadmi=cadme
        if len(mi)!=0:
            cadmi=cadmi+','.join(mi)+","
       
        for a in actividad:
            cada=cadmi
            if a!="":
                cada=cada+a+","
                 
            for i in dfrelaciones.itertuples():
                cadrel=cada
                if i[1]!="":
                    cadrel=cadrel+i[1]+","
                lista2.append(cadrel[:-1])
                
                cont=cont+1
                print("No:",cont)
                print()

dfcolumnas=pd.DataFrame(lista2,columns=["columnas"])      


# PROCESSING INCLUDING TREE AND GRID PARAMS
print()
print("----------------------------------------------")
print()
tiempoInicia=dt.now()
print("Country:",pais)
print("started processing: ",tiempoInicia)


# *********************Segment 1. Loading the dataset
dsUsuarios = pd.read_csv('D:\\OperacionesTwitterArticuloSpyder\\Etapa4Analisis\Datos\\sampleUsersPA_D2.csv')
dsUsuarios=dsUsuarios.drop(columns= ["author_id","created_at","username","verified"], axis=1)
dsUsuariosRecortado=[]
columnas=[]
cont=0
param_grid={}
criterio=[]
balance=[]
lista=[]
columnasRetiradas=""
errores=[]
cont_error=0
giro=0
contfor=0
inicioGiro=dt.now()
duraciongiros=[]
for crit in [1,2]:#criteria: 1 --> 'gini',2 --> 'entropy'
    
    for bal in [0,1,2]:#balance:  0 none, 1 balance, 2  balanced_subsample

        for i in dfcolumnas.itertuples():# i contains the columns that should be removed from the dataframe , specifically in i[1]
            contfor=contfor+1
            if contfor==32768:
                giro=giro+1
                contfor=0
                print("--------------------------")
                print("Enter a new Giro.",giro)
               
                print("crit:",crit," bal:",bal," Giro:",giro," No:",cont)
                print("Errors:",cont_error)
                finGiro=dt.now()   
                diferencia=finGiro-inicioGiro
                print("Time elapsed :",diferencia, " of the previous turn:",giro-1)
                print("Total records:",cont+1)
                duraciongiros.append([giro-1,diferencia])
                print("Turn duration: turn number, duration")
                print(duraciongiros)
                inicioGiro=finGiro
                print()
                
            dsUsuariosRecortado=dsUsuarios.copy()
         
            if i[1]!="":# returns the content, a string
                columnasRetiradas=i[1] # this is just for the end of the script when register which columns were used and not used
                datos= dsUsuariosRecortado.drop(columns=i[1].split(","), axis=1)
                
            else:
                columnasRetiradas="Nope" # this is just for the end of the script when register which columns were used and not used
                datos=dsUsuariosRecortado
            
            cad="datos.drop(columns = 'paisSN'),datos['paisSN'],test_size=0.20,random_state = 123"
            X_train, X_test, y_train, y_test = train_test_split(
                                                datos.drop(columns = 'paisSN'),
                                                datos['paisSN'],
                                                test_size=0.20,
                                                random_state = 123,
                                               
                                            )
        
            if crit==1:
                criterio=['entropy'] 
            else:
                criterio=['gini'] 
            
            if bal==0:
                param_grid = {'n_estimators': [10],
                       'max_features': [3],
                       #'max_depth'   : [None],
                       'criterion'   : criterio
                     
                       }
            else:
                if bal==1:
                    balance=['balanced_subsample']
                else:
                    balance=['balanced']
                param_grid = {'n_estimators': [10],
                       #'max_features': [3],If None, then max_features=n_features
                       #'max_depth'   : [None],
                       'criterion'   : criterio,
                       'class_weight' :balance # ['balanced','balanced_subsample'],default=None
                       }
        
        
            grid = GridSearchCV(
                    estimator  = RandomForestClassifier(random_state = 123),
                    param_grid = param_grid,
                    #verbose    = 10,
                    n_jobs=-1,
                    refit=True
                    #return_train_score = True
                    )
            
            
            try:
                grid.fit(X = X_train, y = y_train)
            except:
                cont_error=cont_error+1
                print("Failed fit line 258.")
                print("Retired Columns:",columnasRetiradas)
                print("Previous number:",cont)
                errores.append([cont_error,cont,columnasRetiradas])
                print()
                continue # save the error and the corresponding data and continue with the next cycle of the for
               
            modelo_final = grid.best_estimator_
        
        
            predicciones = modelo_final.predict(X = X_test)
           
        
            mat_confusion = confusion_matrix(
                                y_true    = y_test,
                                y_pred    = predicciones
                            )
            
            precision = precision_score(
                        y_true    = y_test,
                        y_pred    = predicciones
                     
                        )
            
            strparamgrid=str(param_grid)
            strgrid=str(grid).replace('\n','').replace(' ','')
            strbest=str(grid.best_params_)
            reg=[pais,mat_confusion[0,0],mat_confusion[0,1], mat_confusion[1,0],mat_confusion[1,1],
                   columnasRetiradas,cad,strparamgrid,strgrid,strbest]
            cont=cont+1
            cada1000=cada1000+1
            
            lista.append(reg)# the 196,420 records are added here that at the end are converted into a dataframe to convert to csv
            if cada1000==1000:
                print("Start:",tiempoInicia)
                print("Country:",pais)
                print("crit:",crit," bal:",bal,"Giro:",giro," No:",cont)
                print("Iteration for:",contfor)
                tiempoahora=dt.now()   
                diferencia=tiempoahora-tiempoInicia
                print("Time elapsed:",diferencia)
                print("Processing.")
                print("No. ",cont)
                print("Errors:",cont_error)
                print("Turn duration: turn number, duration")
                print(duraciongiros)
                cada1000=0
                print()
   
print()
print("-------------------------------")
print("Completion of processing, start phase prior to downloading results in csv.")
print("Start:",tiempoInicia)
print("Country:",pais)
tiempoahora=dt.now()   
diferencia=tiempoahora-tiempoInicia
print("Time elapsed:",diferencia)
print("Total records:",cont)
print("Country:",pais)
print()
              
# Results are copied to csv file
print()
print("-------------------------------")
tiempoIniciaCarga=dt.now()
print("Started upload to csv:",tiempoIniciaCarga)
print("Country:",pais)
print("Turn duration: turn number, duration")
print(duraciongiros)
dsfinal=pd.DataFrame(lista,columns=['country','TN','FP','FN','TP','cols','split','params','grid','best'])   
tiempoahora=dt.now()  
diferencia=tiempoahora-tiempoIniciaCarga
print("Elapsed charging time:",diferencia)
print("Country:",pais)

dsfinal.to_csv('D:\\OperacionesTwitterArticuloSpyder\\Etapa4Analisis\Datos\\resultsPA.csv')


    
print()
print("-------------------------------")
print("Finished all script processing.")
print("Country:",pais)
print("No. ",cont)
print("Errors:",cont_error)
print("Turn duration: turn number, duration")
print(duraciongiros)
tiempoTermina=dt.now()   
diferencia=tiempoTermina-tiempoInicia
print()
print("Started the process at =", tiempoInicia)
print("Finished the whole process at = ",tiempoTermina)
print("Difference h/m/s:",diferencia)
print()      



