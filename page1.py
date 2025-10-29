import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # Import Plotly Express

# --- Streamlit Application ---

st.set_page_config(
    page_title="Motorbike Accident Analysis",
    layout="wide" # Use wide layout for better visualization
)

st.title("Motorbike Accident Analysis")
st.subheader("Distribution of Biker Occupation")

# 1. Load the dataset
try:
    # Attempt to load the real data
    # IMPORTANT: Update this path if your CSV is in a different location
    df = pd.read_csv("motorbike_accident_severity.csv") 
except FileNotFoundError:
    # If the file is not found, create a dummy DataFrame for demonstration
    st.warning("Data file 'motorbike_accident_severity.csv' not found. Using dummy data for demonstration.")
    data = {
        'Biker_Occupation': np.random.choice(['Student', 'Employee', 'Self-Employed', 'Retiree', 'Unemployed'], size=200),
        'Accident_Severity': np.random.choice(['Minor', 'Moderate', 'Major'], size=200),
        'Age_Band': np.random.choice(['<25', '25-45', '46-65', '>65'], size=200)
    }
    df = pd.DataFrame(data)

# Ensure 'Biker_Occupation' column exists before plotting
if 'Biker_Occupation' in df.columns:
    # 2. Create the Plotly figure using Plotly Express
    # Plotly Express automatically handles value counts for bar charts when you pass the column
    # To order by count, we first get the value counts and then create the bar chart from that.
    occupation_counts = df['Biker_Occupation'].value_counts().reset_index()
    occupation_counts.columns = ['Biker_Occupation', 'Count'] # Rename columns for clarity

    fig = px.bar(
        occupation_counts,
        x='Biker_Occupation',
        y='Count',
        title='Distribution of Biker Occupation',
        labels={'Biker_Occupation': 'Biker Occupation', 'Count': 'Number of Bikers'},
        color='Biker_Occupation', # Color bars by occupation category
        color_discrete_sequence=px.colors.qualitative.D3 # A different color palette
    )

    # 3. Customize the plot (Plotly customizations)
    fig.update_layout(
        xaxis_title_text='Biker Occupation', # X-axis title
        yaxis_title_text='Count',            # Y-axis title
        xaxis_tickangle=-45,                 # Rotate x-axis labels
        hovermode="x unified"                # Improve hover behavior
    )

    # 4. Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("The DataFrame does not contain a 'Biker_Occupation' column for analysis.")

# You can add more analysis here if needed
st.markdown("---")
st.write("The above chart shows the distribution of biker occupations in the dataset. We can observe that 'Students' are the most frequent occupation among bikers in this dataset, followed by 'Government Employee', 'Self Employed', and 'Private Employee'. 'Others' and 'Unemployed' are less represented.")
