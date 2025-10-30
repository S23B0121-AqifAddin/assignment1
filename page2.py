import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Data Loading (Crucial for the app to run) ---

try:
    # Attempt to load the real data
    # NOTE: Update 'your_data.csv' to the actual filename if needed
    df = pd.read_csv("motorbike_accident_severity.csv")
except FileNotFoundError:
    # Create a dummy DataFrame if the file isn't found
    st.warning("Data file not found. Using dummy data for demonstration.")
    data = {
        'Weather': np.random.choice(['Clear', 'Raining', 'Fog', 'Snowing', 'Windy', 'Overcast'], size=200),
    }
    df = pd.DataFrame(data)

# --- Streamlit Application ---

st.title("Accident Weather Condition Analysis")
st.subheader("To determine if accident frequency remains high during 'Clear' weather relative to adverse conditions (Rainy, Foggy), suggesting that factors beyond weather, such as speed or complacency, are primary contributors to the majority of crashes.")

# --- UPDATED: Summary Box using st.info ---
summary_text = "This chart illustrates the frequency of different weather conditions at the time of the reported motorbike accidents. 'Clear' weather conditions appear to be the most common during accidents, followed by 'Rainy' and 'Foggy' conditions. 'Windy' conditions are the least frequent."
st.info(summary_text)

st.header("1. Weather of Day Analysis")
# --- End of Summary Box --

if 'Weather' in df.columns:
    # 1. Prepare data for Plotly (get counts and reset index)
    weather_counts = df['Weather'].value_counts().reset_index()
    # Explicitly name the columns
    weather_counts.columns = ['Weather Condition', 'Count'] 

    # 2. Create the Plotly Bar Chart
    fig = px.bar(
        weather_counts,
        x='Weather Condition',
        y='Count',
        title='Distribution of Weather Conditions during Accidents',
        color='Weather Condition',  # Color by category
        color_discrete_sequence=px.colors.qualitative.D3 # Choose a color palette
    )

    # 3. Customize the layout
    fig.update_layout(
        xaxis_title='Weather Condition',
        yaxis_title='Count',
        xaxis_tickangle=-45 # Rotate labels for better fit
    )

    # 4. Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Weather' column.")

# --- 3. Time of Day Analysis (New Section) ---
st.header("2. Time of Day Analysis")
st.subheader("To pinpoint peak accident times to optimize enforcement schedules and issue time-specific safety alerts.")

# Summary Box
summary_text_time = "This chart illustrates the frequency of accidents categorized by the time of day. This is crucial for optimizing police patrols and enforcement efforts to target the most dangerous periods for bikers."
st.info(summary_text_time)

if 'Time_of_Day' in df.columns:
    # 1. Prepare data for Plotly (get counts and ensure order)
    time_counts = df['Time_of_Day'].value_counts().reset_index()
    time_counts.columns = ['Time of Day', 'Count'] # Rename columns for clarity

    # 2. Create the Plotly Bar Chart
    fig_time = px.bar(
        time_counts,
        x='Time of Day',
        y='Count',
        title='Distribution of Accidents by Time of Day',
        color='Time of Day',  # Color by time category
        # Using a distinct qualitative palette (Prism)
        color_discrete_sequence=px.colors.qualitative.Prism
    )

    # 3. Customize the layout
    fig_time.update_layout(
        xaxis_title='Time of Day',
        yaxis_title='Count of Accidents',
        xaxis_tickangle=-45 # Rotate labels for better fit
    )

    # 4. Display the chart in Streamlit
    st.plotly_chart(fig_time, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Time_of_Day' column. Please check your data file.")
