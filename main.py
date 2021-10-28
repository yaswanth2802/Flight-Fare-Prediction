'''
Project: Flight Fare Prediction
Author: yaswanth kumar
Date: 28- Oct - 2021
Email: cyk12@iitbbs.ac.in
'''
from datetime import datetime
import pandas as pd
from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    Airline_AirIndia=0
    Airline_GoAir=0
    Airline_IndiGo=0
    Airline_Jet_Airways=0
    Airline_Jet_Airways_Business=0
    Airline_Multiplecarriers=0
    Airline_Multiple_carriers_Premium_economy=0
    Airline_SpiceJet=0
    Airline_Trujet=0
    Airline_Vistara=0
    Airline_Vistara_Premium_economy=0
    Source_Chennai=0
    Source_Delhi=0
    Source_Kolkata=0
    Source_Mumbai=0
    Destination_Cochin=0
    Destination_Delhi=0
    Destination_Hyderabad=0
    Destination_Kolkata=0
    Destination_New_Delhi=0


    if request.method == 'POST':
        Dep_time=str(request.form['journey_time'])
        Arrival_time=str(request.form['journey_time'])
        Duration_time=str(request.form['journey_time'])
        journey_date=str(request.form['journey_date'])
        Total_Stops = int(request.form['Total_Stops'])
        Journey_Month=datetime.strptime(journey_date,format = "%d/%m/%Y").month
        Journey_Day	=datetime.strptime(journey_date,format = "%d/%m/%Y").day
        Journey_Year=datetime.strptime(journey_date,format = "%d/%m/%Y").year
        Dep_hour=datetime.strptime(Dep_time,"%H:%M").hour
        Dep_min=datetime.strptime(Dep_time,"%H:%M").min
        Arrival_hour=datetime.strptime(Arrival_time,"%H:%M").hour
        Arrival_min=datetime.strptime(Arrival_time,"%H:%M").min
        Duration_hour=datetime.strptime(Duration_time,"%H:%M").hour
        Duration_min=datetime.strptime(Duration_time,"%H:%M").min
        Airline=str(request.form['Airline'])
        Source=str(request.form['Source'])
        Destination=str(request.form['Source'])

        
        if Airline=="AirIndia":
            Airline_AirIndia=1
        elif Airline=="GoAir":
            Airline_GoAir=1
        elif Airline=="IndiGo":
            Airline_IndiGo=1
        elif Airline=="Jet_Airways":
            Airline_Jet_Airways=1
        elif Airline=="Jet_Airways_Business":
            Airline_Jet_Airways_Business=1
        elif Airline=="Multiplecarriers":
            Airline_Multiplecarriers=1
        elif Airline=="Multiple_carriers_Premium_economy":
            Airline_Multiple_carriers_Premium_economy=1
        elif Airline=="SpiceJet":
            Airline_SpiceJet=1
        elif Airline=="Trujet":
            Airline_Trujet=1
        elif Airline=="Vistara":
            Airline_Vistara=1
        elif Airline=="Vistara_Premium_economy":
            Airline_Vistara_Premium_economy=1

        if Source=="Chennai":
            Source_Chennai=1
        elif Source=="Delhi":
            Source_Delhi=1
        elif Source=="Kolkata":
            Source_Kolkata=1
        elif Source=="Mumbai":
            Source_Mumbai=1  
        
        if Destination=="Cochin":
            Destination_Cochin=1
        elif Destination=="Delhi":
            Destination_Delhi=1
        elif Destination=="Kolkata":
            Destination_Kolkata=1
        elif Destination=="Hyderabad":
            Destination_Hyderabad=1  
        elif Destination=="New_Delhi":
            Destination_New_Delhi=1
        


        prediction=model.predict([[Total_Stops,Journey_Month,Journey_Day,Journey_Year,Dep_hour,Dep_min,Arrival_hour,Arrival_min,Duration_hour,Duration_min,Airline_AirIndia,Airline_GoAir,Airline_IndiGo,
        Airline_Jet_Airways,Airline_Jet_Airways_Business,Airline_Multiplecarriers,Airline_Multiple_carriers_Premium_economy,Airline_SpiceJet,
        Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium_economy,Source_Chennai,Source_Delhi,Source_Kolkata,Source_Mumbai,Destination_Cochin,Destination_Delhi,Destination_Hyderabad,Destination_Kolkata,Destination_New_Delhi]])
        output=round(prediction[0],2)
        if output<=0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)