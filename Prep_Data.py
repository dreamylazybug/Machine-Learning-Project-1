#######################################################################################
# DATA SCIENCE MODELS POWERED BY VISUALIZATION FROM STREAMLIT
# AUTHOR: LAXMI MULLAPUDI 
# LAST UPDATED " 2022/10/20
########################################################################################


import seaborn as sns
import numpy as np
import matplotlib.pylab as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
#from sklearn.metrics import plot_confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn import tree
import xgboost as xgb
import math
#from apyori import apriori
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


# Data Preparation
# Replacing blanks from data & col names, separating numeric & categorical variables, Fill NA with 0 in numeric data, label encoding categorical variables, merging numeric & categorical dataframe finally
def Prepare_Data(df):
    
    # Replacing Blanks from data
    df.replace(' ', '_', regex=True, inplace=True)

    # Replacing blanks from Columns names (for viewing trees)
    df.columns = df.columns.str.replace(' ', '_')

    # Separating numeric & Categorical columns
    dtf = df._get_numeric_data()
    dtf = dtf.fillna(0)  # Filling NAs
    dtg = df.select_dtypes(include=['object'])
    
    # Getting # of columns to let users know
    l = len(dtg.columns)
    st.write('The number of columns with categorical/non numeric values that will be encoded using label encoder =', l)

    dtf['Index'] = np.arange(len(dtf))
    dtg['Index'] = np.arange(len(dtg))
    
    st.write('The numeric Columns in the data set are' )
    st.dataframe(dtf)
    st.write('The categorical/non numeric Columns in the data set are' )
    st.dataframe(dtg)
    
    

    # Convert all categorical variables to string
    dtg = dtg.applymap(str)

    # Transform Categorical variables
    from sklearn import preprocessing
    label_encoder = preprocessing.LabelEncoder()


    # Encode labels in column
    for i in range(0, l):
        dtg.iloc[:, i] = label_encoder.fit_transform(dtg.iloc[:, i])

    st.write('The categorical/non numeric Columns were encoded as following' )
    st.dataframe(dtg)
   
    df3 = pd.merge(dtf, dtg, left_index=True, right_index=True)
    
    st.success(
        'Cleaned up data is stored in file named Prepared_Data.csv', icon="✅")
    return(df3)



