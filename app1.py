import streamlit as st
from PIL import Image

img=Image.open('IMG-20231206-WA0139 (4).jpg')
st.sidebar.image(img)

st.title("Web App")

st.header("welcome to my Web App")

st.write("This is my first web app")

st.radio("Gender",['Male','Female'])
st.selectbox("Country",['Nigeria','United States','United Kingdom','Canada','Germany'])

st.text_input("Full Name")

st.text_area("Description")

st.number_input("Age",step=1,min_value=1,max_value=30)

st.date_input("Date of Birth")

st.multiselect("Buy",['Milk','Apples','Potatoes'])

st.checkbox("I agree to terms and conditions")

if st.checkbox("Agree"):
    st.write("Thank you for agreeing")
else:
    st.write("Please agree to terms and conditions")

st.file_uploader("Upload a file",type=['csv','pdf','doc'])

st.sidebar.subheader("WEB GIS")



