import streamlit as st
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(layout='wide')

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function to get the color theme
def get_color_theme(theme):
    color_theme_1 = {
        'NPP- Anura Kumara Dissanayake': '#992600',
        'SJB- Sajith Premadasa': '#e6b800',
        'UNP- Ranil Wickremesinghe': '#006600',
        'No one': '#595959',
        'Do not know': '#a6a6a6'
    }
    color_theme_2 = {
        'NPP- Anura Kumara Dissanayake': '#1f77b4',
        'SJB- Sajith Premadasa': '#e6b800',
        'UNP- Ranil Wickremesinghe': '#006600',
        'No one': '#d62728',
        'Do not know': '#7f7f7f'
    }
    if theme == "Theme 1":
        return color_theme_1
    elif theme == "Theme 2":
        return color_theme_2

# Define survey data (including the new data with Locality)
survey_data = {
    'Ensure anti-corruption measures': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [25.8, 14.4, 22.2, 19.7, 17.8],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [29.7, 9.2, 10.7, 20.2],
            [11.5, 24.3, 25.0, 21.0],
            [20.0, 17.1, 17.9, 21.8],
            [24.2, 15.8, 26.8, 12.9],
            [14.6, 33.6, 19.6, 24.2]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [33.1, 18.5],
            [12.5, 16.3],
            [17.9, 21.5],
            [20.1, 24.3],
            [16.3, 19.4]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [26.7, 25.4],
            [15.1, 13.9],
            [17.9, 20.7],
            [25.2, 20.6],
            [15.1, 19.4]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [21.9, 26.7],
            [17.9, 13.6],
            [18.7, 19.9],
            [25.1, 21.6],
            [16.3, 18.1]
        ]
    },
    'Ensure post-war reconciliation and transitional justice': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [29.0, 13.3, 20.3, 23.1, 14.4],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [16.6, 7.2, 5.4, 9.6],
            [10.4, 22.4, 28.6, 20.0],
            [20.6, 14.5, 21.4, 24.0],
            [25.2, 20.4, 17.9, 11.2],
            [27.3, 35.5, 26.8, 35.2]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [20.6, 8.1],
            [11.6, 15.1],
            [19.2, 21.3],
            [22.0, 24.1],
            [26.6, 31.4]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [16.2, 13.4],
            [14.1, 13.0],
            [14.5, 23.3],
            [27.3, 20.7],
            [27.9, 29.6]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [11.5, 15.0],
            [16.3, 12.7],
            [15.9, 21.2],
            [15.1, 24.8],
            [41.3, 26.2]
        ]
    },
    'Uphold the democratic rights of the people': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [19.0, 19.9, 20.3, 21.5, 19.4],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [23.1, 8.6, 8.9, 12.0],
            [17.5, 27.6, 30.4, 30.4],
            [20.9, 19.1, 28.6, 25.6],
            [21.1, 16.4, 17.9, 8.8],
            [17.3, 28.3, 14.3, 23.2]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [25.0, 14.6],
            [17.5, 23.1],
            [21.8, 21.2],
            [18.9, 20.0],
            [16.8, 21.2]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [23.5, 17.9],
            [19.1, 20.9],
            [19.7, 22.4],
            [20.2, 19.0],
            [17.4, 19.8]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [11.1, 21.9],
            [28.6, 18.4],
            [19.4, 22.0],
            [15.5, 20.2],
            [25.4, 17.5]
        ]
    },
    'Addressing Unemployment': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [16.6, 20.3, 20.8, 24.6, 18.0],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [18.8, 7.9, 8.9, 12.1],
            [18.0, 27.6, 32.1, 25.8],
            [24.6, 23.0, 26.8, 26.6],
            [22.5, 12.5, 19.6, 12.9],
            [16.1, 28.9, 12.5, 22.6]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [23.5, 9.6],
            [16.3, 24.4],
            [23.1, 26.1],
            [20.9, 20.0],
            [16.2, 19.9]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [21.4, 13.9],
            [19.5, 20.8],
            [25.4, 24.1],
            [19.7, 20.8],
            [13.9, 20.3]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [12.7, 17.5],
            [28.2, 18.6],
            [23.4, 24.9],
            [18.7, 20.8],
            [17.1, 18.2]
        ]
    },
    'Preserving law and order in the country': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [19.7, 15.1, 22.9, 27.0, 15.4],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [22.3, 8.6, 8.9, 16.8],
            [11.8, 25.2, 26.8, 23.2],
            [28.1, 21.9, 25.0, 24.8],
            [25.6, 13.9, 21.4, 12.8],
            [12.1, 30.5, 17.9, 22.4]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [27.0, 12.4],
            [12.5, 17.5],
            [26.1, 28.0],
            [22.5, 23.4],
            [11.9, 18.8]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [22.2, 18.3],
            [15.5, 14.8],
            [25.8, 27.6],
            [23.7, 22.4],
            [12.8, 16.8]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [12.7, 21.2],
            [24.7, 12.9],
            [22.3, 28.1],
            [24.7, 22.5],
            [15.5, 15.3]
        ]
    },
    'Hold those who are responsible for economic crisis accountable': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [24.0, 14.0, 26.0, 18.0, 18.0],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [27.9, 7.2, 10.7, 19.0],
            [11.1, 25.0, 25.0, 23.0],
            [17.4, 16.4, 19.6, 21.4],
            [28.7, 19.7, 26.8, 14.3],
            [15.0, 31.6, 17.9, 22.2]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [30.3, 17.8],
            [12.2, 16.5],
            [15.7, 19.9],
            [25.7, 26.7],
            [16.0, 19.1]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [25.2, 23.5],
            [13.7, 14.7],
            [16.4, 18.6],
            [28.8, 24.9],
            [16.0, 18.4]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [19.4, 25.2],
            [17.5, 13.5],
            [17.9, 17.8],
            [27.4, 26.0],
            [17.9, 17.4]
        ]
    },
    'Bring justice to the victims of the Easter Attack': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [20.8, 16.0, 12.3, 32.0, 18.9],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [24.1, 7.8, 8.8, 15.2],
            [14.2, 24.2, 24.6, 18.4],
            [11.5, 11.1, 15.8, 17.6],
            [34.8, 26.1, 28.1, 18.4],
            [15.4, 30.7, 22.8, 30.4]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [27.6, 13.9],
            [13.5, 18.6],
            [12.9, 11.5],
            [30.0, 34.0],
            [15.9, 21.9]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [22.5, 19.9],
            [17.0, 15.5],
            [9.5, 13.8],
            [34.0, 31.0],
            [17.0, 19.8]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [15.5, 22.0],
            [19.8, 15.1],
            [14.7, 11.7],
            [33.7, 31.6],
            [16.3, 19.5]
        ]
    },
    'Address the problems of minority communities': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [17.1, 25.0, 24.1, 17.4, 16.3],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [19.9, 4.6, 5.2, 14.3],
            [22.3, 31.6, 44.8, 30.2],
            [25.5, 18.4, 20.7, 21.4],
            [17.6, 21.7, 15.5, 11.9],
            [14.7, 23.7, 13.8, 22.2]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [12.6, 5.3],
            [10.7, 12.5],
            [53.4, 51.2],
            [10.7, 10.1],
            [12.5, 20.9]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [9.2, 8.9],
            [10.3, 12.3],
            [57.8, 49.3],
            [9.7, 10.8],
            [13.0, 18.8]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [6.7, 9.6],
            [14.3, 11.0],
            [42.9, 54.4],
            [15.1, 9.2],
            [21.0, 15.8]
        ]
    },
    'Will negotiate with the IMF for a better deal to resolve the economic crisis': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [16.7, 11.6, 10.4, 9.1, 52.3],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [10.0, 4.6, 5.4, 8.8],
            [9.1, 22.4, 19.6, 14.4],
            [55.7, 39.5, 50.0, 40.8],
            [10.7, 10.5, 10.7, 8.0],
            [14.6, 23.0, 14.3, 28.0]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [12.6, 5.3],
            [10.7, 12.5],
            [53.4, 51.2],
            [10.7, 10.1],
            [12.5, 20.9]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [9.2, 8.9],
            [10.3, 12.3],
            [57.8, 49.3],
            [9.7, 10.8],
            [13.0, 18.8]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [6.7, 9.6],
            [14.3, 11.0],
            [42.9, 54.4],
            [15.1, 9.2],
            [21.0, 15.8]
        ]
    },
    'Resolve the country’s Economic crisis': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [15.4, 19.9, 18.3, 12.4, 33.9],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [18.1, 5.3, 10.5, 8.1],
            [10.4, 22.5, 31.6, 25.0],
            [39.4, 39.1, 38.6, 39.5],
            [21.7, 9.9, 12.3, 10.5],
            [10.4, 23.2, 7.0, 16.9]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [20.9, 9.8],
            [10.7, 17.1],
            [39.7, 39.2],
            [20.6, 17.5],
            [8.1, 16.5]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [18.7, 13.6],
            [12.4, 14.7],
            [41.2, 38.5],
            [19.3, 18.9],
            [8.4, 14.4]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [14.3, 15.7],
            [21.8, 12.1],
            [35.3, 40.3],
            [18.3, 19.2],
            [10.3, 12.7]
        ]
    },
    'Finding alternative approaches to economic recovery': {
        'national': ['NPP- Anura Kumara Dissanayake', 'SJB- Sajith Premadasa', 'UNP- Ranil Wickremesinghe', 'No one', 'Do not know'],
        'national_values': [15.8, 17.8, 16.3, 17.0, 33.1],
        'ethnicity': ['Sinhala', 'Tamil', 'Malaiyaha Tamil', 'Muslim'],
        'ethnicity_values': [
            [21.0, 6.6, 7.0, 9.7],
            [14.7, 25.2, 26.3, 21.8],
            [34.2, 25.2, 36.8, 32.3],
            [17.8, 9.9, 15.8, 12.1],
            [12.3, 33.1, 14.0, 24.2]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [25.1, 10.4],
            [14.0, 20.1],
            [32.4, 33.9],
            [14.9, 17.6],
            [13.7, 17.9]
        ],
        'age': ['18 - 29 Yrs', 'Above 30 Yrs'],
        'age_values': [
            [18.4, 17.4],
            [17.0, 17.1],
            [33.5, 32.9],
            [18.4, 15.1],
            [12.6, 17.5]
        ],
        'locality': ['Urban', 'Rural'],
        'locality_values': [
            [14.3, 18.5],
            [21.9, 16.0],
            [26.7, 34.6],
            [20.3, 15.3],
            [16.7, 15.6]
        ]
    }
}

