# -*- coding: utf-8 -*-
"""deploy_hbp.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yzr3539BccO06ua3TEtbGXzLFSttuMO3
"""

import streamlit as st
import pickle
from PIL import Image

with open("random_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("HIGH BLOOD PRESSURE")
st.markdown("By preethi")
image = Image.open("1e82b7.webp")
st.image(image, use_column_width=True)

age = st.number_input("Age of a person",min_value=0,max_value=100,value=0)
height = st.number_input("Height of a person",min_value=0,max_value=400,value=0)
weight=st.number_input("weight of a person",min_value=0,max_value=1000,value=0)
waist=st.number_input("waist size",min_value=0,max_value=1000,value=0)
eyesight=st.number_input("Eyesight(left)",min_value=0.0)
eyesight=st.number_input("Eyesight(right)",min_value=0.0)
hearing=st.number_input("Hearing(left)",min_value=0,max_value=1000,value=0)
hearing=st.number_input("Hearing(right)",min_value=0,max_value=1000,value=0)
systolic=st.number_input("Systolic pressure",min_value=0,max_value=1000,value=0)
relaxation=st.number_input("Dyastolic pressure",min_value=0,max_value=1000,value=0)
fasting_blood_sugar=st.number_input("Blood sugar",min_value=0,max_value=1000,value=0)
Cholesterol=st.number_input("Cholesterol",min_value=0,max_value=1000,value=0)
triglyceride=st.number_input("Triglyceride",min_value=0,max_value=1000,value=0)
HDL=st.number_input("HDL",min_value=0,max_value=1000,value=0)
LDL=st.number_input("LDL",min_value=0,max_value=1000,value=0)
hemoglobin=st.number_input("Hemoglobin",min_value=0.0)
Urine_protein=st.number_input("urine protein",min_value=0,max_value=1000,value=0)
serum_creatinine=st.number_input("serum creatinine",min_value=0.0)
AST=st.number_input("AST",min_value=0,max_value=1000,value=0)
ALT=st.number_input("ALT",min_value=0,max_value=1000,value=0)
Gtp=st.number_input("GTP",min_value=0,max_value=1000,value=0)
dental_caries=st.number_input("dental caries",min_value=0,max_value=1000,value=0)
smoking=st.number_input("smoking",min_value=0,max_value=100,value=0)
if st.button("HyperTension test result"):
    input_features = [[age, height,weight,waist,eyesight,
       eyesight,hearing,hearing,systolic,
       relaxation, fasting_blood_sugar,Cholesterol, triglyceride,
       HDL,LDL,hemoglobin, Urine_protein,serum_creatinine,AST,
       ALT,Gtp,dental_caries,smoking]] 
    prediction = model.predict(input_features)[0]
    if prediction == 0:
            st.subheader("The person doesn't have Hypertension.")
    elif prediction == 1:
            st.subheader("The person have Hypertension.")
else:
        st.subheader("Please enter a text for prediction.")

