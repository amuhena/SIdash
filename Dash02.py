import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout='wide')

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown('<div class="main-title" >A Rapid Survey on Regulation of Election Expenditure for Advocacy Strategies of CMEV</div>', unsafe_allow_html=True)

# Define your color themes
color_theme_1 = {
    'There should be limits on the amount of money a candidate can spend on election campaigns': '#007b8f',
    'There should not be any limits on the amount of money a candidate can spend on election campaigns': '#ffb100',
    'Don\'t Know/ Not sure': '#bdbdbd',
    'Aware': '#007b8f',
    'Not Aware': '#ffb100',
    'Yes, it will help to fully control the election expenditure as per the Act': '#007b8f',
    'Yes, it will help to control the election expenditure to a certain extent': '#ffb100',
    'No, it will not control the election expenditure at all': '#895273',
}

color_theme_2 = {
    'There should be limits on the amount of money a candidate can spend on election campaigns': '#003366',
    'There should not be any limits on the amount of money a candidate can spend on election campaigns': '#336699',
    'Don\'t Know/ Not sure': '#99ccff',
    'Aware': '#003366',
    'Not Aware': '#ffcc00',
    'Yes, it will help to fully control the election expenditure as per the Act': '#003366',
    'Yes, it will help to control the election expenditure to a certain extent': '#336699',
    'No, it will not control the election expenditure at all': '#895273',
}

# Define your datasets for each question
survey_data = {
    'Opinion on spending on the election campaign': {
        'national': ['There should be limits on the amount of money a candidate can spend on election campaigns', 'There should not be any limits on the amount of money a candidate can spend on election campaigns', 'Don\'t Know/ Not sure'],
        'national_values': [91.6, 3.9, 4.4],
        'ethnicity': ['Sinhala', 'Tamil', 'Up Country Tamil', 'Muslim'],
        'ethnicity_values': [
            [91.3, 95.5, 94.7, 88.4],
            [3.9, 1.9, 5.3, 7.0],
            [4.8, 2.6, 0.0, 4.7]
            
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [91.3, 92.0],
            [4.6, 3.4],
            [4.0, 4.7]
        ],
        'age': ['18-29 Years', 'Above 30 Years'],
        'age_values': [
            [92.2, 91.3],
            [4.8, 3.4],
            [2.9, 5.2]
        ],
    },
    'Awareness on Regulation of Election Expenditure Act': {
        'national': ['Aware', 'Not Aware'],
        'national_values': [21.5, 78.5],
        'ethnicity': ['Sinhala', 'Tamil', 'Up Country Tamil', 'Muslim'],
        'ethnicity_values': [
            [22.0, 24.0, 31.6, 10.1],
            [78.0, 76.0, 68.4, 89.9]
            
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [24.8, 18.2],
            [75.2, 81.8]
        ],
        'age': ['18-29 Years', 'Above 30 Years'],
        'age_values': [
            [19.7, 22.4],
            [80.3, 77.6]
        ],
    },
    'Perception on Regulation of Election Expenditure Act': {
        'national': ['Yes, it will help to fully control the election expenditure as per the Act', 'Yes, it will help to control the election expenditure to a certain extent', 'No, it will not control the election expenditure at all', 'Don\'t Know/ Not sure'],
        'national_values': [21.5, 78.5, 0.0, 0.0],
        'ethnicity': ['Sinhala', 'Tamil', 'Up Country Tamil', 'Muslim'],
        'ethnicity_values': [
            [5.3, 16.2, 23.8, 25.0],
            [53.1, 45.9, 47.1, 66.7],
            [39.9, 29.7, 29.4, 8.3],
            [1.8, 8.1, 0.0, 0.0]
        ],
        'sex': ['Male', 'Female'],
        'sex_values': [
            [9.9, 8.0],
            [45.3, 60.8],
            [43.0, 27.2],
            [1.7, 4.0]
        ],
        'age': ['18-29 Years', 'Above 30 Years'],
        'age_values': [
            [7.4, 9.9],
            [47.4, 54.2],
            [42.1, 33.9],
            [3.2, 2.5]
        ],
    }
}

# Display the logo
logo_path = "CPASI_logo.png"  # Update this with the actual path to your logo image
st.sidebar.image(logo_path, use_column_width=True, width=200)  # Adjust the width value as needed

