import streamlit as st
import plotly.graph_objects as go

# Function to get the color theme
def get_color_theme(theme):
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
    if theme == "Theme 1":
        return color_theme_1
    elif theme == "Theme 2":
        return color_theme_2

# Define survey data
survey_data = {
    'Which of the following statements, do you agree with the most?': {
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
    'How satisfied are you with the current government’s progress on addressing reconciliation, in post-war Sri Lanka?': {
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
    'Power Devolution - Please select the statement, that best describes your ideas.': {
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
    'Secular Constitution - - Please select the statement, that best describes your ideas.': {
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

st.set_page_config(layout='wide')
st.title("Detailed Dashboard")

# Get the selected color theme
if 'selected_theme' not in st.session_state:
    st.session_state.selected_theme = "Theme 1"

with st.sidebar:
    selected_theme = st.radio("Select Color Theme", ["Theme 1", "Theme 2"], index=0, key="theme_radio_sidebar")
    st.session_state.selected_theme = selected_theme

    if st.button("Go to Dashboard"):
        st.experimental_set_query_params(page="Democracy_Reconciliation.py")
        st.experimental_rerun()
    if st.button("Home"):
        st.experimental_set_query_params(page="Home.py")
        st.experimental_rerun()

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
        margin=dict(l=40, r=40, t=80, b=160),  # Adjust margins to make space for annotations
        height=600,  # Adjust the height of the chart
        width=800  # Adjust the width of the chart
    )
    return bar_fig

# Define a function to create horizontal clustered bar charts
def create_horizontal_clustered_bar_chart(labels, values, title, section):
    bar_fig = go.Figure()

    for idx, val in enumerate(values):
        bar_fig.add_trace(go.Bar(
            y=labels, x=val,
            name=survey_data[section]['national'][idx],
            marker_color=color_mapping.get(survey_data[section]['national'][idx], '#000000'),  # Handle missing colors gracefully
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
        margin=dict(l=40, r=40, t=80, b=160),  # Adjust margins to make space for annotations
        height=600,  # Adjust the height of the chart
        width=800  # Adjust the width of the chart
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
        height=600,  # Adjust the height of the chart
        width=800  # Adjust the width of the chart
    )
    return pie_fig

for section in survey_data.keys():
    st.header(section)
    
    data = survey_data[section]
    st.plotly_chart(create_pie_chart(data['national'], data['national_values'], f"{section} - National Level"))
    
    filter_option = st.radio("Filter by", ["Ethnicity", "Sex", "Age"], key=f"{section}_filter_radio")
    
    if filter_option == "Ethnicity":
        bar_chart = create_horizontal_clustered_bar_chart(data['ethnicity'], data['ethnicity_values'], f"{section} by Ethnicity", section)
    elif filter_option == "Sex":
        bar_chart = create_horizontal_clustered_bar_chart(data['sex'], data['sex_values'], f"{section} by Sex", section)
    elif filter_option == "Age":
        bar_chart = create_horizontal_clustered_bar_chart(data['age'], data['age_values'], f"{section} by Age", section)
    else:
        bar_chart = None

    if bar_chart:
        st.plotly_chart(bar_chart)
