import streamlit as st
import pandas as pd


st.title ( " Pleasure to see you Ata Turhan ! ")
st.write("""

Sports and fitness are important for a number of reasons. Physical activity and exercise have been shown to have numerous health benefits, including improving cardiovascular health, strengthening bones and muscles, and reducing the risk of chronic diseases such as obesity, type 2 diabetes, and heart disease.

In addition to the physical benefits, participation in sports and fitness activities can also have a positive impact on mental health. Exercise has been shown to reduce stress and improve mood, and participating in sports can help to build self-esteem, self-confidence, and a sense of community.

Sports and fitness can also be a fun and enjoyable way to spend time with friends and family, and can provide an opportunity to learn new skills and challenge oneself.

Overall, engaging in sports and fitness activities can help to improve overall health and well-being, and is an important aspect of a healthy and balanced lifestyle.

 """)

st.subheader("Don't forget that first rule: stay alive and be healty")
st.write("Here are the four important issue")

st.success("Nutrition:Eating a healthy, balanced diet that is rich in nutrients is essential for maintaining good health. This includes consuming a variety of fruits, vegetables, whole grains, and lean proteins, as well as staying hydrated")
st.success("Exercise: Regular physical activity can help improve cardiovascular health, strengthen bones and muscles, and reduce the risk of chronic conditions such as obesity, type 2 diabetes, and heart disease.")
st.success("Sleep: Getting enough sleep is important for physical and mental well-being. Adults should aim for 7-9 hours of sleep per night.")
st.success("Mental health: Taking care of your mental health is just as important as taking care of your physical health. This includes managing stress, practicing self-care, and seeking help if you are struggling with mental health issues such as depression or anxiety.")

st.subheader('Let check your BMI')
 
# TAKE WEIGHT INPUT in kgs

weight = st.number_input("Enter your weight (in kgs)")
 
# TAKE HEIGHT INPUT
# radio button to choose height format

status = st.radio('Select your height format: ',

                  ('cms', 'meters', 'feet'))
 
# compare status value

if(status == 'cms'):

    # take height input in centimeters

    height = st.number_input('Centimeters')
 

    try:

        bmi = weight / ((height/100)**2)

    except:

        st.text("Enter some value of height")
 

elif(status == 'meters'):

    # take height input in meters

    height = st.number_input('Meters')
 

    try:

        bmi = weight / (height ** 2)

    except:

        st.text("Enter some value of height")
 

else:

    # take height input in feet

    height = st.number_input('Feet')
 

    # 1 meter = 3.28

    try:

        bmi = weight / (((height/3.28))**2)

    except:

        st.text("Enter some value of height")
 
# check if the button is pressed or not

if(st.button('Calculate BMI')):
 

    # print the BMI INDEX

    st.text("Your BMI Index is {}.".format(bmi))
 

    # give the interpretation of BMI index

    if(bmi < 16):

        st.error("You are Extremely Underweight")

    elif(bmi >= 16 and bmi < 18.5):

        st.warning("You are Underweight")

    elif(bmi >= 18.5 and bmi < 25):

        st.success("Healthy")

    elif(bmi >= 25 and bmi < 30):

        st.warning("Overweight")

    elif(bmi >= 30):

        st.error("Extremely Overweight")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.pinimg.com/564x/20/14/5f/20145f90254f60ee33db2358f8f96203.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 