# Add introductory text button
if st.sidebar.button('Show Introductory Text'):
    st.markdown("<h2 style='text-align: center; color: #0097B2;'>Introduction</h2>", unsafe_allow_html=True)
    intro_text = """
    This report is prepared by Social Indicator (SI), the survey research arm of the Centre for Policy Alternatives for the Centre for Monitoring Election Violence (CMEV) in order to provide a distinct perspective of the Regulation of Election Expenditure Act (Campaign Finance Act) from the public point of view. The Act, which was passed in the parliament on the 19th of January 2023, is the first framework to regulate election campaign finance in the country and aims to regulate expenditure incurred by recognized political parties, independent groups, and candidates at every election. 
    
    In this backdrop, the survey aims to evaluate the public opinion on election expenditure and their level of awareness on the Regulation of Election Expenditure Act. Going a step further, the survey strives to assess the public perception of the effectiveness of this legislation and their understanding of the individuals or entities that ought to be held accountable in the event of a violation of this Act. By seeking such public opinion, the survey anticipate to further stimulate public attention and awareness of the legislation, offering the masses a better platform to express their views regarding the Act. On the other hand, it will provide space for extending the legislation beyond institutional discourse, further strengthening the democratic foundation of the country.
    """
    st.markdown(intro_text)

# Add methodology text button
if st.sidebar.button('Show Methodology Text'):
    st.markdown("<h2 style='text-align: center;  color: #0097B2;'>Methodology</h2>", unsafe_allow_html=True)
    methodology_text = """
    The survey was carried out using a semi-structured questionnaire that was administered amongst a sample of 1350 individuals from the four main ethnic communities - Sinhala, Tamil, Up-Country Tamil, and Muslim. The sample locations for the survey were selected using multi-staged stratified random sampling technique while a random walk method was applied to select respondents within a location. Thus, the sample captured both men and women living in urban as well as rural localities in all 25 districts. The fieldwork for the survey was carried out between the 6th and 23rd of November 2023 where the data collection was conducted by 80 trained enumerators (male and female) belonging to all four main ethnic communities. Following the completion of the data collection process, the data set was weighted to reflect the actual district and ethnic proportion of the population. Finally, the data set was analyzed using the Statistical Package for Social Sciences (SPSS).
    """
    st.markdown(methodology_text)

# Select box for main headings
selected_heading = st.sidebar.radio("Select Main Heading", list(survey_data.keys()))

# Create link button for the report
st.sidebar.markdown("[For the Report-PDF](https://www.cpalanka.org/topline-report-democracy-reconciliation-in-sri-lanka/)")

# Define a function to get the selected color theme
def get_color_theme(theme):
    if theme == "Theme 1":
        return color_theme_1
    elif theme == "Theme 2":
        return color_theme_2

# Create layout with two columns
col1, col2 = st.columns([5, 1])

# Radio buttons for graphs and color theme in the right column
with col2:
    selected_graph = st.radio(
        "Select Graph to Display",
        ["National", "Ethnicity", "Sex", "Age"],
        key="right_radio"
    )

    selected_theme = st.radio("Select Color Theme", ["Theme 1", "Theme 2"], index=0, key="theme_radio")

# Get the selected color theme
color_mapping = get_color_theme(selected_theme)

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
        height=550  # Adjust the height of the chart
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
        margin=dict(l=40, r=40, t=80, b=160),  # Adjust margins to make space for annotations
        height=550  # Adjust the height of the chart
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
        height=550  # Adjust the height of the chart
    )
    return pie_fig

# Display selected graph in the left column
with col1:
    data = survey_data[selected_heading]
    chart_title = f"{selected_heading} by {selected_graph.lower().capitalize()}"
    if selected_graph == "National":
        st.plotly_chart(create_pie_chart(data['national'], data['national_values'], chart_title))
    elif selected_graph == "Ethnicity":
        st.plotly_chart(create_horizontal_clustered_bar_chart(data['ethnicity'], data['ethnicity_values'], chart_title))
    elif selected_graph == "Sex":
        st.plotly_chart(create_horizontal_clustered_bar_chart(data['sex'], data['sex_values'], chart_title))
    elif selected_graph == "Age":
        st.plotly_chart(create_horizontal_clustered_bar_chart(data['age'], data['age_values'], chart_title))
