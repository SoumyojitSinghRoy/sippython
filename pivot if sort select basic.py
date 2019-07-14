# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:31:33 2019

@author: rony
"""
##multi indexing
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from pydataset import data #importing data
data('iris')
mtcars = data('mtcars')
mtcars.head()
data1= mtcars
data1.columns #column name
data1.values #values of df
data1.index #index name
data1.dtypes
data1[['am','vs','cyl','gear','carb']] = data1[['am','vs','cyl', 'gear','carb']].astype('category')## changing datatype to category
data1.dtypes
data1.iloc[0:3,0:4]
#resetting the index
data2 = data1.reset_index()
data2.iloc[0:3,0:4]
data2.columns
data2.rename({'index':'carname'},inplace=True, axis = 'columns')
data2.head() 
data2.columns
data3cyl = data2.set_index('cyl')
data3cyl.head()
data3cyl.loc[6,]
data2.dtypes
data3cyl.column
data2.head()
#resetting index
data3 = data2.set_index('gear', drop=True).head()
data3
data3.reset_index().set_index('cyl').head()
#%%%
data2.columns
data2.head()
#groupby
dataGg = data2.groupby(['gear']).mpg.mean() #gear by mean milage
dataGg
dataGg.index
type(dataGg)
dataGg[3]
#group by two column
dataGga = data2.groupby(['gear','am']).mpg.mean()
dataGga.index
dataGga
dataGgcc = data2.groupby(['gear','cyl','carb']).mpg.mean()
dataGgcc
dataGgcc.unstack()
dataGgcc.unstack().unstack()
dataGgcc
dataGgcc.loc[3]#take output 3 gear index
dataGgcc.head()
dataGgcc.loc[4]
dataGgcc.loc[4,6] #takes the output of 3 gear 6 cylinder
dataGgcc.loc[4,4,1]
dataGgcc.sort_index()#sorting gear 0 column
dataGgcc.sort_index(level=1)# sorting cyl
dataGgcc.sort_index(level=2) #carb
mtcars.sort_values(['mpg','hp']).head(10)#sorting
mtcars.sort_values(['mpg','hp','wt'],ascending= True).head(10)
mtcars[['gear','cyl','wt']].sort_values(['gear','cyl','wt'], ascending=[True,False,True])
mtcars.loc[mtcars['mpg']>25,['mpg','hp']]
mtcars.loc[mtcars['mpg']>25,['mpg','hp']]
mtcars.loc[mtcars['mpg']>25,['mpg','hp']]
mtcars.loc[(mtcars['mpg']>25) & (mtcars['hp']>35) , ['mpg','hp']]
mtcars.loc[(mtcars['vs']==1)| (mtcars['am']==1) , ['mpg','hp','vs','am']].head(10)
mtcars.pivot_table(index='gear',values='mpg', columns='am')
mtcars.pivot_table(index=['gear','vs'], values='mpg', columns=['am','cyl'],fill_value=0)
mtcars.pivot_table(index=['gear'], columns=['vs','am'],aggfunc={'mpg':np.mean,'wt':min})
