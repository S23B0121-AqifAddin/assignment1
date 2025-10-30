import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # Import Plotly Express
import matplotlib.pyplot as plt # Needed for st.pyplot()
import seaborn as sns # Needed for sns.countplot()

# --- Streamlit Application ---

st.set_page_config(
    page_title="Motorbike Accident Analysis",
    layout="wide" # Use wide layout for better visualization
)

st.title("Motorbike Accident Analysis")
st.subheader("The primary objective of this visualization is to compare and quantify the representation of different occupations within the biker population to identify which occupation categories are the most and least common.")

# --- UPDATED: Summary Box using st.info ---
summary_text = "The above chart shows the distribution of biker occupations in the dataset. We can observe that 'Students' are often a frequent occupation among bikers in this dataset, followed by other categories like 'Government Employee', 'Self Employed', and 'Private Employee'. 'Others' and 'Unemployed' are typically less represented."
st.info(summary_text)

# --- End of Summary Box --

# 1. Load the dataset
try:
    # Attempt to load the real data
    # IMPORTANT: Update this path if your CSV is in a different location
    df = pd.read_csv("motorbike_accident_severity.csv")
except FileNotFoundError:
    # If the file is not found, create a dummy DataFrame for demonstration
    st.warning("Data file 'motorbike_accident_severity.csv' not found. Using comprehensive dummy data for demonstration.")
    
    # Dummy data structure must include all columns used later in the script
    data = {
        'Biker_Occupation': np.random.choice(['Student', 'Govt Employee', 'Self Employed', 'Private Employee', 'Others', 'Unemployed'], size=200),
        'Accident_Severity': np.random.choice(['Minor', 'Moderate', 'Major'], size=200),
        'Age_Band': np.random.choice(['<25', '25-45', '46-65', '>65'], size=200),
        'Biker_Education_Level': np.random.choice(['High School', 'Diploma', 'Bachelor\'s', 'Master\'s', 'PhD', 'None'], size=200) # Added missing column
    }
    df = pd.DataFrame(data)

# --- FIRST CHART: Biker Occupation Distribution (Plotly) ---
if 'Biker_Occupation' in df.columns:
    st.header('Biker Occupation Distribution (Plotly)')

    # 2. Create the Plotly figure using Plotly Express
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

# --- SECOND CHART: Biker Education Level Distribution (Matplotlib/Seaborn) ---
if 'Biker_Education_Level' in df.columns:
    st.header('Biker Education Level Distribution (Seaborn)')

    # Create the figure object as required by st.pyplot()
    fig, ax = plt.subplots(figsize=(10, 6))

    # Recreate the seaborn countplot logic on the axes object
    sns.countplot(
        data=df,
        x='Biker_Education_Level',
        order=df['Biker_Education_Level'].value_counts().index,
        palette='magma',
        ax=ax # Pass the axes object to seaborn
    )

    # Set the title and labels using the axes object
    ax.set_title('Distribution of Biker Education Level')
    ax.set_xlabel('Biker Education Level')
    ax.set_ylabel('Count')

    # Rotate x-tick labels and adjust layout
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)
else:
    st.error("The DataFrame does not contain a 'Biker_Education_Level' column for analysis.")
