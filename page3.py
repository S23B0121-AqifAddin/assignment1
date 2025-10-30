import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Data Loading (Placeholder for your DataFrame 'df') ---
# NOTE: The dummy data now includes both 'Road_Type' and 'Road_condition'
try:
    df = pd.read_csv("motorbike_accident_severity.csv") 
except FileNotFoundError:
    st.warning("Data file not found. Using dummy data for demonstration.")
    data = {
        'Road_Type': np.random.choice(['Single Carriageway', 'Dual Carriageway', 'Roundabout', 'Motorway', 'Slip Road'], size=500),
        'Road_condition': np.random.choice(['Dry', 'Wet / Damp', 'Snow', 'Frost / Ice', 'Flood'], size=500),
    }
    df = pd.DataFrame(data)

# --- Streamlit Application ---

st.title("🏍️ Motorbike Accident Distribution Analysis")

# --- 1. Road Type Analysis ---
st.header("1. Road Type Analysis")
st.subheader("To identify the specific road environments that contribute most significantly to motorbike accidents, thereby enabling targeted safety interventions and resource allocation.")

# Summary Box
summary_text_type = "This chart shows the distribution of accidents across different road types. This analysis helps determine where resources (like widening or speed limit enforcement) should be concentrated."
st.info(summary_text_type)

