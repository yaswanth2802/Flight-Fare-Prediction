import streamlit as st
#from PIL import Image
import pickle
import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dir,"running_logs.log"),level=logging.INFO, format=logging_str, filemode="a")


model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
 
logging.info("*****"*10)

def run():
    #img1 = Image.open('flight.jpg')
    #img1 = img1.resize((300, 200))
    #st.image(img1, use_column_width=False)
    st.title("Flight Price Prediction using Machine Learning")
    st.subheader('Please Enter the following details to Predict Flight Price')


     # ------ Airlines----------
    Airline_Air_India =0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_Jet_Airways = 0
    Airline_Jet_Airways_Business = 0
    Airline_Multiplecarriers = 0
    Airline_Multiplecarriers_Premiumeconomy = 0
    Airline_SpiceJet=0
    Airline_Trujet=0
    Airline_Vistara = 0
    Airline_Vistara_Premiumeconomy = 0

    # ---- Source ------------

    Source_Chennai = 0
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 0

    # -------- Destination ---------

    Destination_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0
    Destination_New_Delhi =0
    Destination_Cochin=0
    # --------Additional Info----
    
    col1, col2 , col3 = st.columns(3)

    with col1:
        # Total stop
        total_stop = 0
        ts = st.radio('Select Number of Stops:',['Non_stop','1 stop','2 stop','3 stop','4 stop'])
        if ts == 'Non_stop':
            total_stop = 0
        elif ts =='1 stop':
            total_stop = 1
        elif ts =='2 stop':
            total_stop = 2
        elif ts == '3 stop':
            total_stop = 3
        else:
            total_stop = 4

        # Journey Day
        journey_day = st.number_input('Select Journey Date: ',min_value=1,max_value=31,value=15,step=1)

        # Journey Month
        journey_month = st.number_input('Select Journey month: ',min_value=1,max_value=12,value=6,step=1)



    with col2:
        # Dept Hour and Min

        #hr = st.time_input('Enter Hour and Min for Departure:')
        dep_hr=  st.number_input('Select departure Hour: ',min_value=0,max_value=24,value=12,step=1)
        
        dep_min =  st.number_input('Select departure minute: ',min_value=0,max_value=60,value=30,step=1)

        # Arrival Hour and Min
        arrival_hr= st.number_input('Select arrival Hour: ',min_value=1,max_value=24,value=12,step=1)
        
        arrival_min = st.number_input('Select arrival minute: ',min_value=1,max_value=60,value=30,step=1)
        #hr2 = st.time_input('Enter Hour and Min for Arrival:')

        #arrival_hr = hr2.hour
        #arrival_min = hr2.minute

        # Duration
        
        dur_min = st.slider('Enter flight duration in minutes: ',1,600,1)
        dur_hr =dur_min//60
        dur_min=dur_min-60*dur_hr
        # Airline
        airline_list = ['Air India','GoAir','IndiGo','Jet Airways','Jet Airways Business',
              'Multiple carriers','Multiple carriers Premium economy','SpiceJet','Trujet','Vistara','Vistara Premium economy']

        al = st.selectbox('Select Airline Details: ', airline_list)
        if al =='Air India':
            Airline_Air_India = 1
        elif al == 'GoAir':
            Airline_GoAir = 1
        elif al == 'Indigo':
            Airline_IndiGo = 1
        elif al == 'Jet Airways':
            Airline_Jet_Airways = 1
        elif al == 'Jet Airways Business':
            Airline_Jet_Airways_Business = 1
        elif al == 'Multiple carriers':
            Airline_Multiplecarriers = 1
        elif al == 'Multiple carriers Premium economy':
            Airline_Multiplecarriers_Premiumeconomy = 1
        elif al == 'SpiceJet':
            Airline_SpiceJet = 1
        elif al == 'Trujet':
            Airline_Trujet = 1
        elif al == 'Vistara':
            Airline_Vistara = 1
        else:
            Airline_Vistara_Premiumeconomy = 1

    with col3:     # Source

        source_list = ['Chennai','Delhi','Kolkata','Mumbai']
        sr = st.selectbox('Select Source Details: ', source_list)
        if sr == 'Chennai':
            Source_Chennai = 1
        elif sr == 'Delhi':
            Source_Delhi = 1
        elif sr == 'Kolkata':
            Source_Kolkata = 1
        else:
            Source_Mumbai = 1

        # Destination
        dest_list = ['Delhi','Hyderabad','Kolkata','New Delhi','Cochin']
        dest = st.selectbox('Select Destination Details: ', dest_list)
        if dest == 'Delhi':
            Destination_Delhi = 1
        elif dest == 'Hyderabad':
            Destination_Hyderabad = 1
        elif dest == 'Kolkata':
            Destination_Kolkata = 1
        elif dest == 'Cochin':
            Destination_Cochin= 1
        else:
            Destination_New_Delhi = 1

         # Additional Info
        
       



    features = [total_stop,journey_day,journey_month,dep_hr,dep_min,arrival_hr,arrival_min,dur_hr,dur_min,
                     Airline_Air_India,Airline_GoAir,Airline_IndiGo,Airline_Jet_Airways,Airline_Jet_Airways_Business,
                     Airline_Multiplecarriers,Airline_Multiplecarriers_Premiumeconomy,Airline_SpiceJet,Airline_Trujet,Airline_Vistara,Airline_Vistara_Premiumeconomy,
                     Source_Chennai,Source_Delhi,Source_Kolkata,Source_Mumbai,Destination_Cochin,Destination_Delhi,Destination_Hyderabad,
                     Destination_Kolkata,Destination_New_Delhi,]

    logging.info(features)

    if st.button("Predict Flight Price"):
        predictions = model.predict([features])[0]
        logging.info(predictions)
        st.success(f'The Predicted Flight Price is {predictions}')

logging.info("*****"*10)

run()
logging.info("****"*20)
 #streamlit run app.py --browser.gatherUsageStats false

