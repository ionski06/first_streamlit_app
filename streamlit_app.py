import streamlit
import pandas as pd
import snowflake.connector
import requests
from urllib.error import URLError

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


streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()
  
# streamlit.write('The user entered ', fruit_choice)

streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)

# new input box for another fruit
add_my_fruit = streamlit.text_input('What fruit would you like information about?','')
streamlit.write('The user entered ', add_my_fruit)

#inserting another row from SL/Git to Snowflake
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