if 'Road_Type' in df.columns:
    # 1. Prepare data for Plotly (get counts and ensure order)
    road_type_counts = df['Road_Type'].value_counts().reset_index()
    road_type_counts.columns = ['Road Type', 'Count'] # Rename columns for clarity

    # 2. Create the Plotly Bar Chart
    fig_type = px.bar(
        road_type_counts,
        x='Road Type',
        y='Count',
        title='Distribution of Accidents by Road Type',
        color='Road Type',  # Color by road type category
        color_discrete_sequence=px.colors.qualitative.Vivid 
    )

    # 3. Customize the layout
    fig_type.update_layout(
        xaxis_title='Road Type',
        yaxis_title='Count',
        xaxis_tickangle=-45 # Rotate labels for better fit
    )

    # 4. Display the chart in Streamlit
    st.plotly_chart(fig_type, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Road_Type' column.")


st.markdown("---") # Separator for clarity

# --- 2. Road Condition Analysis ---
st.header("2. Road Condition Analysis")
st.subheader("To assess the correlation between road surface condition and accident frequency, prioritizing maintenance and hazard warnings.")

# Summary Box
summary_text_condition = "This chart illustrates the frequency of accidents by the condition of the road surface at the time of the crash. This analysis helps identify road surface hazards (like ice or wet surfaces) that contribute most to accidents."
st.info(summary_text_condition)

if 'Road_condition' in df.columns:
    # 1. Prepare data for Plotly (get counts and ensure order)
    condition_counts = df['Road_condition'].value_counts().reset_index()
    condition_counts.columns = ['Road Condition', 'Count'] # Rename columns for clarity

    # 2. Create the Plotly Bar Chart
    fig_condition = px.bar(
        condition_counts,
        x='Road Condition',
        y='Count',
        title='Distribution of Accidents by Road Condition',
        color='Road Condition',  # Color by road condition category
        color_discrete_sequence=px.colors.qualitative.Vivid # Using the Deep palette
    )

    # 3. Customize the layout
    fig_condition.update_layout(
        xaxis_title='Road Condition',
        yaxis_title='Count of Accidents',
        xaxis_tickangle=-45 # Rotate labels for better fit
    )

    # 4. Display the chart in Streamlit
    st.plotly_chart(fig_condition, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Road_condition' column. Please check your data file.")

st.title("Accident Analysis Dashboard: Motorbike Safety")
st.subheader("Key factors influencing motorbike accident frequency and severity.")

# --- 1. Weather of Day Analysis (Plotly) ---
st.header("1. Weather of Day Analysis")
# ... (Previous code for Weather chart) ...
# (Keeping this section collapsed for brevity)
if 'Weather' in df.columns:
    weather_counts = df['Weather'].value_counts().reset_index()
    weather_counts.columns = ['Weather Condition', 'Count'] 
    fig_weather = px.bar(weather_counts, x='Weather Condition', y='Count', title='Distribution of Weather Conditions during Accidents', color='Weather Condition', color_discrete_sequence=px.colors.qualitative.D3)
    fig_weather.update_layout(xaxis_title='Weather Condition', yaxis_title='Count', xaxis_tickangle=-45)
    st.plotly_chart(fig_weather, use_container_width=True)
else:
    st.error("The DataFrame does not contain a 'Weather' column.")

# --- 2. Time of Day Analysis (Plotly) ---
st.header("2. Time of Day Analysis")
# ... (Previous code for Time of Day chart) ...
# (Keeping this section collapsed for brevity)
if 'Time_of_Day' in df.columns:
    time_counts = df['Time_of_Day'].value_counts().reset_index()
    time_counts.columns = ['Time of Day', 'Count']
    fig_time = px.bar(time_counts, x='Time of Day', y='Count', title='Distribution of Accidents by Time of Day', color='Time of Day', color_discrete_sequence=px.colors.qualitative.Prism)
    fig_time.update_layout(xaxis_title='Time of Day', yaxis_title='Count of Accidents', xaxis_tickangle=-45)
    st.plotly_chart(fig_time, use_container_width=True)
else:
    st.error("The DataFrame does not contain a 'Time_of_Day' column.")

# --- 3. Relationship between Weather and Accident Severity (Plotly Stacked Bar) ---
st.header("3. Relationship between Weather and Accident Severity")
# ... (Previous code for Weather vs Severity chart) ...
# (Keeping this section collapsed for brevity)
if 'Weather' in df.columns and 'Accident_Severity' in df.columns:
    fig_severity_weather = px.histogram(df, x='Weather', color='Accident_Severity', barmode='stack', title='Accident Severity by Weather Condition (Stacked)', labels={'Weather': 'Weather Condition', 'count': 'Number of Accidents'}, category_orders={"Accident_Severity": ['Slight', 'Serious', 'Fatal']}, color_discrete_sequence=px.colors.qualitative.T10)
    fig_severity_weather.update_layout(xaxis_title='Weather Condition', yaxis_title='Number of Accidents (Count)', xaxis_tickangle=-45, legend_title="Severity")
    fig_severity_weather.update_xaxes(categoryorder='total descending')
    st.plotly_chart(fig_severity_weather, use_container_width=True)
else:
    st.error("DataFrame must contain 'Weather' and 'Accident_Severity' columns.")

# --- 4. Relationship between Road Condition and Accident Severity (Plotly Stacked Bar) ---
st.header("3. Relationship between Road Condition and Accident Severity")
st.subheader("Severity of Accidents by Road Condition")

summary_text_road = "This stacked chart visualizes how accident severity levels change based on the road surface condition (Dry, Wet, Icy, etc.). This is crucial for identifying risks associated with poor road traction."
st.info(summary_text_road)

if 'Road_condition' in df.columns and 'Accident_Severity' in df.columns:
    
    # Use Plotly Express's histogram for the stacked bar chart
    fig_severity_road = px.histogram(
        df,
        x='Road_condition',
        color='Accident_Severity',
        barmode='stack', # Key setting for a stacked bar chart
        title='Accident Severity by Road Condition (Stacked)',
        labels={'Road_condition': 'Road Condition', 'count': 'Number of Accidents'},
        # Ensure severity order is logical
        category_orders={"Accident_Severity": ['Slight', 'Serious', 'Fatal']},
        # Using a palette similar to 'plasma' but in Plotly (like Inferno or a custom sequence)
        color_discrete_sequence=px.colors.sequential.Plasma_r 
    )

    # Apply customizations matching the Matplotlib style
    fig_severity_road.update_layout(
        xaxis_title='Road Condition',
        yaxis_title='Number of Accidents (Count)',
        xaxis_tickangle=-45,
        legend_title="Severity"
    )
    
    # Sort the bars by the total count for better readability
    fig_severity_road.update_xaxes(categoryorder='total descending')

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_severity_road, use_container_width=True)
    
else:
    st.error("DataFrame must contain 'Road_condition' and 'Accident_Severity' columns.")