# Get the selected color theme
if 'selected_theme' not in st.session_state:
    st.session_state.selected_theme = "Theme 1"

with st.sidebar:
    st.image('CPASI_logo.png', use_column_width=True)  # Add your logo path here
    st.markdown('<div class="main-title">Democracy & Reconciliation in Sri Lanka</div>', unsafe_allow_html=True)
    selected_theme = st.radio("Select Color Theme", ["Theme 1", "Theme 2"], index=0, key="theme_radio_sidebar")
    st.session_state.selected_theme = selected_theme

    if st.button("Go to Dashboard"):
        st.experimental_set_query_params(page="CIDGI_survey.py")
        st.experimental_rerun()
    if st.button("Home"):
        st.experimental_set_query_params(page="Home.py")
        st.experimental_rerun()


color_mapping = get_color_theme(st.session_state.selected_theme)

# Define a function to create horizontal bar charts
def create_horizontal_bar_chart(labels, values, title, height=400):
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
            orientation='v',
            yanchor='top',
            y=0.5,
            xanchor='left',
            x=1.05
        ),
        margin=dict(l=40, r=40, t=80, b=60),  # Adjust margins to make space for annotations
        height=height,  # Adjust the height of the chart
        width=800  # Adjust the width of the chart
    )
    return bar_fig

