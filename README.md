## Repository of data and script used by the article: **Methodological proposal to identify the nationality of Twitter users through Random-Forests**

We have saved 30 tables in two repositories: repository 1 and repository 2.   
**Repository 1** has 12 tables:  https://github.com/damian-quijano/identify_nationality_twitter    
http://dx.doi.org/10.5281/zenodo.7254532     
**Repository 2** has 18 tables: https://github.com/damian-quijano/-identify_nationality_twitter2   
http://dx.doi.org/10.5281/zenodo.7254534     
   
Large tables have been saved in the first repository, small size tables and code have been saved in the second repository. 
  
**This is repository 2**. Below are the names and sizes of the largest tables used in the study.It is a group of 18 tables.

| Sequence 	| Table                	| File txt                 	| Records 	| Size kb txt 	|
|----------	|----------------------	|--------------------------	|---------	|-------------	|
| 2        	| UsersCR_D1           	| UsersCR_D1.txt           	| 12000   	| 979         	|
| 2        	| UsersGT_D1           	| UsersGT_D1.txt           	| 14314   	| 1170        	|
| 2        	| UsersHN_D1           	| UsersHN_D1.txt           	| 8991    	| 744         	|
| 2        	| UsersNI_D1           	| UsersNI_D1.txt           	| 6942    	| 588         	|
| 2        	| UsersPA_D1           	| UsersPA_D1.txt           	| 17292   	| 1418        	|
| 2        	| UsersSV_D1           	| UsersSV_D1.txt           	| 13642   	| 1128        	|
| 4        	| UsersCR_D2           	| UsersCR_D2.txt           	| 9843    	| 1123        	|
| 4        	| UsersNI_D2           	| UsersNI_D2.txt           	| 5223    	| 608         	|
| 4        	| UsersPA_D2           	| UsersPA_D2.txt           	| 14789   	| 1704        	|
| 5        	| sampleUsersCR_D2     	| sampleUsersCR_D2.txt     	| 196420  	| 45          	|
| 5        	| sampleUsersNI_D2     	| sampleUsersNI_D2.txt     	| 196420  	| 46          	|
| 5        	| sampleUsersPA_D2     	| sampleUsersPA_D2.txt     	| 196420  	| 46          	|
| 7        	| classifiedUsersCR_D2 	| classifiedUsersCR_D2.txt 	| 9843    	| 1445        	|
| 7        	| classifiedUsersNI_D2 	| classifiedUsersNI_D2.txt 	| 5223    	| 803         	|
| 7        	| classifiedUsersPA_D2 	| classifiedUsersPA_D2.txt 	| 14789   	| 2205        	|
| 8        	| UsersCR_TP           	| UsersCR_TP.txt           	| 3886    	| 543         	|
| 8        	| UsersNI_TP           	| UsersNI_TP.txt           	| 1343    	| 204         	|
| 8        	| UsersPA_TP          	| UsersPA_TP.txt           	| 6392    	| 935         	|


**Sequence** refers to the order in which data is generated from the above tables. This means that if the table has sequence 3 it was created from the data in the table with sequence 2.  
In this repository the tables with sequence 2,4,5,7 and 8 are stored. In repository 1 are the tables with sequences 1,3 and 6. 
Size kb txt means that the file size is in kilobytes and text format.  
   
*Below is shown data structure of the following tables*: **USersCR_D1,UsersGT_D1,UsersHN_D1,UsersNI_D1,USersPA_D1,UsersSV_D1**   
| Field               	| Type        	| Description                                    	|
|---------------------	|-------------	|------------------------------------------------	|
| id_user             	| bigint      	| id user                                        	|
| created_at          	| varchar(50) 	| account creation date                          	|
| username            	| varchar(50) 	|                                                	|
| verified            	| varchar(50) 	| If the account is verified by Twitter          	|
| followers           	| int         	|                                                	|
| following           	| int         	|                                                	|
| tweet_count         	| int         	|                                                	|
| listed_count        	| int         	|                                                	|
| cant_tweets_muestra 	| int         	| Number of messages downloaded from the account 	|
| rt                  	| int         	| retweet                                        	|
| vreplicas           	| int         	| replies                                        	|
| likes               	| int         	| likes                                          	|
| rtquotes            	| int         	| quotes                                         	|


