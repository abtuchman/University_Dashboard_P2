import streamlit as st
import plotly.express as px
import pandas as pd



# Title of the app
st.title("Streamlit Dashboard with Plotly")

#Load Data
url="https://github.com/abtuchman/University_Dashboard_P2/blob/c9eb52f7d7d49ac300374da7cae0c75124f39d33/university_student_dashboard_data.csv?raw=true"
uni=pd.read_csv(url)

#convert year and term into one column
uni['Year'] = pd.to_datetime(uni['Year'], format='%Y')
uni['Year_Term'] = uni['Year'].dt.strftime('%Y') + ' ' + uni['Term']

#Plot admissions raw data
fig1=px.line(uni, x='Year_Term', y=uni.columns[2:5],markers=True,color_discrete_sequence=["red", "blue", "green"])
fig1.update_layout(
    title='Admissions Over Time',
    xaxis_title='Year and Term',
    yaxis_title='Count',
    yaxis_range=[0, max(uni['Applications'])+500],
    legend={'title_text':''},
    xaxis_showgrid=True
)
fig1.update_xaxes(tickangle=45)
fig1.show()

#Plot retention rate
fig2=px.line(uni, x='Year_Term', y=uni.columns[5],markers=True,color_discrete_sequence=["orange"])
fig2.update_layout(
    title='Retention Rate Over Time',
    xaxis_title='Year and Term',
    yaxis_title='Retention Rate (%)',
    yaxis_range=[0, 100],
    legend={'title_text':''},
    xaxis_showgrid=True
)
fig2.update_xaxes(tickangle=45)
fig2.show()

#Plot student satisfaction
fig3=px.line(uni, x='Year_Term', y=uni.columns[6],markers=True,color_discrete_sequence=["magenta"])
fig3.update_layout(
    title='Student Satisfaction Over Time',
    xaxis_title='Year and Term',
    yaxis_title='Student Satisfaction (%)',
    yaxis_range=[0, 100],
    legend={'title_text':''},
    xaxis_showgrid=True
)
fig3.update_xaxes(tickangle=45)
fig3.show()

#Plot percentage enrollment of each department
import plotly.graph_objects as go

total_admissions = uni['Enrolled']
engineering_percentage = (uni['Engineering Enrolled']/ total_admissions) * 100
business_percentage = (uni['Business Enrolled'] / total_admissions) * 100
arts_percentage = (uni['Arts Enrolled']/ total_admissions) * 100
science_percentage = (uni['Science Enrolled']/ total_admissions) * 100

uni['engineering_percentage'] = engineering_percentage
uni['business_percentage'] = business_percentage
uni['arts_percentage'] = arts_percentage
uni['science_percentage'] = science_percentage

fig4 = go.Figure()

fig4.add_trace(go.Bar(
    x=uni['Year_Term'],
    y=uni['engineering_percentage'],
    name='Engineering',
    marker_color='red'
))

fig4.add_trace(go.Bar(
    x=uni['Year_Term'],
    y=uni['business_percentage'],
    name='Business',
    marker_color='green'
))

fig4.add_trace(go.Bar(
    x=uni['Year_Term'],
    y=uni['arts_percentage'],
    name='Arts',
    marker_color='yellow'
))

fig4.add_trace(go.Bar(
    x=uni['Year_Term'],
    y=uni['science_percentage'],
    name='Science',
    marker_color='blue'
))

fig4.update_layout(
    barmode='stack',
    title='Percentage of Enrolled Students by Department Over Time',
    xaxis_title='Year and Term',
    yaxis_title='Percentage of Enrolled Students',
    xaxis_tickangle=-45
)
fig4.show()

# Display the Plotly chart in Streamlit
# Layout - Using Tabs to Display Multiple Plots
tab1, tab2, tab3, tab4 = st.tabs(["Admission", "Retention", "Student Satisfaction", "Enrollment by Department"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.plotly_chart(fig4, use_container_width=True)
