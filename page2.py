import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# Removed: import matplotlib.pyplot as plt
# Removed: import seaborn as sns 
# NOTE: We keep Plotly Express (px) as the primary visualization library

# --- Data Loading (Crucial for the app to run) ---

try:
    # Attempt to load the real data
    # NOTE: Update 'your_data.csv' to the actual filename if needed
    df = pd.read_csv("motorbike_accident_severity.csv")
except FileNotFoundError:
    # Create a dummy DataFrame if the file isn't found
    st.warning("Data file not found. Using dummy data for demonstration.")
    # Dummy data must include all required columns for the app to run completely.
    size = 200
    data = {
        'Weather': np.random.choice(['Clear', 'Raining', 'Fog', 'Snowing', 'Windy', 'Overcast'], size=size),
        'Accident_Severity': np.random.choice(['Slight', 'Serious', 'Fatal'], size=size),
        'Time_of_Day': np.random.choice(['Morning (6-12)', 'Afternoon (12-18)', 'Evening (18-24)', 'Night (0-6)'], size=size),
    }
    df = pd.DataFrame(data)

# --- Streamlit Application ---

st.title("Accident Weather Condition Analysis")
st.subheader("To determine if accident frequency remains high during 'Clear' weather relative to adverse conditions (Rainy, Foggy), suggesting that factors beyond weather, such as speed or complacency, are primary contributors to the majority of crashes.")

# --- 1. Weather of Day Analysis (Plotly) ---
st.header("1. Weather of Day Analysis")
summary_text = "This chart illustrates the frequency of different weather conditions at the time of the reported motorbike accidents. 'Clear' weather conditions appear to be the most common during accidents, followed by 'Rainy' and 'Foggy' conditions. 'Windy' conditions are the least frequent."
st.info(summary_text)

if 'Weather' in df.columns:
    weather_counts = df['Weather'].value_counts().reset_index()
    weather_counts.columns = ['Weather Condition', 'Count'] 

    fig_weather = px.bar(
        weather_counts,
        x='Weather Condition',
        y='Count',
        title='Distribution of Weather Conditions during Accidents',
        color='Weather Condition',  
        color_discrete_sequence=px.colors.qualitative.D3
    )

    fig_weather.update_layout(
        xaxis_title='Weather Condition',
        yaxis_title='Count',
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig_weather, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Weather' column.")

# --- 2. Time of Day Analysis (Plotly) ---
st.header("2. Time of Day Analysis")
st.subheader("To pinpoint peak accident times to optimize enforcement schedules and issue time-specific safety alerts.")

summary_text_time = "This chart illustrates the frequency of accidents categorized by the time of day. This is crucial for optimizing police patrols and enforcement efforts to target the most dangerous periods for bikers."
st.info(summary_text_time)

if 'Time_of_Day' in df.columns:
    time_counts = df['Time_of_Day'].value_counts().reset_index()
    time_counts.columns = ['Time of Day', 'Count']

    fig_time = px.bar(
        time_counts,
        x='Time of Day',
        y='Count',
        title='Distribution of Accidents by Time of Day',
        color='Time of Day',  
        color_discrete_sequence=px.colors.qualitative.Prism
    )

    fig_time.update_layout(
        xaxis_title='Time of Day',
        yaxis_title='Count of Accidents',
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig_time, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Time_of_Day' column. Please check your data file.")

# --- 3. Relationship between Weather and Accident Severity (Plotly Stacked Bar) ---
st.header("3. Relationship between Weather and Accident Severity (Stacked)")
summary_text_severity = "This stacked chart displays accident counts grouped by weather and segmented by severity. This helps determine if certain weather types lead to a disproportionately higher number of fatal or serious crashes."
st.info(summary_text_severity)

if 'Weather' in df.columns and 'Accident_Severity' in df.columns:

    st.subheader("Stacked Bar Chart of Accident Severity by Weather Condition")

    # Use Plotly Express to create the stacked bar chart directly
    fig_severity = px.histogram(
        df,
        x='Weather',
        color='Accident_Severity',
        barmode='stack', # This creates the stacked effect
        title='Accident Severity by Weather Condition (Stacked)',
        labels={'Weather': 'Weather Condition', 'count': 'Number of Accidents'},
        color_discrete_sequence=px.colors.qualitative.Prism # Choosing a color-blind safe palette
    )

    # Customize layout and axis labels
    fig_severity.update_layout(
        xaxis_title='Weather Condition',
        yaxis_title='Number of Accidents (Count)',
        xaxis_tickangle=-45,
        legend_title="Severity"
    )
    
    # Ensure all bars are clearly visible
    fig_severity.update_xaxes(categoryorder='total descending')

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_severity, use_container_width=True)
    
else:
    st.error("DataFrame must contain 'Weather' and 'Accident_Severity' columns.")
