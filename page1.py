import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example: load your dataset (replace with your actual df)
# df = pd.read_csv("motorbike_accident_severity.csv")

st.subheader("Distribution of Biker Occupation")

# Create the Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(
    data=df,
    x='Biker_Occupation',
    order=df['Biker_Occupation'].value_counts().index,
    palette='magma',
    ax=ax
)

ax.set_title('Distribution of Biker Occupation')
ax.set_xlabel('Biker Occupation')
ax.set_ylabel('Count')
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
plt.tight_layout()

# Display the chart in Streamlit
st.pyplot(fig)
