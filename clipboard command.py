# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:50:11 2019

@author: rony
"""
## read from clipboard copy from excel
import pandas as pd
dfread = pd.read_clipboard()
dfread
dfread.to_clipboard()
dfread.iloc[1:5:,0:2] ##[desire index:desire index+1,desire row:desire row+1]starts with zero
