import streamlit as sl
import pandas as pd

sl.title("My Parents New Healthy Diner")

sl.header("Breakfast Menu")
sl.text("🥗 Omega 3 & Bluberry Oatmeal")
sl.text("🥣 Kale, Spinach and Rocket Smoothie")
sl.text("🐔 Hard-Boiled Free-Range Egg")

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
sl.multiselect("Pick some fruits", list(my_fruit_list.index),["Avocado","Strawberries"])
sl.dataframe(my_fruit_list)
