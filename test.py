import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
import streamlit as st
import pickle
model=pickle.load(open('model.pkl','rb'))
#web app

st.title("Credit Card Fraud Detection")

input=st.text_input("Enter All required Features Values")
input_df=input.split(',')
submit=st.button("Submit")

if submit:
    features=np.asarray(input_df, dtype=np.float64)
    detection_result = model.predict(features.reshape(1,-1))
    if detection_result[0]==0:
        st.write("Secure Transaction")
    else:
        st.write("Fradulant Transaction")
    
    


