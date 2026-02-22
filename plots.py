import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

st.header('Altair Scatter Plot')
chart_data = pd.DataFrame(np.random.randn(500,4), columns = ['a','b','c','d'])
chart = alt.Chart(chart_data).mark_circle().encode(x = 'a', y = 'b', size = 'c', tooltip = ['a','b','c','d'])
st.altair_chart(chart)

st.header('Interactive Chart')
st.subheader('Line Chart')
df = pd.read_csv("I:\Streamlit\lang_data.csv")
lang_list = df.columns.tolist()
lang_choices = st.multiselect('Choose your Language', lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)

st.subheader('Area Chart')
st.area_chart(new_df)


st.header('Data Visulization with plotly')
st.subheader('Display the dataset')
df = pd.read_csv("I:/Streamlit/tips.csv")
st.dataframe(df.head())

st.subheader('Pie Chart')
fig = px.pie(df, values = 'total_bill', names = 'day')
st.plotly_chart(fig)


st.subheader('Pie Chart with multiple Parameters')
fig = px.pie(df, values = 'total_bill', names = 'day', opacity = .7, color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.header('Histogram')
x1 = np.random.randn(100)
x2 = np.random.randn(100)
x3 = np.random.randn(100)
hist_data = [x1,x2,x3]
group_labels = ['Group - 1', 'Group - 2', 'Group - 3']
fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1,.2,5])
st.plotly_chart(fig)
