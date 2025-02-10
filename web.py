import streamlit as st 
import pickle 
import os
from streamlit_option_menu import option_menu

st.set_page_config(page_title="prediction of Disease Outbreaks",layout="wide", page_icon="🧑‍⚕️")
working_dir = os.path.dirname(os.path.abspath(__file__))


diabetes_model = pickle.load(open(r"C:\Users\aashi\OneDrive\Documents\predictions\saved_models\diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\aashi\OneDrive\Documents\predictions\saved_models\heart_model.sav",'rb'))
parkinsons_disease_model = pickle.load(open(r"C:\Users\aashi\OneDrive\Documents\predictions\saved_models\parkinsons_model.sav",'rb'))


with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)


if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("BloodPressure Value")
    with col1:
        SkinThickness = st.text_input("SkinThickness Value")
    with col2:
        Insulin = st.text_input("Insulin Value")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the person")

diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
    user_input= [float(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis= 'The person is diabetic'
    else:
        diab_diagnosis= 'The person is not diabetic'
st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using Machine Learning")
    col1, col2, col3  = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain Types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestroal in mg/dl")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    heart_disease_result = ""
    if st.button("Heart Disease Test Result"):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        prediction = heart_disease_model.predict([user_input])
        if prediction[0]==1:
            heart_disease_result = "This person is having heart disease"
        else:
            heart_disease_result = "This person does not have any heart disease"
    st.success(heart_disease_result)

if selected == 'Parkinsons prediction':  

    st.title("Parkinsons Disease Prediction Using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col1:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col2:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        RAP = st.text_input("MDVP:RAP")
    with col1:
        PPQ = st.text_input("MDVP:PPQ")
    with col2:
        DDP = st.text_input("Jitter:DDP")
    with col3:
        Shimmer = st.text_input("MDVP:Shimmer")
    with col1:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        APQ3 = st.text_input("Shimmer:APQ3")
    with col3:
        APQ5 = st.text_input("Shimmer:APQ5")
    with col1:
        APQ = st.text_input("MDVP:APQ")
    with col2:
        DDA = st.text_input("Shimmer:DDA")
    with col3:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col1:
        spread1 = st.text_input("Spread1")
    with col2:
        spread2 = st.text_input("Spread2")
    with col3:
        D2 = st.text_input("D2")
    with col1:
        PPE = st.text_input("PPE")

    parkinsons_result = ""

    if st.button("Parkinsons Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        prediction = parkinsons_disease_model.predict([user_input])

        if prediction[0] == 1:
            parkinsons_result = "The person has Parkinsons disease"
        else:
            parkinsons_result = "The person does not have Parkinsons disease"

    st.success(parkinsons_result)




























