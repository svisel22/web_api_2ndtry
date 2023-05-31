import streamlit as st
import requests
#import json


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
else:
    st.write("Error: Unable to retrieve data from the API")