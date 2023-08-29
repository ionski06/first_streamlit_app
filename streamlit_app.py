import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.text("🥗 Omega 3 & Bluberry Oatmeal")
streamlit.text("🥣 Kale, Spinach and Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick some fruits", list(my_fruit_list['Fruit']),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list[my_fruit_list['Fruit'].isin(fruits_selected)]
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# streamlit.text(fruityvice_response.json()) -- uni said to delete this

# normalizong the json data
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# making the normalized json into a df
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

 

print("Connecting...")

con = snowflake.connector.connect(
[snowflake]
user = "ionski16",
user = "ionski16"
password = "226962mB"
account = "OSUMQZB.GB61005"
warehouse = "pc_rivery_wh" 
database = "pc_rivery_db" 
schema = "public"
role= "accountadmin"

)

 

print(con)

 

con.cursor().execute("USE WAREHOUSE " + WAREHOUSE)

con.cursor().execute("USE DATABASE " + DATABASE)

 

try:

  result = con.cursor().execute("Select * from FRUIT_LOAD_LIST")

