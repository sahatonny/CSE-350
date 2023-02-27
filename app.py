#importing all the important libraries
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#building the sidebar of the web app which will help us navigate through the different sections of the entire application
rad=st.sidebar.radio("Navigation Menu",["Home","About","Anxiety","Depression","Suicide","Bipolar","Eating Disorder","PTSD","Plots"])

#Home Page 

#displays all the available disease prediction options in the web app
if rad=="Home":

    st.title("Mental Disorders Prediction App")
    st.image("Mental Disorders Prediction.png",width =600)
    #st.text("In this App following Mental Disorders Pridiction is Available ->")
    #st.text("1. Anxiety")
    #st.text("2. Depression")
    #st.text("3. Heart Disease Predictions")



#About Page

if rad=="About":

    st.title("About")
    #st.header("")
    st.text("This is a web app created using Streamlit.")
    st.text("In this app, we take some input from the user and predict the user of having ")
    st.text("different kinds of mental disorders.")
    #st.image("Mental Disorders Prediction.png",width =600)
    st.markdown("Here these following Mental Disorder Pridiction are Available :-")
    st.text("# Anxiety Prediction")
    st.text("# Depression Prediction")
    st.text("# Suicide Prediction")
    st.text("# Bipolar Prediction")
    st.text("# Eating Disorder Prediction")
    st.text("# PTSD Prediction")