*Below is shown data structure of the following tables*: **USersCR_D2,UsersNI_D2,USersPA_D2**  

| Field               	| Type         	| Description                                                                                                                                          	|
|---------------------	|--------------	|------------------------------------------------------------------------------------------------------------------------------------------------------	|
| author_id           	| bigint       	| id user                                                                                                                                              	|
| username            	| varchar(MAX) 	|                                                                                                                                                      	|
| created_at          	| varchar(50)  	|                                                                                                                                                      	|
| verified            	| varchar(50)  	| If the account is verified by Twitter                                                                                                                	|
| followers           	| int          	|                                                                                                                                                      	|
| following           	| int          	|                                                                                                                                                      	|
| tweet_count         	| int          	|                                                                                                                                                      	|
| listed_count        	| int          	|                                                                                                                                                      	|
| cant_tweets_muestra 	| int          	| Number of messages downloaded from the account                                                                                                       	|
| rt                  	| int          	| retweet                                                                                                                                              	|
| vreplicas           	| int          	| replies                                                                                                                                              	|
| likes               	| int          	| likes                                                                                                                                                	|
| rtquotes            	| int          	| quotes                                                                                                                                               	|
| menciones_a_In      	| int          	| mentions of the user to other   users      that are part of the users of the table                                                                   	|
| menciones_a_Out     	| int          	| mentions to other users who are   not part      of the table users                                                                                   	|
| menciones_de_In     	| int          	| mentions of other users to the   current user      that are part of the table users                                                                  	|
| rt_a_In             	| int          	| retweets of the user to other   users      that are part of the users of the table                                                                   	|
| rt_a_Out            	| int          	| retweets to other users who are   not part      of the table users                                                                                   	|
| rt_de_In            	| int          	| retweets of other users to the   current user that      are part of the table users                                                                  	|
| rp_a_In             	| int          	| replies of the user to other users that are part of the users of the table                                                                           	|
| rp_a_Out            	| int          	| replies to other users who are not part of the table users                                                                                           	|
| rp_de_In            	| int          	| replies of other users to the current user that are part of the table users                                                                          	|
| rq_a_In             	| int          	| quotes of the user to other users that are part of the users of the table                                                                            	|
| rq_a_Out            	| int          	| quotes to other users who are not part of the table users                                                                                            	|
| rq_de_In            	| int          	| quotes of other users to the current user that are part of the table users                                                                           	|
| Actividad           	| int          	| Activity.Columns sum: menciones_a_In,menciones_a_Out, menciones_de_In,rt_a_In,rt_a_Out,rt_de_In,rp_a_In, rp_a_Out,rp_de_In,rq_a_In,rq_a_Out,rq_de_In 	|

*Below is shown data structure of the following tables*: **sampleUsersCR_D2,sampleUsersNI_D2,sampleUsersPA_D2**  
| Field               	| Type         	| Description                                                                                                                                          	|
|---------------------	|--------------	|------------------------------------------------------------------------------------------------------------------------------------------------------	|
| author_id           	| bigint       	| id user                                                                                                                                              	|
| username            	| varchar(MAX) 	|                                                                                                                                                      	|
| created_at          	| varchar(50)  	|                                                                                                                                                      	|
| verified            	| varchar(50)  	| If the account is verified by Twitter                                                                                                                	|
| followers           	| int          	|                                                                                                                                                      	|
| following           	| int          	|                                                                                                                                                      	|
| tweet_count         	| int          	|                                                                                                                                                      	|
| listed_count        	| int          	|                                                                                                                                                      	|
| cant_tweets_muestra 	| int          	| Number of messages downloaded from the account                                                                                                       	|
| rt                  	| int          	| retweet                                                                                                                                              	|
| vreplicas           	| int          	| replies                                                                                                                                              	|
| likes               	| int          	| likes                                                                                                                                                	|
| rtquotes            	| int          	| quotes                                                                                                                                               	|
| menciones_a_In      	| int          	| mentions of the user to other   users      that are part of the users of the table                                                                   	|
| menciones_a_Out     	| int          	| mentions to other users who are   not part      of the table users                                                                                   	|
| menciones_de_In     	| int          	| mentions of other users to the   current user      that are part of the table users                                                                  	|
| rt_a_In             	| int          	| retweets of the user to other   users      that are part of the users of the table                                                                   	|
| rt_a_Out            	| int          	| retweets to other users who are   not part      of the table users                                                                                   	|
| rt_de_In            	| int          	| retweets of other users to the   current user that      are part of the table users                                                                  	|
| rp_a_In             	| int          	| replies of the user to other users that are part of the users of the table                                                                           	|
| rp_a_Out            	| int          	| replies to other users who are not part of the table users                                                                                           	|
| rp_de_In            	| int          	| replies of other users to the current user that are part of the table users                                                                          	|
| rq_a_In             	| int          	| quotes of the user to other users that are part of the users of the table                                                                            	|
| rq_a_Out            	| int          	| quotes to other users who are not part of the table users                                                                                            	|
| rq_de_In            	| int          	| quotes of other users to the current user that are part of the table users                                                                           	|
| Actividad           	| int          	| Activity.Columns sum: menciones_a_In,menciones_a_Out, menciones_de_In,rt_a_In,rt_a_Out,rt_de_In,rp_a_In, rp_a_Out,rp_de_In,rq_a_In,rq_a_Out,rq_de_In 	|
| paisSN              	| int          	| 1 or 0. 1 Identified the country, 0 is not the country. Human check.    

  
  
