import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Data Loading (Crucial for the app to run) ---
# Use st.cache_data for efficiency if the dataframe is large
@st.cache_data
def load_data():
    try:
        # Attempt to load the real data
        # NOTE: Update 'your_data.csv' to the actual filename if needed
        df = pd.read_csv("motorbike_accident_severity.csv")
        return df
    except FileNotFoundError:
        # Create a dummy DataFrame if the file isn't found
        st.warning("Data file not found. Using dummy data for demonstration.")
        size = 200
        data = {
            'Weather': np.random.choice(['Clear', 'Raining', 'Fog', 'Snowing', 'Windy', 'Overcast'], size=size),
            'Accident_Severity': np.random.choice(['Slight', 'Serious', 'Fatal'], size=size),
            'Time_of_Day': np.random.choice(['Morning (6-12)', 'Afternoon (12-18)', 'Evening (18-24)', 'Night (0-6)'], size=size),
        }
        return pd.DataFrame(data)

df = load_data()

# --- Streamlit Application ---

st.subheader("Objective : To quantify the influence of road conditions and road type on both accident frequency and the resulting severity, identifying key road-related hazards.")
summary_text = "These charts analyze how road characteristics influence accident frequency and severity. The Distribution of Accidents by Road Type shows a relatively even spread across City Roads, Highways, and Village Roads, suggesting accident risk is pervasive regardless of the road environment. However, the Road Condition Analysis reveals that Dry conditions account for the largest total number of accidents, a finding that suggests high traffic volume and driver behavior are major contributors. Crucially, the Relationship between Road Condition and Accident Severity demonstrates that although dry roads have more total incidents, accidents occurring on Wet road surfaces are significantly more likely to be classified as Severe. This indicates that reduced traction on wet roads elevates the danger level of any incident."
st.info(summary_text)
# --- 1. Weather of Day Analysis (Plotly) ---
st.header("1. Weather of Day Analysis")
summary_text = "Accidents peak significantly during the Afternoon time segment. Night has the second-highest count, while Morning, Noon, and Evening have lower, but roughly equal, frequencies. This clearly identifies the Afternoon as the most dangerous period for bikers, likely correlating with high traffic volume (e.g., afternoon commute)"
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
st.subheader("")

summary_text_time = "The highest total number of accidents occur during Clear weather, with Rainy and Foggy conditions having a slightly lower but comparable count. Similar to the road condition analysis, this indicates that the majority of accidents happen under seemingly ideal (clear) conditions, which may be due to higher traffic, speeding, or overconfidence, rather than weather-related impairment."
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
st.header("3. Relationship between Weather and Accident Severity")
st.subheader("Severity of Accidents by Weather Condition")
summary_text_severity = "The proportion of the most severe accidents ('No Accident' and 'Severe Accident' seem to be the severe categories based on the legend colors: Yellow and Green, or perhaps Severe Accident and Moderate Accident are the non-minor categories). Assuming the top two colors are the most severe: The proportions of severe accidents appear relatively consistent across Clear, Rainy, and Foggy weather. This suggests that while Rainy and Foggy weather are hazardous, the severity of an accident, once it occurs, is not drastically different compared to Clear conditions."
st.info(summary_text_severity)

if 'Weather' in df.columns and 'Accident_Severity' in df.columns:

    # Use Plotly Express's histogram function to automatically count and stack the data
    fig_severity = px.histogram(
        df,
        x='Weather',
        color='Accident_Severity',
        barmode='stack', # Key setting for a stacked bar chart
        title='Accident Severity by Weather Condition (Stacked)',
        labels={'Weather': 'Weather Condition', 'count': 'Number of Accidents'},
        # Order the severity levels logically for the legend
        category_orders={"Accident_Severity": ['Slight', 'Serious', 'Fatal']},
        color_discrete_sequence=px.colors.qualitative.T10 # Using a standard Plotly palette
    )

    # Customize layout and axis labels
    fig_severity.update_layout(
        xaxis_title='Weather Condition',
        yaxis_title='Number of Accidents (Count)',
        xaxis_tickangle=-45,
        legend_title="Severity"
    )
    
    # Ensure all bars are clearly visible (e.g., sort by total count descending)
    fig_severity.update_xaxes(categoryorder='total descending')

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_severity, use_container_width=True)
    
else:
    st.error("DataFrame must contain 'Weather' and 'Accident_Severity' columns.")
