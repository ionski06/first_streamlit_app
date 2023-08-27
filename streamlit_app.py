import streamlit as sl
import pandas as pd

sl.title("My Parents New Healthy Diner")

sl.header("Breakfast Menu")
sl.text("🥗 Omega 3 & Bluberry Oatmeal")
sl.text("🥣 Kale, Spinach and Rocket Smoothie")
sl.text("🐔 Hard-Boiled Free-Range Egg")

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = sl.multiselect("Pick some fruits", list(my_fruit_list['Fruit']),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list[my_fruit_list['Fruit'].isin(fruits_selected)]
sl.dataframe(fruits_to_show)

import requests
sl.header("Fruityvice Fruit Advice!")
fruit_choice = sl.text_input('What fruit would you like information about?','Kiwi')
sl.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# sl.text(fruityvice_response.json()) -- uni said to delete this

# normalizong the json data
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# making the normalized json into a dataframe
sl.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
