import pandas as pd
import plotly.express as px
import streamlit as st

def plot(title, fig):
    st.write(title)
    st.plotly_chart(fig, use_container_width=True)

vehicles_data = pd.read_csv('vehicles_us.csv')

fig_1 = px.histogram(
    vehicles_data,
    title="Vehicles Paint Color Histogram",
    x="paint_color",
    labels={'paint_color':'paint color'},
)

fig_2 = px.histogram(
    vehicles_data,
    title="Vehicles Price Histogram",
    x="price",
)

fig_3 = px.histogram(
    vehicles_data,
    title="Vehicles Model Year Histogram",
    x="model_year",
    labels={'model_year':'model year'},
)

fig_4 = px.scatter(
    vehicles_data, 
    title="Vehicles Price vs Odometer Scatter Plot",
    x="odometer", 
    y="price",
    color="cylinders",
)

fig_5 = px.scatter(
    vehicles_data, 
    title="Vehicles Price vs Model Year Scatter Plot",
    x="model_year", 
    y="price",
    labels={'model_year':'model year'},
    color="cylinders",
)

fig_6 = px.scatter(
    vehicles_data, 
    title="Vehicles Price vs Model Scatter Plot",
    x="model", 
    y="price",
    color="cylinders",
)

st.header("Vehicles Dataset Data Visualization")

fig_1_checkbox = st.checkbox('Vehicles Paint Color Histogram')
fig_2_checkbox = st.checkbox('Vehicles Price Histogram')
fig_3_checkbox = st.checkbox('Vehicles Model Year Histogram')
fig_4_checkbox = st.checkbox('Vehicles Price vs Odometer Scatter Plot')
fig_5_checkbox = st.checkbox('Vehicles Price vs Model Year Scatter Plot')
fig_6_checkbox = st.checkbox('Vehicles Price vs Model Scatter Plot')

if fig_1_checkbox: 
    plot("Vehicles Paint Color Histogram", fig_1)
if fig_2_checkbox: 
    plot("Vehicles Price Histogram", fig_2)
if fig_3_checkbox: 
    plot("Vehicles Price Histogram", fig_3)
if fig_4_checkbox: 
    plot("Vehicles Price Histogram", fig_4)
if fig_5_checkbox: 
    plot("Vehicles Price Histogram", fig_5)
if fig_6_checkbox: 
    plot("Vehicles Price vs Model Scatter Plot", fig_6)

