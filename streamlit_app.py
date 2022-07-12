import streamlit
import pandas
import requests
from urllib.error import URLError

streamlit.title('My parent''s new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('Omega 3')
streamlit.text('Kale')
streamlit.text('Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])

# Display the table on the page.
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.header("Fruityvice Fruit Advice!")



try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
   if not  fruit_choice:
       streamlit.error("Please select a fruit") 
   else 
  # write your own comment -what does the next line do? 
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
    streamlit.dataframe(fruityvice_normalized)
    streamlit.write('The user entered ', fruit_choice)
except UrlError as e:
     streamlit.error() 
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()




my_cur.execute("select * from fruit_load_list")
my_data_rows=my_cur.fetchall();

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_rows)

streamlit.header("Fruit load list contains")
streamlit.dataframe(my_data_rows)


# Let's put a pick list here so they can pick the fruit they want to include 
add_my_fruit= streamlit.text_input('What fruit would you like information about?','Banana')
streamlit.write('Thank you for entering', add_my_fruit)
