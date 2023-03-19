<h1 align="center">
             Mental Disorder Prediction Web App 🩺 💊 💉
</h1>
  
  <img src="Mental Disorders Prediction.png" alt="Mental Disorders Prediction logo" style="height: 400px; width:750px;"/>


This app is used to predict the likeliness of any individual having mental disorders
This includes:->

**1. Anxiety**

**2. Depression**

**3. Suicide**

**4. Bipolar**

**5. Eating Disorder**

**6. PTSD**

## Tech Stacks Used

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

## Libraries Used

<img src="https://img.shields.io/badge/numpy%20-%2314354C.svg?&style=for-the-badge&logo=numpy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas%20-%2314354C.svg?&style=for-the-badge&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/plotly%20-%2314354C.svg?&style=for-the-badge&logo=plotly&logoColor=white"/>
<img src="https://img.shields.io/badge/streamlit%20-%2314354C.svg?&style=for-the-badge&logo=streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/scikitlearn%20-%2314354C.svg?&style=for-the-badge&logo=scikitlearn&logoColor=white"/>

## Structure Of The Project

- Each prediction page is conneceted with a Machine Learning Model which uses Random Forest Classifier to predict the results.
- Also we have used different datasets to train the model for each prediction.
- We can land into each prediction site of the web app from the options in the Navigation Menu.


- Each prediction is done with the help of some features which will be taken as input from the user.
- The most relevant features are taken into consideration for prediction also these features can be found out with simple tests or analysis without visiting any doctor.
- So the individual can get a broad overview of their health condition.

## The features taken into consideration

| Disorders | Features |
| - | - |
| Anxiety | Panic Attack , Heart Rate , Breathing Rate |
| Depression | Anxiety Level, Sadness Level, Insomnia Level, Emptiness Level  |
| Suicide | Self-harm Level, Anxiety Level, Depression Level |
| Bipolar |  Depression Level, Energy Level, Self-harm Level |
| Eating Disorder | Meal Skip, Insomnia Level, Self-harm Probability |
| PTSD | Insomnia Level, Anxiety Level, Self-harm Level | 


## Deployment Of The Project

After the modeling part the model is deployed using Streamlit library on Streamlit Share so that the app is available for usage for everyone.

## Link To My Web Application -

https://sahatonny-cse-350-app-halfn1.streamlit.app/