# Define a function to create horizontal clustered bar charts
def create_horizontal_clustered_bar_chart(labels, values, title, section, height=400, width=1000, legend_bottom=False):
    bar_fig = go.Figure()

    for idx, val in enumerate(values):
        bar_fig.add_trace(go.Bar(
            y=labels, x=val,
            name=survey_data[section]['national'][idx],
            marker_color=color_mapping.get(survey_data[section]['national'][idx], '#000000'),  # Handle missing colors gracefully
            text=[f"{v}%" for v in val], textposition='outside',  # Position text outside the bars and add percentage
            orientation='h'  # Horizontal orientation
        ))

    legend_dict = dict(
        orientation='v',
        yanchor='top',
        y=0.5,
        xanchor='left',
        x=1.05
    )
    
    if legend_bottom:
        legend_dict = dict(
            orientation='h',
            yanchor='bottom',
            y=-0.2,
            xanchor='center',
            x=0.5
        )

    bar_fig.update_layout(
        barmode='group',
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=18)),
        xaxis=dict(color='black'),
        yaxis=dict(color='black'),
        font=dict(color='black'),  # Set text color to black
        legend=legend_dict,
        margin=dict(l=40, r=40, t=80, b=80),  # Adjust margins to make space for annotations and legend
        height=height,  # Adjust the height of the chart
        width=width  # Adjust the width of the chart
    )
    return bar_fig

