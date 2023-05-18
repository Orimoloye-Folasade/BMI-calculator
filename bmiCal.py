import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# st.title('BMI CALCULATOR')
# st.subheader('Body Mass Index')
# st.sidebar.image('pngwing.com (3).png')
st.markdown("<h1 style = 'color: #d72845' >BMI CALCULATOR INTERFACE</h1>", unsafe_allow_html=True)
st.markdown("<h6 style = 'color: #62b946'>Body Mass Index</h6> ", unsafe_allow_html = True)
st.image('pngwing.com (3).png', width= 400, caption= 'Live Healthy')

st.video('https://www.youtube.com/watch?v=UowWA-8TiyI')

gender = st.radio('Gender',['Male','Female'])

username = st.text_input('Username')
if st.button('SUBMIT'):
    if gender=='Male':
        st.write(f"Welcome Mr {username}")
    else:
        st.write(f"Welcome Miss {username}")


st.markdown('<hr>', unsafe_allow_html=True)

# FOR HEIGHT

height_metric_selector = st.selectbox('Your Height Metric', ['cms', 'meters','foot'])

if height_metric_selector=='cms':
    height = st.slider('Slide your height in cms', 10.0, 1000.0,500.0)
    heights= height * 0.0328084
elif height_metric_selector=='meters':
    height = st.slider('Slide your heigght in meters', 1.0, 15.0, 6.0)
    heights=height *3.28084
elif height_metric_selector=='foot':
    height= st.slider('Slide your height in foot', 3.0, 10.0,7.0)
    heights = height


# FOR WEIGHT
Weight_metric_selector = st.selectbox('Select Your Weight Metric',['kg', 'lbs'])

if Weight_metric_selector=='kg':
    weight = st.slider('Slide your weight in Kilogram(kg)', 1.0, 250.0,50.0)
    weights = weight
elif Weight_metric_selector:
    weight= st.slider('Slide your weight in Pounds(lbs)', 1.0, 600.0, 70.0)
    weights = weight *2.20462
st.markdown('<hr>', unsafe_allow_html=True)

# NIGERIA STANDARD OF CALCULATION

body_size={'weight':weight, 'height':height}

data = pd.DataFrame(body_size,index=[0])
st.write(data)
bmi = (weights/(heights *0.3048)**2)
if st.button('Get your BMI'):
    st.success(bmi)

st.balloons()
if bmi< 18.5:
    st.error('You are  Underweight')

elif bmi >18.5:
    st.error('Normal')