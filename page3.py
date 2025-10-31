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
    # Added dummy 'Accident_Severity' to allow the third chart to run with dummy data
    data = {
        'Road_Type': np.random.choice(['Single Carriageway', 'Dual Carriageway', 'Roundabout', 'Motorway', 'Slip Road'], size=500),
        'Road_condition': np.random.choice(['Dry', 'Wet / Damp', 'Snow', 'Frost / Ice', 'Flood'], size=500),
        'Accident_Severity': np.random.choice(['Slight', 'Serious', 'Fatal'], size=500)
    }
    df = pd.DataFrame(data)

# --- Streamlit Application ---
st.subheader("Objective : To show the count of accidents segmented by severity level for each weather condition. This is a key metric to identify disproportionately dangerous conditions (i.e., which weather conditions lead to the most severe outcomes).")
summary_text = "This section examines the influence of time and weather on accident occurrences. The Time of Day Analysis pinpoints the Afternoon as the peak period for accidents, which strongly suggests a correlation with high-volume traffic times, such as the daily commute. In contrast, the Weather of Day Analysis shows that the highest count of accidents happens during Clear weather—conditions seemingly ideal for riding. This implies that overconfidence or speed in good weather may be a primary cause of incidents. Furthermore, the stacked chart on the Relationship between Weather and Accident Severity indicates that the proportion of severe accidents is relatively stable across Clear, Rainy, and Foggy conditions, reinforcing the idea that rider behavior, rather than solely environmental impairment, drives the overall accident severity rate."
st.info(summary_text)

# --- 1. Road Type Analysis ---
st.header("1. Road Type Analysis")
# FIX APPLIED: Removed extra closing parenthesis
summary_text = "Accidents are fairly evenly distributed across the three road types: City Road, Highway, and Village Road. City Road has the highest count, but the differences between the three categories are not extreme. This suggests that accident risk is significant regardless of the type of road, necessitating safety measures across all environments."
st.info(summary_text)


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
# FIX APPLIED: Removed extra closing parenthesis
summary_text = "There are significantly more accidents on Dry road conditions than on Wet conditions. This suggests that while wet roads are inherently dangerous, the sheer volume of traffic and riding time on dry roads leads to a greater total number of accidents. Interventions should focus on safety during dry conditions, which account for the majority of incidents."
st.info(summary_text)

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

st.header("3. Relationship between Road Condition and Accident Severity")
# FIX APPLIED: Removed extra closing parenthesis
summary_text = "Accidents on Dry roads are much more frequent than on Wet roads.The proportion of Severe Accidents (pink/red color) is visually higher for Wet conditions compared to Dry conditions. This suggests that while more total accidents happen on dry roads, accidents on wet roads are more likely to result in a Severe outcome."
st.info(summary_text)


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
