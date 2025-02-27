# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:30:14 2025

** Predictive Credit Risk Modelling**
_______________________________________________________________________________
Predictive credit risk modelling is very important for financial institutions,
this is because by using machine learning it can be easier to identify which 
borrower will not repay their loans and this can also help by identifying 
hidden traits that are associated with borrowers who default which a credit 
score may not be able to point out, we are going to use Leading Indian Bank & 
CIBIL Real-World Dataset to develop our predictive model.
_______________________________________________________________________________
@author: Dakalo Mudimeli
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
internal = pd.read_excel("Data/Internal_Bank_Dataset.xlsx")
external = pd.read_excel("Data/External_Cibil_Dataset.xlsx")

df1 = internal.copy()