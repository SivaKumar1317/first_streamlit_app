import streamlit

streamlit.title('My Parent New Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text('🥗 Kale, spinach  & rocket smoothie')
streamlit.text('🐔 Hard-Bolied free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
