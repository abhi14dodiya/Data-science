import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pn 

#in this prectical we have multipl task to do on given file each operation has description before it.

#1.open files
df_matches  = pn.read_csv('matches.csv')
df_delv  = pn.read_csv('deliveries.csv')

#2.print data and data types
# print("matches data")
# print(df_matches.head())#print whole data
# print(df_matches.describe())#cut the string and describe only countable values
# print(df_matches.info())#tell datatypes of column

# #3.print specific column and drop from real file and save
# #print(df_matches['umpire3'].unique())#will show specific column
# df2 = df_matches.drop(['umpire3'],axis=1)
# print(df2.head())
# df2.to_csv("D:\\python experiment\\pythn basic precticals\\pnada operation\\ipl_dataipl_data\\matches2.csv",index=False)#find solution for syntax make index false or it will have additionsl column of index in csv file and whole command copy filr into given file

#4.print total no matahes played,number of season,
# print("total matches played:",df_matches.shape[0])
# print("total seasons played:",df_matches['season'].nunique())#add n before unique will print total count instead of full array

# #5.print most mn of the match// highest winning team(total highest wins)
# print("highest no of man of the match win by: \n",df_matches['player_of_match'].value_counts()[:10])#will print maximum wins in decrising order and value _count funtion will count each value which is repeating  and at last[:10 ] will print top 10 datasets
# print("highest no of Wins of ateam is: \n",df_matches['winner'].value_counts().idxmax())#same as above but just for teams win and at end we add idxmax() function wich count highest value  and print only top one(in short it will return index that max time repeat)

#6.find team which have won by max margine
# big_margin = df_matches[(df_matches['win_by_runs'] >= 100) | (df_matches['win_by_wickets'] >= 8)]# we add two condition using 'or' it will identifies that row that passed theses conditiions and store in variable
# print(" Wins matches by huge margine teams are: \n",big_margin['winner'].value_counts())#using that variable we print that rows winner's column data that stored row in variable

# #7.find each city match played 
# print("highest no of matched played at stadium: \n",df_matches['city'].value_counts())

#8.find min and max win_by_wicket at each city
# min_wicket = df_matches[(df_matches['win_by_wickets'] > 9) ]# here we find that which team is won by wicket more than 9 means in match second inning  1 wicket or no wicket is down  it is min wicket win and  
# print(" in second inning min by wickets wins at minimum wicket are: \n",min_wicket['city'].value_counts())
# max_wicket = df_matches[(df_matches['win_by_wickets'] < 10) ]# here we find that which team is won by wicket less than 10 because at 10 wicket team is lost so  means in match second inning  9 wicket or less wicket is down  it is min wicket win and  
# print(" in second inning max by wickets wins at maximum wicket are: \n",min_wicket['city'].value_counts())

#9.find the match by biggest defeat by runs

#10.find the match by biggest defeat by wickets
