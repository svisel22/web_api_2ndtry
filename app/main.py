import streamlit as st
import requests
import pandas as pd

response = requests.get("http://api.open-notify.org/astros.json")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    number_of_people = data["number"]
    people = data["people"]

    # Display the total number of people in space
    st.write("Total number of people in space:", number_of_people)

    # Display the names of the people in space
    st.write("Names of people in space:")
    for person in people:
        st.write(person["name"])

    # Fetch the current location of the ISS
    location_response = requests.get("http://api.open-notify.org/iss-now.json")

    # Check if the location request was successful
    if location_response.status_code == 200:
        location_data = location_response.json()
        latitude = float(location_data["iss_position"]["latitude"])
        longitude = float(location_data["iss_position"]["longitude"])

        # Create a dataframe with the latitude and longitude values
        df = pd.DataFrame({"LAT": [latitude], "LON": [longitude]})

        # Display the map with the current ISS location
        st.write("Map showing the current location of the ISS:")
        st.map(df)
        
        # Add a short description for the map
        st.write("The marker on the map represents the current location of the International Space Station.")
    else:
        st.write("Error: Unable to retrieve ISS location data from the API")
else:
    st.write("Error: Unable to retrieve data from the API")
