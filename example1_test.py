import streamlit as st
import plotly.express as px
import pandas as pd



# Title of the app
st.title("Streamlit Dashboard with Plotly")

url="https://github.com/abtuchman/University_Dashboard_P2/blob/c9eb52f7d7d49ac300374da7cae0c75124f39d33/university_student_dashboard_data.csv?raw=true"
uni=pd.read_csv(url)

#convert year and term into one column
uni['Year'] = pd.to_datetime(uni['Year'], format='%Y')
uni['Year_Term'] = uni['Year'].dt.strftime('%Y') + ' ' + uni['Term']


#Plot admissions raw data
fig=px.line(uni, x='Year_Term', y=uni.columns[2:5],markers=True,color_discrete_sequence=["red", "blue", "green"])
fig.update_layout(
    title='Admissions Over Time',
    xaxis_title='Year and Term',
    yaxis_title='Count',
    yaxis_range=[0, max(uni['Applications'])+500],
    legend={'title_text':''}
)
fig.update_xaxes(tickangle=45)
fig.show()
#convert year and term into one column
uni['Year'] = pd.to_datetime(uni['Year'], format='%Y')
uni['Year_Term'] = uni['Year'].dt.strftime('%Y') + ' ' + uni['Term']


#Plot admissions raw data
fig=px.line(uni, x='Year_Term', y=uni.columns[2:5],markers=True,color_discrete_sequence=["red", "blue", "green"])
fig.update_layout(
    title='Admissions Over Time',
    xaxis_title='Year and Term',
    yaxis_title='Count',
    yaxis_range=[0, max(uni['Applications'])+500],
    legend={'title_text':''}
)
fig.update_xaxes(tickangle=45)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig)
