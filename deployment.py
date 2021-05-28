# -*- coding: utf-8 -*-
"""
Created on Mon May 24 18:49:03 2021

@author: Amit Kulkarni
"""

import pandas as pd
import numpy as np
import pickle

from xgboost import XGBClassifier

import streamlit as st

loaded_model = pickle.load(open("Loan_Prediction_G1_P53.pkl","rb"))

# giving the webpage a title
st.title("Loan Status Prediction")
st.header("This application helps you identify Loan Status for the given inputs")
st.subheader("From the all classification methods we will use Extreme Gradient Boosting Method")

st.sidebar.title('Please select suitable option')
# here we define some of the front end elements of the web page like 
# the font and background color, the padding and the text to be displayed
html_temp = """
<div style ="background-color:orange;padding:13px">
<h1 style ="color:black;text-align:center;">Group - 1 Batch - P53 </h1>
</div>
"""
# this line allows us to display the front end aspects we have 
# defined in the above code
st.markdown(html_temp, unsafe_allow_html = True)
result =""


def user_input_features():
    #Radio Button for Married & Credit History
    
    Married_Yes = st.sidebar.radio("Marital Status: ", ('Married', 'Unmarried'))
    
    if Married_Yes == 'Married':
        Married_Yes = 1
    else:
        Married_Yes = 0
    
    Credit_History = st.sidebar.radio("Select Credit History: ", ('Clear', 'Unclear'))
    
    if Credit_History == 'Clear':
        Credit_History = 1
    else:
        Credit_History = 0
    
    #Selection Box for Dependents & Property_Area
    
    Dependents = st.sidebar.selectbox("Dependents: ",['No Dependents', 'Singleton', 'Two Dependents', 'Three or more Dependents'])
    
    if Dependents == 'No Dependents':
        Dependents = 0
    elif Dependents == 'Singleton':
        Dependents = 1
    elif Dependents == 'Two Dependents':
        Dependents = 2
    else:
        Dependents = 3
    
    Property_Area = st.sidebar.selectbox("Property Area Owned: ",['Rural', 'Semi Urban', 'Urban'])
    
    if Property_Area == 'Rural':
        Property_Area = 0
    elif Property_Area == 'Semi Urban':
         Property_Area = 1
    else:
         Property_Area = 2
    
    #Number Input for Loan Amount and Tenure
    LoanAmount = st.sidebar.number_input("Loan Amount (in Thousands):",min_value=0)
    
    LoanAmount = LoanAmount*1000
    
    Loan_Amount_Term = st.sidebar.number_input("Loan Term (in months)",min_value = 12, max_value = 360, value = 12)
    
    #Slider for Applicant & Coapplicant Income
    ApplicantIncome = st.sidebar.slider("Applicant Income",0,81000,key="ApplicantIncome")
    CoapplicantIncome = st.sidebar.slider("Copplicant Income",0,41667,key="ApplicantIncome")
    
    topdata = {'Married_Yes':Married_Yes,'Dependents':Dependents,'Credit_History':Credit_History,'Property_Area':Property_Area,'LoanAmount':LoanAmount,'Loan_Amount_Term':Loan_Amount_Term,'ApplicantIncome':ApplicantIncome,'CoapplicantIncome':CoapplicantIncome}
    features = pd.DataFrame(topdata,index = [0]) 
    return features

df = user_input_features()
st.subheader('User Input parameters')
st.write(df)



def new_features():
    TotalIncome = df['ApplicantIncome'] + df['CoapplicantIncome']
    r = (10/100)/12
    df['LoanAmount']
    a = df['LoanAmount']*r*(1+r)**df['Loan_Amount_Term']
    b = (1+r)**(df['Loan_Amount_Term']-1)
    EMI = a/b
    LoanAmount_per_Total_Income = df['LoanAmount']/(TotalIncome)
    EMI_per_Loan_Amount_Term = EMI/(df['Loan_Amount_Term'])
    TotalIncome_t = np.power(np.log1p(TotalIncome),0.25)
    
    newfeatures = {'TotalIncome':TotalIncome,'EMI':EMI,'TotalIncome_t':TotalIncome_t,'LoanAmount_per_Total_Income':LoanAmount_per_Total_Income,'EMI_per_Loan_Amount_Term':EMI_per_Loan_Amount_Term}
    features1 = pd.DataFrame(newfeatures,index = [0]) 
    return features1

df1 = new_features()
st.subheader('New parameters')
st.write(df1)

# =============================================================================
# TOP 15 FEATURES
# =============================================================================

#1
Married_Yes = df['Married_Yes']