# Define a function to create pie charts
def create_pie_chart(labels, values, title, height=400):
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
            orientation='v',
            yanchor='top',
            y=0.5,
            xanchor='left',
            x=1.05
        ),
        margin=dict(l=40, r=40, t=80, b=60),  # Adjust margins to make space for annotations
        height=height,  # Adjust the height of the chart
        width=800  # Adjust the width of the chart
    )
    return pie_fig

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

# Placeholder for combined chart
combined_section = 'Overall Survey Data'
combined_labels = [
    "Finding alternative approaches to economic recovery", "Ensure anti-corruption measures", 
    "Ensure post-war reconciliation and transitional justice", "Uphold the democratic rights of the people", 
    "Addressing Unemployment", "Preserving law and order in the country", 
    "Hold those who are responsible for economic crisis accountable", 
    "Bring justice to the victims of the Easter Attack", 
    "Address the problems of minority communities", 
    "Will negotiate with the IMF for a better deal to resolve the economic crisis", 
    "Resolve the country’s Economic crisis"
]
combined_values = [
    [15.8, 25.8, 29.0, 19.0, 16.6, 19.7, 24.0, 20.8, 17.1, 16.7, 15.4],
    [17.8, 14.4, 13.3, 19.9, 20.3, 15.1, 14.0, 16.0, 25.0, 11.6, 19.9],
    [16.3, 22.2, 20.3, 20.3, 20.8, 22.9, 26.0, 12.3, 24.1, 10.4, 18.3],
    [17.0, 19.7, 23.1, 21.5, 24.6, 27.0, 18.0, 32.0, 17.4, 9.1, 12.4],
    [33.1, 17.8, 14.4, 19.4, 18.0, 15.4, 18.0, 18.9, 16.3, 52.3, 33.9]
]

combined_chart = create_horizontal_clustered_bar_chart(
    combined_labels, combined_values, "Overall Survey Data", 'Ensure anti-corruption measures', height=1100, width=1200, legend_bottom=True
)
st.plotly_chart(combined_chart)

# Detailed Survey Data
for section in survey_data.keys():
    st.markdown(f"<h2 style='color: #993300;'>{section}</h2>", unsafe_allow_html=True)
    
    data = survey_data[section]
    st.plotly_chart(create_pie_chart(data['national'], data['national_values'], f"{section} - National Level"))
    
    filter_option = st.radio("Filter by", ["Ethnicity", "Sex", "Age", "Locality"], key=f"{section}_filter_radio")
    
    if filter_option == "Ethnicity":
        bar_chart = create_horizontal_clustered_bar_chart(data['ethnicity'], data['ethnicity_values'], f"{section} by Ethnicity", section)
    elif filter_option == "Sex":
        bar_chart = create_horizontal_clustered_bar_chart(data['sex'], data['sex_values'], f"{section} by Sex", section)
    elif filter_option == "Age":
        bar_chart = create_horizontal_clustered_bar_chart(data['age'], data['age_values'], f"{section} by Age", section)
    elif filter_option == "Locality":
        bar_chart = create_horizontal_clustered_bar_chart(data['locality'], data['locality_values'], f"{section} by Locality", section)
    else:
        bar_chart = None

    if bar_chart:
        st.plotly_chart(bar_chart)
