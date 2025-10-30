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
st.subheader("To identify the specific road environments that contribute most significantly to motorbike accidents, thereby enabling targeted safety interventions and resource allocation.")

# --- UPDATED: Summary Box using st.info ---
summary_text = "This chart shows the distribution of road types where accidents occurred. 'Village Road' is the most frequent road type in the dataset, followed by 'Urban Road' and 'Rural Road'. 'Highway' is the least common road type for accidents in this dataset."
st.info(summary_text)

# --- End of Summary Box ---

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
        color='Road Type',  # Color by road type category (Corrected from 'plasma')
        # UPDATED: Using a brighter, distinct qualitative palette (Vivid)
        color_discrete_sequence=px.colors.qualitative.Vivid 
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

if 'Road_condition' in df.columns:
    # 1. Prepare data for Plotly (get counts and ensure order)
    # The 'order=...' logic from your seaborn code is implemented here via value_counts()
    condition_counts = df['Road_condition'].value_counts().reset_index()
    condition_counts.columns = ['Road Condition', 'Count'] # Rename columns for clarity

    # 2. Create the Plotly Bar Chart
    fig = px.bar(
        condition_counts,
        x='Road Condition',
        y='Count',
        title='Distribution of Accidents by Road Condition',
        color='Road Condition',  # Color by road condition category
        # Using a distinct qualitative palette (Deep)
        color_discrete_sequence=px.colors.qualitative.Deep 
    )

    # 3. Customize the layout
    fig.update_layout(
        xaxis_title='Road Condition',
        yaxis_title='Count of Accidents',
        xaxis_tickangle=-45 # Rotate labels for better fit
    )

    # 4. Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Road_condition' column. Please check your data file.")


# Original st.write has been removed as its content is now in st.info()
