import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Data Loading (Placeholder for your DataFrame 'df') ---
# NOTE: Replace this with your actual data loading code if it's not present elsewhere
try:
    df = pd.read_csv("motorbike_accident_severity.csv") 
except FileNotFoundError:
    st.warning("Data file not found. Using dummy data for demonstration.")
    data = {
        'Road_Type': np.random.choice(['Single Carriageway', 'Dual Carriageway', 'Roundabout', 'Motorway', 'Slip Road'], size=200),
    }
    df = pd.DataFrame(data)

# --- Streamlit Application ---

st.title("🛣️ Road Type Analysis")
st.subheader("Distribution of Road Types During Accidents")

if 'Road_Type' in df.columns:
    # 1. Prepare data for Plotly (get counts and ensure order)
    road_type_counts = df['Road_Type'].value_counts().reset_index()
    road_type_counts.columns = ['Road Type', 'Count'] # Rename columns for clarity

    # 2. Create the Plotly Bar Chart
    fig = px.bar(
        road_type_counts,
        x='Road Type',
        y='Count',
        title='Distribution of Road Type',
        color='Road Type',  # Color by road type category
        color_discrete_sequence=px.colors.sequential.Cividis # Use a sequential color scheme similar to 'cividis'
    )

    # 3. Customize the layout
    fig.update_layout(
        xaxis_title='Road Type',
        yaxis_title='Count',
        xaxis_tickangle=-45 # Rotate labels for better fit
    )

    # 4. Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Road_Type' column.")
