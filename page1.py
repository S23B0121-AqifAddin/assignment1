import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np # Added for creating dummy data if the file isn't available

# --- Streamlit Application ---

# 1. Load the dataset
# IMPORTANT: Replace "motorbike_accident_severity.csv" with the correct path 
# to your file, or use the dummy data below if you don't have a file.

try:
    # Attempt to load the real data
    df = pd.read_csv("motorbike_accident_severity.csv")
except FileNotFoundError:
    # If the file is not found, create a dummy DataFrame for demonstration
    st.warning("Data file 'motorbike_accident_severity.csv' not found. Using dummy data for demonstration.")
    data = {
        'Biker_Occupation': np.random.choice(['Student', 'Employee', 'Self-Employed', 'Retiree', 'Unemployed'], size=100),
    }
    df = pd.DataFrame(data)

st.title("Motorbike Accident Analysis")
st.subheader("Distribution of Biker Occupation")

# 2. Create the Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the count distribution using seaborn
sns.countplot(
    data=df,
    x='Biker_Occupation',
    # Order the bars by count (most frequent first)
    order=df['Biker_Occupation'].value_counts().index,
    palette='magma',
    ax=ax
)

# 3. Customize the plot
ax.set_title('Distribution of Biker Occupation')
ax.set_xlabel('Biker Occupation')
ax.set_ylabel('Count')

# Rotate x-axis labels for better readability
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# 4. Display the chart in Streamlit
st.pyplot(fig)
