# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:53:19 2019

@author: rony
"""
import pandas as pd
from pydataset import data
df=data('mtcars')
df.shape[0]
df.dtypes
df.describe()
pd.set_option('display.max_column',11)
df
print(dir(pd),end=',') #all pandas commands
pd.read_csv?
import numpy as np
print(dir(np),end=',')
np.cos?
np1 = np.array([1,2,34,5,67,7,5]) #array creation
np1
np1.index # no index- error
np1[0:3]
np1[[1,5,3]]
ps1 = pd.Series([1,3,4,5,6,4])#column wise
ps1
ps1[0:3]
ps1.index#gives you index
ps2=pd.Series([1,2,3,4,5,6,7],index=['bba','das','rew','fdsf','ewd','ere','cdc'], dtype='int32')
ps2
ps2['bba']
ps2[['das','rew','ewd']]
ps2[['bba':'ewd']]##does not work

ps2.sample(2)
