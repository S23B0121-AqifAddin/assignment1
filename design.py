import streamlit as st
import pandas as pd
import plotly.express as px


# --- Corrected Imports ---
import plotly.graph_objects as go # Keep this if you need go, though px handles everything here

# Set Streamlit page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Tutorial Scientific Visualization",
    layout="wide" # Set layout here for consistency
)

# Page header
st.header("Tutorial Scientific Visualization", divider="grey")

col1, col2, col3, col4 = st.columns(4)
    
col1.metric(label="PLO 2", value=f"3.3", help="PLO 2: Cognitive Skill", border=True)
col2.metric(label="PLO 3", value=f"3.5", help="PLO 3: Digital Skill", border=True)
col3.metric(label="PLO 4", value=f"4.0", help="PLO 4: Interpersonal Skill", border=True)
col4.metric(label="PLO 5", value=f"4.3", help="PLO 5: Communication Skill", border=True)

# Load your data
try:
    df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='utf-8')
except UnicodeDecodeError:
    df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='latin-1')

st.dataframe(df2.head()) # Use st.dataframe instead of just df2 to display the data

# Filter Arts faculty if 'Faculty' column exists
arts_df = df2[df2['Faculty'] == 'Arts'] if 'Faculty' in df2.columns else df2

# Gender distribution chart (This part is correctly placed outside run_app but will execute)
if 'Gender' in arts_df.columns:
    st.subheader("Distribution of Gender in Arts Faculty (Plotly)")

    gender_counts = arts_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']

    # Create a Plotly Pie Chart
    fig = px.pie(
        gender_counts,
        values='Count',
        names='Gender',
        title='Distribution of Gender in Arts Faculty',
        hole=0.3, 
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("The dataset does not contain a 'Gender' column.")

st.markdown("---")
st.title("🎓 Arts Faculty Survey Dashboard (Plotly Interactive)")
st.markdown("---")

# --- Function Definition and Body with Correct Indentation ---
def run_app():
    # 1. Distribution of Academic Year (Bar Chart)
    st.header("1. Distribution of Academic Year in Arts Faculty")
    academic_year_counts = arts_df['Masters Academic Year in EU'].value_counts().reset_index()
    academic_year_counts.columns = ['Masters Academic Year in EU', 'Count']

    fig1 = px.bar(
        academic_year_counts, 
        x='Masters Academic Year in EU', 
        y='Count',
        title='Distribution of Academic Year in Arts Faculty',
        color='Masters Academic Year in EU',
        labels={'Masters Academic Year in EU': 'Academic Year', 'Count': 'Number of Students'}
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("---")


    # 2. Expectation vs. Met Expectation for Quality of Resources (Scatter Plot)
    st.header("2. Expectation vs. Met Expectation for Quality of Resources")
    
    fig2 = px.scatter(
        arts_df,
        x='Q3 [What was your expectation about the University as related to quality of resources?]',
        y='Q5 [To what extent your expectation was met?]',
        title='Expectation vs. Met Expectation for Quality of Resources (Arts Faculty)',
        labels={
            'Q3 [What was your expectation about the University as related to quality of resources?]': 'Expectation about Quality of Resources (Scale)',
            'Q5 [To what extent your expectation was met?]': 'Extent Expectation Met (Scale)'
        },
        trendline="ols",
        hover_data=[arts_df.index]
    )
    fig2.update_layout(xaxis_showgrid=True, yaxis_showgrid=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("---")


    # 3. Distribution of Best Aspects of the Program (Horizontal Bar/Count Plot)
    # NOTE: The explicit column renaming for robustness is included here.
    st.header("3. Distribution of Best Aspects of the Program")

    best_aspects_df = arts_df['Q7. In your opinion,the best aspect of the program is'].value_counts().reset_index()
    best_aspects_df.columns = ['Aspect', 'Count'] 

    fig3 = px.bar(
        best_aspects_df,
        y='Aspect', 
        x='Count', 
        orientation='h',
        title='Distribution of Best Aspects of the Program (Arts Faculty)',
        labels={'Aspect': 'Best Aspect of the Program', 'Count': 'Count'},
        color='Aspect'
    )
    fig3.update_yaxes(autorange="reversed") 
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("---")


    # 4. Aspects of the Program that Could be Improved (Horizontal Bar/Count Plot)
    st.header("4. Aspects of the Program that Could be Improved")

    improvement_aspects_df = arts_df['What aspects of the program could be improved?'].value_counts().reset_index()
    improvement_aspects_df.columns = ['Aspect', 'Count'] 

    fig4 = px.bar(
        improvement_aspects_df,
        y='Aspect',
        x='Count',
        orientation='h',
        title='Aspects of the Program that Could be Improved (Arts Faculty)',
        labels={'Aspect': 'Aspects for Improvement', 'Count': 'Count'},
        color='Aspect'
    )
    fig4.update_yaxes(autorange="reversed")
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown("---")


    # 5. Perceived Improvement in Education Quality (Count Plot)
    st.header("5. Perceived Improvement in Education Quality")
    
    fig5 = px.histogram(
        arts_df,
        x='Do you feel that the quality of education improved at EU over the last year?',
        title='Perceived Improvement in Education Quality (Arts Faculty)',
        labels={'x': 'Response', 'count': 'Count'},
        color='Do you feel that the quality of education improved at EU over the last year?'
    )
    st.plotly_chart(fig5, use_container_width=True)
    st.markdown("---")


    # 6. Perceived Improvement in University Image (Count Plot)
    st.header("6. Perceived Improvement in University Image")
    
    fig6 = px.histogram(
        arts_df,
        x='Do you feel that the image of the University improved over the last year?',
        title='Perceived Improvement in University Image (Arts Faculty)',
        labels={'x': 'Response', 'count': 'Count'},
        color='Do you feel that the image of the University improved over the last year?'
    )
    st.plotly_chart(fig6, use_container_width=True)
    
# Run the application
if __name__ == '__main__':
    run_app()
