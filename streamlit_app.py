import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🐔 Chicken Tika Masalla')
streamlit.text('🍞 Moussaka')
streamlit.text('🥗 Greek Salad')
streamlit.text('🥑 Avocado Bowl')
streamlit.text('🥣 Chicken Soup')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
