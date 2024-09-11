import json
import streamlit as st
import pandas as pd
import altair as alt

# Load the JSON data from the file
with open('weather.json', 'r') as file:
    data = json.load(file)

# Extract temperature data
temperature_data = data['temperature']['data']

# Convert the temperature data to a DataFrame
df = pd.DataFrame(temperature_data)

# Create a Streamlit app to display the temperature data
st.title("Temperature in Each Area")

# Display the temperature data as a bar chart
chart = alt.Chart(df).mark_bar().encode(
    x='place',
    y='value',
    tooltip=['place', 'value', 'unit']
).properties(
    width=800,
    height=400
)
st.altair_chart(chart, use_container_width=True)

# Add a sidebar for user to select a location
selected_place = st.sidebar.selectbox("Select a location", df['place'])

# Display the temperature for the selected location
selected_temp = df[df['place'] == selected_place]['value'].values[0]
selected_unit = df[df['place'] == selected_place]['unit'].values[0]
st.sidebar.write(f"Temperature in {selected_place}: {selected_temp} {selected_unit}")
