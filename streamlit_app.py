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

def get_fruityvice_data(this_fruit_choice):
  # write your own comment -what does the next line do? 
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
   if not  fruit_choice:
       streamlit.error("Please select a fruit") 
   else:
      function_result=get_fruityvice_data(fruit_choice)
      
# write your own comment - what does this do?
      streamlit.dataframe(function_result)
      streamlit.write('The user entered ', fruit_choice)
except UrlError as e:
     streamlit.error() 



import snowflake.connector

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe (my_data_rows)

def insert_row_snowflake (new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding " + new_fruit
      
add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets ["snowflake"])
    back_from_function = insert_row_snowflake (add_my_fruit)
    streamlit.text(back_from_function)    

streamlit.stop()

# Let's put a pick list here so they can pick the fruit they want to include 
add_my_fruit= streamlit.text_input('What fruit would you like information about?','Banana')
streamlit.write('Thank you for entering', add_my_fruit)
