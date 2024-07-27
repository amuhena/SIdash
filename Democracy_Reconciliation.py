import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import base64
from io import BytesIO
import folium
from streamlit_folium import folium_static
import plotly.io as pio
import simplekml
import base64

st.set_page_config(layout='wide')

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Custom CSS to display radio buttons horizontally
st.markdown(
    """
    <style>
    .stRadio > div {
        flex-direction: row;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">Democracy & Reconciliation in Sri Lanka</div>', unsafe_allow_html=True)

# Define your color themes
color_theme_1 = {
    'Democracy is preferable to any other form of government': '#993300',
    'In certain situations, a dictatorial government can be preferable to a democratic one': '#cc6600',
    'It doesn’t matter to me whether we have democratic or non-democratic government': '#ffbb33',
    'No opinion/ Don’t Know': '#ffd480',
    'Yes': '#1f77b4',
    'No': '#ff7f0e',
    'Don’t Know': '#7f7f7f',
    'Satisfied': '#993300',
    'Not Satisfied': '#cc6600',
    'Could not understand/ No Opinion': '#ffd480',
    'It is ok to decentralize certain powers but the powers of the central government should not be reduced': '#ffbb33',
    'Neither': '#cc6600',
    'Power needs to be devolved to the Provincial Councils while reducing the power of the central government.': '#993300',
    'In order to maintain every citizen\'s right to equality, no religion should be given the foremost place in the constitution.': '#ffbb33',
    'It is okay for the majority religion to be given the foremost place in the constitution.': '#993300'
}

color_theme_2 = {
    'Democracy is preferable to any other form of government': '#003366',
    'In certain situations, a dictatorial government can be preferable to a democratic one': '#336699',
    'It doesn’t matter to me whether we have democratic or non-democratic government': '#6699cc',
    'No opinion/ Don’t Know': '#99ccff',
    'Yes': '#ffcc00',
    'No': '#ff9900',
    'Don’t Know': '#ff6600',
    'Satisfied': '#003366',
    'Not Satisfied': '#336699',
    'Could not understand/ No Opinion': '#99ccff',
    'It is ok to decentralize certain powers but the powers of the central government should not be reduced': '#6699cc',
    'Neither': '#336699',
    'Power needs to be devolved to the Provincial Councils while reducing the power of the central government.': '#003366',
    'In order to maintain every citizen\'s right to equality, no religion should be given the foremost place in the constitution.': '#6699cc',
    'It is okay for the majority religion to be given the foremost place in the constitution.': '#003366'
}

# Define a function to get the selected color theme
def get_color_theme(theme):
    if theme == "Theme 1":
        return color_theme_1
    elif theme == "Theme 2":
        return color_theme_2

# Define your datasets for each question
survey_data = {
    'Support for Democracy': {
        'national': ['No opinion/ Don’t Know', 'It doesn’t matter to me whether we have democratic or non-democratic government', 'In certain situations, a dictatorial government can be preferable to a democratic one', 'Democracy is preferable to any other form of government'],
        'national_values': [4.2, 9.8, 9.4, 76.7],
        'ethnicity': ['Muslim', 'Malaiyaha Tamil', 'Tamil', 'Sinhala'],
        'ethnicity_values': [
            [6.0, 4.8, 11.6, 2.9],
            [4.8, 4.8, 7.1, 11.0],
            [11.9, 11.6, 8.9, 9.9],
            [84.5, 78.6, 72.3, 76.3]
        ],
        'sex': ['Female', 'Male'],
        'sex_values': [
            [5.6, 2.7],
            [8.4, 11.2],
            [8.6, 10.2],
            [77.4, 75.9]
        ],
        'age': ['Above 30 Yrs', '18 - 29 Yrs'],
        'age_values': [
            [4.1, 4.2],
            [10.8, 8.2],
            [8.6, 10.8],
            [76.5, 76.8]
        ],
    },
    'Progress on Reconciliation': {
        'national': ['Don’t Know', 'Not Satisfied', 'Satisfied'],
        'national_values': [6.1, 62.1, 31.8],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [6.0, 4.5, 7.1, 8.4],
            [62.9, 62.5, 64.3, 53.0],
            [31.1, 33.0, 28.6, 38.6]
        ],
        'sex': ['Female', 'Male'],
        'sex_values': [
            [7.3, 4.8],
            [62.0, 62.3],
            [30.7, 32.9]
        ],
        'age': ['Above 30 Yrs', '18 - 29 Yrs'],
        'age_values': [
            [7.1, 4.2],
            [61.8, 62.8],
            [31.1, 33.0]
        ],
    },
    'Power Devolution': {
        'national': ['Could not understand/ No Opinion', 'It is ok to decentralize certain powers but the powers of the central government should not be reduced', 'Neither', 'Power needs to be devolved to the Provincial Councils while reducing the power of the central government.'],
        'national_values': [12.6, 44.7, 7.0, 35.6],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [9.4, 24.8, 11.6, 28.6],
            [50.0, 15.0, 48.8, 32.1],
            [7.2, 7.1, 7.0, 4.8],
            [33.4, 53.1, 32.6, 34.5]
        ],
        'sex': ['Female', 'Male'],
        'sex_values': [
            [16.1, 9.1],
            [42.3, 37.2],
            [4.4, 9.8],
            [37.2, 43.9]
        ],
        'age': ['Above 30 Yrs', '18 - 29 Yrs'],
        'age_values': [
            [13.0, 12.1],
            [44.5, 45.0],
            [8.0, 5.3],
            [34.4, 37.6]
        ],
    },
    'Secular Constitution': {
        'national': ['Could not understand/ No opinion', 'In order to maintain every citizen\'s right to equality, no religion should be given the foremost place in the constitution.', 'Neither', 'It is okay for the majority religion to be given the foremost place in the constitution.'],
        'national_values': [4.4, 52.0, 1.4, 42.2],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [2.2, 15.0, 4.7, 9.5],
            [48.6, 58.4, 64.3, 70.2],
            [1.0, 1.8, 7.1, 2.4],
            [48.1, 24.8, 23.8, 17.9]
        ],
        'sex': ['Female', 'Male'],
        'sex_values': [
            [4.4, 4.6],
            [49.6, 54.2],
            [0.8, 2.1],
            [45.2, 39.0]
        ],
        'age': ['Above 30 Yrs', '18 - 29 Yrs'],
        'age_values': [
            [3.9, 5.0],
            [46.7, 61.2],
            [1.5, 1.3],
            [47.8, 32.5]
        ],
    }
}

# Define the dictionary for custom questions
custom_questions = {
    'Support for Democracy': "What is your opinion on the form of government that is preferable?",
    'Progress on Reconciliation': "How do you rate the progress on reconciliation in the country?",
    'Power Devolution': "What is your stance on the devolution of power?",
    'Secular Constitution': "What are your views on the secular nature of the constitution?"
}

# Create two columns for the selection sections
col1, col2 = st.columns([1, 1])

with col1:
    selected_heading = st.selectbox("Select Section", list(survey_data.keys()), key="main_heading_dropdown")

with col2:
    selected_graph = st.radio(
        "Filter", ["Ethnicity", "Sex", "Age"],
        key="right_radio"
    )

# Placeholder for chart title
chart_title_placeholder = st.empty()

# Create a placeholder for the content
content_placeholder = st.empty()

if 'selected_theme' not in st.session_state:
    st.session_state.selected_theme = "Theme 1"

if 'selected_info' not in st.session_state:
    st.session_state.selected_info = "Show Charts"

with st.sidebar:
    selected_theme = st.radio("Select Color Theme", ["Theme 1", "Theme 2"], index=0, key="theme_radio_sidebar")
    selected_info = st.radio("Select Information", ["Show Charts", "Show Introductory Text", "Show Methodology Text"], key="info_radio_sidebar")

    # Add buttons for "Full Report" and "Home"
    if st.button("Full Report"):
        st.experimental_set_query_params(page="CIDGI_detailSheet.py")
        st.experimental_rerun()
    if st.button("Home"):
        st.experimental_set_query_params(page="Home.py")
        st.experimental_rerun()
        
    st.markdown("[View full report as PDF](https://www.cpalanka.org/topline-report-democracy-reconciliation-in-sri-lanka/)")

# Ensure selected_theme and selected_info are updated in session state
st.session_state.selected_theme = selected_theme
st.session_state.selected_info = selected_info

# Function to get the color theme
color_mapping = get_color_theme(st.session_state.selected_theme)

# Define a function to create horizontal bar charts
def create_horizontal_bar_chart(labels, values, title):
    bar_fig = go.Figure()

    bar_fig.add_trace(go.Bar(
        y=labels, x=values,
        marker_color=[color_mapping.get(label, '#000000') for label in labels],  # Handle missing colors gracefully
        text=[f"{v}%" for v in values], textposition='outside',  # Position text outside the bars and add percentage
        orientation='h'  # Horizontal orientation
    ))

    bar_fig.update_layout(
        title=dict(text=title, x=0.5),  # Center the title
        xaxis=dict(title='Percentage', color='black'),
        yaxis=dict(title='Category', color='black'),
        font=dict(color='black'),  # Set text color to black
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=-0.5,
            xanchor='center',
            x=0.5
        ),
        margin=dict(l=40, r=40, t=80, b=120),  # Adjust margins to make space for annotations
        height=450,  # Adjust the height of the chart
        width=500  # Adjust the width of the chart
    )
    return bar_fig

# Define a function to create horizontal clustered bar charts
def create_horizontal_clustered_bar_chart(labels, values, title):
    bar_fig = go.Figure()

    for idx, val in enumerate(values):
        bar_fig.add_trace(go.Bar(
            y=labels, x=val,
            name=survey_data[selected_heading]['national'][idx],
            marker_color=color_mapping.get(survey_data[selected_heading]['national'][idx], '#000000'),  # Handle missing colors gracefully
            text=[f"{v}%" for v in val], textposition='outside',  # Position text outside the bars and add percentage
            orientation='h'  # Horizontal orientation
        ))

    bar_fig.update_layout(
        barmode='group',
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=18)),
        xaxis=dict(color='black'),
        yaxis=dict(color='black'),
        font=dict(color='black'),  # Set text color to black
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=-0.5,
            xanchor='center',
            x=0.5
        ),
        margin=dict(l=40, r=40, t=80, b=120),  # Adjust margins to make space for annotations
        height=450,  # Adjust the height of the chart
        width=500 # Adjust the width of the chart
    )
    return bar_fig

# Define a function to create pie charts
def create_pie_chart(labels, values, title):
    pie_fig = go.Figure()

    pie_fig.add_trace(go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=[color_mapping.get(label, '#000000') for label in labels]),  # Handle missing colors gracefully
        textinfo='percent',  # Show only percentages
        hoverinfo='label+percent',  # Show labels and percentages on hover
        sort=False  # Maintain the order of the data
    ))

    pie_fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=18)),
        font=dict(color='#993300'),  # Set text color to black
        legend=dict(
            orientation='h',
            yanchor='top',
            y=-0.2,
            xanchor='center',
            x=0.5
        ),
        margin=dict(l=40, r=40, t=80, b=160),  # Adjust margins to make space for annotations
        height=450,  # Adjust the height of the chart
        width=500  # Adjust the width of the chart
    )
    return pie_fig

# Text section above the chart section that changes based on the dropdown selection
question_text = custom_questions.get(selected_heading, f"Question: {selected_heading}")
st.markdown(f"<h4 style='text-align: center; color: #8C3703;'>{question_text}</h4>", unsafe_allow_html=True)

if st.session_state.selected_info == "Show Charts":
    # Create two columns for the charts
    chart_col1, chart_col2 = st.columns([1, 1])

    with chart_col1:
        data = survey_data[selected_heading]
        pie_chart = create_pie_chart(data['national'], data['national_values'], f"{selected_heading} - National Level")
        st.plotly_chart(pie_chart)

    with chart_col2:
        if selected_graph == "Ethnicity":
            bar_chart = create_horizontal_clustered_bar_chart(data['ethnicity'], data['ethnicity_values'], f"{selected_heading} by Ethnicity")
        elif selected_graph == "Sex":
            bar_chart = create_horizontal_clustered_bar_chart(data['sex'], data['sex_values'], f"{selected_heading} by Sex")
        elif selected_graph == "Age":
            bar_chart = create_horizontal_clustered_bar_chart(data['age'], data['age_values'], f"{selected_heading} by Age")
        else:
            bar_chart = None
        if bar_chart:
            st.plotly_chart(bar_chart)

elif st.session_state.selected_info == "Show Introductory Text":
    with content_placeholder.container():
        st.markdown("<h2 style='text-align: center; color: #8C3703;'>Introduction</h2>", unsafe_allow_html=True)
        intro_text = """
        This brief report aims to share some of the selected key findings of the latest survey on democracy and reconciliation conducted by Social Indicator, the survey arm of the Centre for Policy Alternatives. The poll was designed to capture the current public opinion on matters related to themes of democracy and reconciliation in Sri Lanka. The survey findings on support for democracy, trust in democratic institutions, public assessment of the progress of reconciliation, and attitude toward constitutional reforms are discussed in this brief report.
        
        A total of 1350 individuals belonging to the four main ethnic communities - Sinhala, Tamil, Malaiyaha Tamil, and Muslim - across 25 districts participated in this survey. A semi-structured questionnaire was administered amongst the respondents who were chosen using a multi-stage stratified random sampling technique. The fieldwork was conducted between 4th and 22nd of January 2024 employing 73 field enumerators (male and female) who belong to the four main ethnic communities. Upon completion of the data collection process, the data set was weighted to reflect the actual district and ethnic proportion of the population. The data set was analysed using the Statistical Package for Social Sciences (SPSS).
        """
        st.markdown(intro_text)

elif st.session_state.selected_info == "Show Methodology Text":
    with content_placeholder.container():
        st.markdown("<h2 style='text-align: center; color: #8C3703;'>Methodology</h2>", unsafe_allow_html=True)
        methodology_text = """
        The survey was carried out through face-to-face interviews utilizing a semi-structured questionnaire amongst a sample of 1350 individuals selected from the four main ethnic communities - Sinhala, Tamil, Malaiyaha Tamil, and Muslim - across 25 districts. The sample locations are selected using a multi-stage stratified random sampling technique to ensure fair representation of men and women residing in both rural and urban localities. The fieldwork was conducted between the 4th and 22nd of January 2024 employing 73 field enumerators (male and female) who belong to the four main ethnic communities. The final data set was weighted to reflect the actual district and ethnic proportion of the population and was analysed using the Statistical Package for Social Sciences (SPSS).
        """
        st.markdown(methodology_text)
