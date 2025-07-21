import streamlit as st 
import joblib

model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Email Spam Check")

input_email = st.text_area("Enter Email that you want to check !")

if st.button("Check"):
    if input_email.strip() == "":
        print("Enter some Email")
    else:
        vec_email = vectorizer.transform([input_email])
        prediction = model.predict(vec_email)
        if prediction == 0:
            st.text("Warning : This Email is Spam !")
        else:
            st.text("Alhumdulillah Email is Okie.")
