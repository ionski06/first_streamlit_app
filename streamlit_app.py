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

# sl.dataframe(my_fruit_list)