#Anxiety
#loading the Anxiety dataset
df1=pd.read_csv("Anxiety1.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x1) & target(y1)
x1=df1.drop("Prediction",axis=1)
x1=np.array(x1)
y1=pd.DataFrame(df1["Prediction"])
y1=np.array(y1)
#performing train-test split on the data
x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model1=RandomForestClassifier()
#fitting the model with train data (x1_train & y1_train)
model1.fit(x1_train,y1_train)

#Anxiety Page

#heading over to the Anxiety section
if rad=="Anxiety":
    st.header("Know If You Have Anxiety")
    st.image("Anxiety.png",width=200)
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Dry Cough (drycough), Fever (fever), Sore Throat (sorethroat), Breathing Problem (breathingprob)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    #drycough=st.number_input("Panic Attack in a week (0-10)",min_value=0,max_value=10,step=1)
    age=st.number_input("Enter your Age",min_value=0,max_value=100,step=1)
    gender =st.radio('Select Gender',['Male','Female','Prefer not to say'])
    drycough=st.number_input("Panic Attack in a week (0-10)",0,10)
    #fever=st.number_input("Heart Rate in a week(0-100)",min_value=0,max_value=100,step=1)
    fever=st.number_input("Heart Rate in a minute(0-100)",0,100)
    #breathingprob=st.number_input("Breathing Rate in a minute(0-20)",min_value=0,max_value=20,step=1)
    breathingprob=st.number_input("Breathing Rate in a minute(0-20)",0,20)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction1=model1.predict([[drycough,fever,breathingprob]])[0]
    
    #prediction part predicts whether the person is affected by Covid-19 or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if prediction1=="Yes":
            st.warning("You Have Anxiety")
        elif prediction1=="yes":
            st.warning("You Have Anxiety")
        elif prediction1=="No":
            st.success("You Are Safe")
        elif prediction1=="YES":
            st.warning("You Have Anxiety")
        elif prediction1=="NO":
            st.success("You Are Safe")
        elif prediction1=="no":
            st.success("You Are Safe")



#Depression Prediction

#loading Depression dataset
df2=pd.read_csv("Depression1.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x3) & target(y3)
x2=df2.iloc[:,[0,1,2,3]].values
x2=np.array(x2)
y2=y2=df2.iloc[:,[-1]].values
y2=np.array(y2)
#performing train-test split on the data
x2_train,x2_test,y2_train,y2_test=train_test_split(x2,y2,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model2=RandomForestClassifier()
#fitting the model with train data (x2_train & y2_train)
model2.fit(x2_train,y2_train)

#Depression Page

#heading over to the Depression section
if rad=="Depression":
    st.header("Know If You Have Depression")
    st.image("Depression.png",width=200)
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Chest Pain (chestpain), Blood Pressure-BP (bp), Cholestrol (cholestrol), Maximum HR (maxhr)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    age=st.number_input("Enter your Age (0-100)",min_value=0,max_value=100,step=1)
    gender =st.radio('Select Gender',['Male','Female','Prefer not to say'])
    chestpain=st.number_input("Rate Your Anxiety level (0-5)",min_value=0,max_value=5,step=1)
    bp=st.number_input("Rate Your Blood Sadness level (0-10)",min_value=0,max_value=10,step=1)
    cholestrol=st.number_input("Rate Your Insomnia level(0-10)",min_value=0,max_value=10,step=1)
    maxhr=st.number_input("Rate You Emptiness level(0-5)",min_value=0,max_value=5,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction2=model2.predict([[chestpain,bp,cholestrol,maxhr]])[0]


    #prediction part predicts whether the person is affected by Heart Disease or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if str(prediction2)=="Yes":
            st.warning("You Might Have Depression")
        elif str(prediction2)=="yes":
            st.warning("You Might Have Depression")
        elif str(prediction2)=="No":
            st.success("You Are Safe")
        elif str(prediction2)=="YES":
            st.warning("You Might Have Depression")
        elif str(prediction2)=="NO":
            st.success("You Are Safe")
        elif prediction2=="no":
            st.success("You Are Safe")


#Suicide Prediction

#loading the Suicide dataset
df3=pd.read_csv("Suicide1.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x3) & target(y3)
x3=df3.iloc[:,[0,1,2]].values
x3=np.array(x3)
y3=y3=df3.iloc[:,[-1]].values
y3=np.array(y3)
#performing train-test split on the data
x3_train,x3_test,y3_train,y3_test=train_test_split(x3,y3,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model3=RandomForestClassifier()
#fitting the model with train data (x3_train & y3_train)
model3.fit(x3_train,y3_train)

#Suicide Page

#heading over to the Suicide section
if rad=="Suicide":
    st.header("Know If You Are Suicidal")
    st.image("Therapy.png",width=200)
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Chest Pain (chestpain), Blood Pressure-BP (bp), Cholestrol (cholestrol), Maximum HR (maxhr)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    age=st.number_input("Enter your Age (0-100)",min_value=0,max_value=100,step=1)
    gender =st.radio('Select Gender',['Male','Female','Prefer not to say'])
    
    bipolar= st.radio("Select if diagnosed with bipolarity",['Yes','No'])
    suicide= st.radio("Select if previous record of suicide attempt",['Yes','No'])
  
    chestpain=st.number_input("Rate Your Depression Level(0-10)",min_value=0,max_value=10,step=1)
    bp=st.number_input("Enter Your Anxiety Level(0-10)",min_value=0,max_value=10,step=1)
    cholestrol=st.number_input("Probability of Self-harm(0-5)",min_value=0,max_value=5,step=1)
    #maxhr=st.number_input("Enter You Maximum Heart Rate (70-200)",min_value=70,max_value=200,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction3=model3.predict([[chestpain,bp,cholestrol]])[0]
    
    #prediction part predicts whether the person is affected by Heart Disease or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if str(prediction3)=="Yes":
            st.warning("You Are in Danger!")
        elif str(prediction3)=="yes":
            st.warning("You Are in Danger!")
        elif str(prediction3)=="YES":
            st.warning("You Are in Danger!")
        elif str(prediction3)=="No":
            st.success("You Are Safe!")
        elif str(prediction3)=="NO":
            st.success("You Are Safe!")
        elif prediction3=="no":
            st.success("You Are Safe!")


#Bipolar Prediction

#loading the Bipolar dataset
df4=pd.read_csv("Bipolar.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x3) & target(y3)
x4=df4.iloc[:,[0,1,2]].values
x4=np.array(x4)
y4=y4=df4.iloc[:,[-1]].values
y4=np.array(y4)
#performing train-test split on the data
x4_train,x4_test,y4_train,y4_test=train_test_split(x4,y4,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model4=RandomForestClassifier()
#fitting the model with train data (x3_train & y3_train)
model4.fit(x4_train,y4_train)

#Bipolar Page

#heading over to the Bipolar section
if rad=="Bipolar":
    st.header("Know If You Are Bipolar")
    st.image("Bipolar.png",width=200)
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Chest Pain (chestpain), Blood Pressure-BP (bp), Cholestrol (cholestrol), Maximum HR (maxhr)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    age=st.number_input("Enter your Age (0-100)",min_value=0,max_value=100,step=1)
    gender =st.radio('Select Gender',['Male','Female','Prefer not to say'])
    
    bipolar= st.radio("Select if previous record of manic episode",['Yes','No'])
    suicide= st.radio("Select if previous record of suicide attempt",['Yes','No'])
  
    chestpain=st.number_input("Rate Your Depression Level(0-10)",min_value=0,max_value=10,step=1)
    bp=st.number_input("Rate of Energy Level(0-10)",min_value=0,max_value=10,step=1)
    cholestrol=st.number_input("Probability of Self-harm(0-5)",min_value=0,max_value=10,step=1)
    #maxhr=st.number_input("Enter You Maximum Heart Rate (70-200)",min_value=70,max_value=200,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction4=model4.predict([[chestpain,bp,cholestrol]])[0]
    
    #prediction part predicts whether the person is affected by Heart Disease or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if str(prediction4)=="Yes":
            st.warning("You Have Bipolar")
        elif str(prediction4)=="yes":
            st.warning("You Have Bipolar")
        elif str(prediction4)=="YES":
            st.warning("You Have Bipolar")
        elif str(prediction4)=="No":
            st.success("You Are Okay!")
        elif str(prediction4)=="NO":
            st.success("You Are Okay!")
        elif prediction4=="no":
            st.success("You Are Okay!")



#Eating Disorder

#loading the Bipolar dataset
df5=pd.read_csv("Eating Disorder.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x3) & target(y3)
x5=df5.iloc[:,[0,1,3]].values
x5=np.array(x4)
y5=y5=df5.iloc[:,[-2]].values
y5=np.array(y5)
#performing train-test split on the data
x5_train,x5_test,y5_train,y5_test=train_test_split(x5,y5,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model5=RandomForestClassifier()
#fitting the model with train data (x3_train & y3_train)
model5.fit(x5_train,y5_train)

#Eating Disorder Page

#heading over to the Bipolar section
if rad=="Eating Disorder":
    st.header("Know If Have Eating Disorder")
    st.image("Anxiety.png",width=200)
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Chest Pain (chestpain), Blood Pressure-BP (bp), Cholestrol (cholestrol), Maximum HR (maxhr)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    age=st.number_input("Enter your Age (0-100)",min_value=0,max_value=100,step=1)
    gender =st.radio('Select Gender',['Male','Female','Prefer not to say'])
    
    bipolar= st.radio("Select if family history with eating disorder",['Yes','No'])
    suicide= st.radio("Select if previous record of suicide attempt",['Yes','No'])
  
    chestpain=st.number_input("Number of meal skip in a day (0-3)",min_value=0,max_value=3,step=1)
    bp=st.number_input("Insomnia Level (0-5)",min_value=0,max_value=5,step=1)
    cholestrol=st.number_input("Probability of Self-harm(0-5)",min_value=0,max_value=5,step=1)
    #maxhr=st.number_input("Enter You Maximum Heart Rate (70-200)",min_value=70,max_value=200,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction5=model5.predict([[chestpain,bp,cholestrol]])[0]
    
    #prediction part predicts whether the person is affected by Heart Disease or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if str(prediction5)=="Yes":
            st.warning("You Have Eating Disorder")
        elif str(prediction5)=="yes":
            st.warning("You Have Eating Disorder")
        elif str(prediction5)=="YES":
            st.warning("You Have Eating Disorder")
        elif str(prediction5)=="No":
            st.success("You Are Okay!")
        elif str(prediction5)=="NO":
            st.success("You Are Okay!")
        elif prediction5=="no":
            st.success("You Are Okay!")



#PTSD Prediction

#loading the PTSD dataset
df6=pd.read_csv("PTSD.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x3) & target(y3)
x6=df6.iloc[:,[0,1,2]].values
x6=np.array(x6)
y6=y6=df6.iloc[:,[-1]].values
y6=np.array(y6)
#performing train-test split on the data
x6_train,x6_test,y6_train,y6_test=train_test_split(x6,y6,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model6=RandomForestClassifier()
#fitting the model with train data (x3_train & y3_train)
model6.fit(x6_train,y6_train)

#PTSD Page

#heading over to the Bipolar section
if rad=="PTSD":
    st.header("Know If You Have PTSD")
    st.image("Therapy.png",width=200)
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Chest Pain (chestpain), Blood Pressure-BP (bp), Cholestrol (cholestrol), Maximum HR (maxhr)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    age=st.number_input("Enter your Age (0-100)",min_value=0,max_value=100,step=1)
    gender =st.radio('Select Gender',['Male','Female','Prefer not to say'])
    
    bipolar= st.radio("Select if previous record of self_harm",['Yes','No'])
    suicide= st.radio("Select if previous record of suicide attempt",['Yes','No'])
  
    chestpain=st.number_input("Insomnia Level(0-10)",min_value=0,max_value=10,step=1)
    bp=st.number_input("Anxiety Level(0-10)",min_value=0,max_value=10,step=1)
    cholestrol=st.number_input("Self-harm  Level(0-10)",min_value=0,max_value=10,step=1)
    #maxhr=st.number_input("Enter You Maximum Heart Rate (70-200)",min_value=70,max_value=200,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction6=model6.predict([[chestpain,bp,cholestrol]])[0]
    
    #prediction part predicts whether the person is affected by Heart Disease or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if str(prediction6)=="Yes":
            st.warning("You Have PTSD")
        elif str(prediction6)=="yes":
            st.warning("You Have PTSD")
        elif str(prediction6)=="YES":
            st.warning("You Have PTSD")
        elif str(prediction6)=="No":
            st.success("You Are Okay!")
        elif str(prediction6)=="NO":
            st.success("You Are Okay!")
        elif prediction6=="no":
            st.success("You Are Safe")







if rad=="Plots":
    #
    type=st.selectbox("Which Plot Do You Want To See?",["Anxiety","Depression","Suicide","Bipolar","Eating Disorder","PTSD"])
    if type=="Anxiety":
        fig=px.scatter(df1,x="Panic attack in a week (0-10)",y="Prediction")
        #st.plotly_chart(fig)
        st.line_chart(df1)
        
        #st.map(df1)

    elif type=="Depression":
        fig=px.scatter(df2,x="Emptiness level(0-5)",y="Insomnia level(0-10)")
        #st.plotly_chart(fig)
        st.bar_chart(df2)
        #st.line_chart(df2)
        #st.pydeck_chart(df2)
        
    elif type=="Suicide":
        fig=px.scatter(df3,x="Probability of Self-harm(0-5)",y="Prediction")
        #st.plotly_chart(fig)
        st.area_chart(df3)
    elif type=="Bipolar":
        fig=px.scatter(df4,x="Probability of Self-harm(0-5)",y="Prediction")
        st.line_chart(df4)

    elif type=="Eating Disorder":
        fig=px.scatter(df5,x="Insomnia Level (0-5)",y="Prediction")
        st.bar_chart(df5)

    elif type=="PTSD":
        fig=px.scatter(df6,x="Insomnia Level(0-10)",y="Prediction")
        st.area_chart(df6)

                                        
    


