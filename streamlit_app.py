import streamlit as st
import pandas as pd
import requests
import snowflake.connector

st.title("My Parents New Healthy Diner")

st.header("Breakfast Menu")
st.text("🥗 Omega 3 & Bluberry Oatmeal")
st.text("🥣 Kale, Spinach and Rocket Smoothie")
st.text("🐔 Hard-Boiled Free-Range Egg")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = st.multiselect("Pick some fruits", list(my_fruit_list['Fruit']),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list[my_fruit_list['Fruit'].isin(fruits_selected)]
st.dataframe(fruits_to_show)

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)

# Accessing Snowflake secrets
snowflake_secrets = st.secrets["snowflake"]

my_cnx = snowflake.connector.connect(**snowflake_secrets)
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)