*Below is shown data structure of the following tables*: **classifiedUsersCR_D2,classifiedUsersNI_D2,classifiedUsersPA_D2,UsersCR_TP,UsersNI_TP, UsersPA_TP**    
| Field               	| Type         	| Description                                                                                                                                          	|
|---------------------	|--------------	|------------------------------------------------------------------------------------------------------------------------------------------------------	|
| author_id           	| bigint       	| id user                                                                                                                                              	|
| username            	| varchar(MAX) 	|                                                                                                                                                      	|
| created_at          	| varchar(50)  	|                                                                                                                                                      	|
| verified            	| varchar(50)  	| If the account is verified by Twitter                                                                                                                	|
| followers           	| int          	|                                                                                                                                                      	|
| following           	| int          	|                                                                                                                                                      	|
| tweet_count         	| int          	|                                                                                                                                                      	|
| listed_count        	| int          	|                                                                                                                                                      	|
| cant_tweets_muestra 	| int          	| Number of messages downloaded from the account                                                                                                       	|
| rt                  	| int          	| retweet                                                                                                                                              	|
| vreplicas           	| int          	| replies                                                                                                                                              	|
| likes               	| int          	| likes                                                                                                                                                	|
| rtquotes            	| int          	| quotes                                                                                                                                               	|
| menciones_a_In      	| int          	| mentions of the user to other   users      that are part of the users of the table                                                                   	|
| menciones_a_Out     	| int          	| mentions to other users who are   not part      of the table users                                                                                   	|
| menciones_de_In     	| int          	| mentions of other users to the   current user      that are part of the table users                                                                  	|
| rt_a_In             	| int          	| retweets of the user to other   users      that are part of the users of the table                                                                   	|
| rt_a_Out            	| int          	| retweets to other users who are   not part      of the table users                                                                                   	|
| rt_de_In            	| int          	| retweets of other users to the   current user that      are part of the table users                                                                  	|
| rp_a_In             	| int          	| replies of the user to other users that are part of the users of the table                                                                           	|
| rp_a_Out            	| int          	| replies to other users who are not part of the table users                                                                                           	|
| rp_de_In            	| int          	| replies of other users to the current user that are part of the table users                                                                          	|
| rq_a_In             	| int          	| quotes of the user to other users that are part of the users of the table                                                                            	|
| rq_a_Out            	| int          	| quotes to other users who are not part of the table users                                                                                            	|
| rq_de_In            	| int          	| quotes of other users to the current user that are part of the table users                                                                           	|
| Actividad           	| int          	| Activity.Columns sum: menciones_a_In,menciones_a_Out, menciones_de_In,rt_a_In,rt_a_Out,rt_de_In,rp_a_In, rp_a_Out,rp_de_In,rq_a_In,rq_a_Out,rq_de_In 	|
|pred             	| int          	| 1 or 0,   Model prediction.                                                                         	|
| prob0           	| float          	|Probability class 0 (not of the nationality)                                                                                           	|
| prob1            	| float        	| Probability  class 1 (nationality ok)  
  


