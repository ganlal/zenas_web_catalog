import streamlit
import snowflake.connector
streamlit.title('My parents new healthy dinner')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
