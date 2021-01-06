import pandas as pd
import matplotlib.pyplot as plt
#looks maths for this concepts
df = pd.read_csv('wine.csv')
x= type(df)
print(x)
# x = df.head()#inside function pass value of that value you want to read or fill nothing
# print(x)

#messure mean and median
#x = df['Proanth'].mean()#it will print mean of each column and after df if you write specific name of column it will only print that column
x = df.mean()
print(x) 

#median
print("median is ")
#x = df['Proanth'].median()#same works and writting mathod as mean
x = df.median()
print(x)

#x = df.wine.mode()//df['wine'].mode#you can write like this and get specific value for column
x = df.Wine.mode()#same as mean and median 
print("mode for specific value")
print(x)
x= df.describe()#it will describe your data in percntage
print(x)

#find range
print("find rage ")
x = max(df['Wine'])-min(df['Wine'])
print(x)


# varience looks determine all data points according to mean and then evaluate
x = df.var() 
print("varience is ")
print(x)

#histograms
x = df.hist('Wine');#will print histogram for each column
print(x)

#Skew
x =df.skew()#will print skew value
print("skew value")
print(x)


# will print graph for all data
# plt.bar(df['Wine'],df['Alcohol'])#will print graph of all data
# plt.xticks(rotation=90)#this will rotate tags of data on their position
# plt.show()