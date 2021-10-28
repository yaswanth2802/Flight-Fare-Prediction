'''
Project: Flight Fare Prediction
Author: yaswanth kumar
Date: 28- Oct - 2021
Email: cyk12@iitbbs.ac.in
'''


from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Total_Stops = int(request.form['Total_Stops'])
        Journey_Month=int(request.form['Journey_Month'])
        Journey_Day	=int(request.form['Journey_Day'])
        Journey_Year=int(request.form['Journey_Year'])
        Dep_hour=int(request.form['Dep_hour'])
        Dep_min=int(request.form['Dep_min'])
        Arrival_hour=int(request.form[' Arrival_hour'])
        Arrival_min=int(request.form['Arrival_min'])
        Duration_hour=int(request.form['Duration_hour'])
        Duration_min=int(request.form['Duration_min'])
        Airline_AirIndia=int(request.form[' Airline_AirIndia'])
        Airline_GoAir=int(request.form['Airline_GoAir'])
        Airline_IndiGo=int(request.form['Airline_IndiGo'])
        Airline_Jet_Airways=int(request.form['Airline_Jet Airways'])
        Airline_Jet_Airways_Business=int(request.form['Airline_Jet Airways Business'])
        Airline_Multiplecarriers=int(request.form[' Airline_Multiple carriers'])
        Airline_Multiple_carriers_Premium_economy=int(request.form['Airline_Multiple carriers Premium economy'])
        Airline_SpiceJet=int(request.form['Airline_SpiceJet'])
        Airline_Trujet=int(request.form['Airline_Trujet'])
        Airline_Vistara=int(request.form['Airline_Vistara'])
        Airline_Vistara_Premium_economy=int(request.form['Airline_Vistara Premium economy'])
        Source_Chennai=int(request.form[' Source_Chennai'])
        Source_Delhi=int(request.form['Source_Delhi'])
        Source_Kolkata=int(request.form[' Source_Kolkata'])
        Source_Mumbai=int(request.form['Source_Mumbai'])
        Destination_Cochin=int(request.form['Destination_Cochin'])
        Destination_Delhi=int(request.form['Destination_Delhi'])
        Destination_Hyderabad=int(request.form['Destination_Hyderabad'])
        Destination_Kolkata=int(request.form['Destination_Kolkata'])
        Destination_New_Delhi=int(request.form['Destination_New Delhi'])
        
            
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