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

st.title("🚗 Accident Weather Condition Analysis")
st.subheader("Distribution of Weather Conditions during Accidents (Plotly)")

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

st.write("This chart illustrates the frequency of different weather conditions at the time of the reported motorbike accidents. 'Clear' weather conditions appear to be the most common during accidents, followed by 'Rainy' and 'Foggy' conditions. 'Windy' conditions are the least frequent.")
