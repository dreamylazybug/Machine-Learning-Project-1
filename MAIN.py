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
import Explore
import Prep_Data
import Correlations
import Clean
import Regression
import XGBoost
import Cluster
import Custplots

st.title('DataScience for your Business')

# Read input Data
uploaded_file = st.sidebar.file_uploader("Choose the CSV data file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    

# Run Load & Prep Data for analysis
if st.sidebar.button('Explore Data'):
    Explore.Load_Data(df)



# Data Preparation
# Replacing blanks from data & col names, separating numeric & categorical variables, removing outliers 4 std dev away, label encoding categorical variables, merging numeric & categorical dataframe finally

if st.sidebar.button('Clean and Prepare Data'):
   df3 = Prep_Data.Prepare_Data(df)
   st.dataframe(df3)


plttype = st.sidebar.selectbox('Select the plot type', ('None','Scatter', 'Linear Regression', 'Distribution', 'Box Plot for Categorical Data'))
if plttype != 'None' :
        Custplots.cstplt(df,plttype)

if st.sidebar.button('Correlations within data'):
    Correlations.corell(df)
    

st.sidebar.write('Predictive Modeling Section')


# Selecting Features
if uploaded_file is not None:
    df3 = Clean.Clean(df)

    # Select Target Variable & Dimensions
    choices = df3.columns.values.tolist()
    optiony = st.sidebar.selectbox(
        'Select the y-variable or the target for regression?', choices)
    optionx = st.sidebar.multiselect(
        'Select the x-variables or the predictors for regression', choices)
    
    # Storing them as predictors & targets data frames
    predictors = df3[optionx]
    targets = df3[optiony]

with st.sidebar:

    with st.form(key='Regression'):
        st.write('Parameter Tuning for XGBoost')
        testsz = st.number_input('Test Sample Size', min_value=0.2, max_value=0.7, value=0.3, step=0.05)
        lr = st.number_input('Learning rate', min_value=0.05, max_value=0.3, value=0.1, step=0.05)
        maxdepth = st.number_input('Maximum Depth', min_value=3, max_value=10, value=5, step=1)
        submit_button = st.form_submit_button(label='Submit parameters')

if st.sidebar.button('Regress Data'):
    Regression.regres(predictors, targets, testsz)
    
if st.sidebar.button('Gradient Boosting - XGBOOST'):
    XGBoost.xgboost(predictors, targets, testsz, lr, maxdepth)
    
st.sidebar.write('Data Clustering')



if uploaded_file is not None:

    # Pick the parameters to cluster 
    choicesclst = df3.columns.values.tolist()
    optionclst = st.sidebar.multiselect(
        'Select the columns to cluster data points', choicesclst)

    # Data for Clustering
    dclst = df3[optionclst]

if st.sidebar.button('k-Means'):
    Cluster.cluster(dclst)
