import streamlit as st
import pandas as pd

# Title of the app
st.title('Enhanced Streamlit App')

# Taking input from the user
user_input = st.text_input('Enter some text')

# Button to display the input text
if st.button('Display Text'):
    st.write(f'You entered: {user_input}')

# Display a simple data table using Pandas
df = pd.DataFrame({
  'First column': [1, 2, 3, 4],
  'Second column': [10, 20, 30, 40]
})

st.write('Here is a simple data table:')
st.write(df)

st.write('The app is now enhanced!')