#2
Dependents = df['Dependents']
   
#3
Credit_History = df['Credit_History']

#4
Property_Area = df['Property_Area']

#5
LoanAmount_t = np.log(np.power(df['LoanAmount'],1/3))

#6
ApplicantIncome_t = np.log1p(np.power(df['ApplicantIncome'],1/6))

#7
TotalIncome = df1['TotalIncome']


#8
EMI_t = np.log1p(np.power(df1['EMI'],1/3))

#9 Total_Income_Bins
TotalIncome_t = df1['TotalIncome_t']
if pd.Series(TotalIncome_t>1.733406891).all():
    Total_Income_Bins = 4
elif pd.Series(TotalIncome_t>1.7177858).all():
    Total_Income_Bins = 3
elif pd.Series(TotalIncome_t>1.70664370).all():
    Total_Income_Bins = 2
elif pd.Series(TotalIncome_t>1.694597431).all():
    Total_Income_Bins = 1
else:
    Total_Income_Bins = 0
   

#10 LoanAmount_per_Total_Income_t
LoanAmount_per_Total_Income_t = (np.power(df1['LoanAmount_per_Total_Income'],1/4))

#11 Credit_History_Income_Sum_t

if pd.Series(Credit_History==0).bool():
    Credit_History_Income_Sum_t = 2.400064483
else:
    Credit_History_Income_Sum_t = 2.466787324
   
#12 Dependents_LoanAmount_Sum_t

if pd.Series(Dependents == 0).all():
    Dependents_LoanAmount_Sum_t = 2.049922748
elif pd.Series(Dependents == 1).all():
    Dependents_LoanAmount_Sum_t = 2.02184802
elif pd.Series(Dependents == 2).all():
    Dependents_LoanAmount_Sum_t = 2.016481798
else:
    Dependents_LoanAmount_Sum_t = 2.002254345


#13 LoanAmount_per_Total_Income_Bins

if pd.Series(LoanAmount_per_Total_Income_t >= 2.328178545).all():
    LoanAmount_per_Total_Income_Bins = 4
elif pd.Series(LoanAmount_per_Total_Income_t >= 2.250321431).all():
    LoanAmount_per_Total_Income_Bins = 3
elif pd.Series(LoanAmount_per_Total_Income_t >= 2.175743674).all():
    LoanAmount_per_Total_Income_Bins = 2
elif pd.Series(LoanAmount_per_Total_Income_t >= 2.050008243).all():
    LoanAmount_per_Total_Income_Bins = 1
else:
    LoanAmount_per_Total_Income_Bins = 0

#14
EMI_per_Loan_Amount_Term_t = np.power(np.log1p(df1['EMI_per_Loan_Amount_Term']),1/4)

#15 Property_Area_LoanAmount_per_TotalIncome_mean_t
 
if pd.Series(Property_Area == 0).bool():
    Property_Area_LoanAmount_per_Total_Income_mean_t = 1.590497483
elif pd.Series(Property_Area == 1).bool():
    Property_Area_LoanAmount_per_Total_Income_mean_t = 1.595491286
else:
    Property_Area_LoanAmount_per_Total_Income_mean_t = 1.568713913



topfeatures = {'Married_Yes':Married_Yes,'Dependents':Dependents, 'Credit_History':Credit_History, 'Property_Area':Property_Area, 'LoanAmount_t':LoanAmount_t
                  ,'ApplicantIncome_t':ApplicantIncome_t, 'TotalIncome_t':TotalIncome_t, 'EMI_t':EMI_t,'Total_Income_Bins':Total_Income_Bins,'LoanAmount_per_Total_Income_Bins':LoanAmount_per_Total_Income_Bins, 'Credit_History_Income_Sum_t':Credit_History_Income_Sum_t,
   'Dependents_LoanAmount_Sum_t':Dependents_LoanAmount_Sum_t, 'LoanAmount_per_Total_Income_t':LoanAmount_per_Total_Income_t,
   'EMI_per_Loan_Amount_Term_t':EMI_per_Loan_Amount_Term_t,'Property_Area_LoanAmount_per_Total_Income_mean_t':Property_Area_LoanAmount_per_Total_Income_mean_t}
features2 = pd.DataFrame(topfeatures,index = [0]) 

df2 = features2
st.subheader('Top Features')
st.write(df2)

    
prediction = loaded_model.predict(df2)
prediction_proba = loaded_model.predict_proba(df2)

st.subheader('Predicted Result')
st.write('Congratulations your Loan is approved' if prediction == 1 else 'Sorry your Loan is Rejected')

st.subheader('Prediction Probability')
st.write(prediction_proba)