import streamlit as st
import pandas as pd
import glob
import os

st.title ('Excel Update App - Ενημέρωση υφιστάμενου αρχείου csv : data/users.csv & δημιουργία νέου αρχείου csv : data/users_new.csv')

df = pd.read_csv('data/users.csv')
st.header('Existing File : data/users.csv')
st.write(df)

st.sidebar.header('Options')
options_form = st.sidebar.form('options_form', clear_on_submit=True)
user_email = options_form.text_input('email') 
user_name = options_form.text_input('username')
user_real_name = options_form.text_input('name')
user_age = options_form.text_input('age')
add_data = options_form.form_submit_button()

if add_data:
   st.write(user_email, user_name, user_real_name, user_age)
   new_data = {'email': user_email, 'username': user_name,
              'name': user_real_name, 'age': int(user_age), 
              }
   st.write(new_data)
   df=df.append(new_data, ignore_index=True) 
   
   st.header('Existing File : data/users.csv - Updated')
   st.write(df)
   df.to_csv('data/users.csv', index=False)

   st.header('New File : data/users_new.csv - Created')
   st.write(df)
   df.to_csv('data/users_new.csv', index=False) 


   # download def   
   @st.cache
   def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

   csv1 = convert_df(df)
   csv2 = convert_df(df) 
   
   # download csv file users.csv
   st.download_button(
     label="Download data as users.CSV",
     data=csv1,
     file_name='users.csv',
     mime='text/csv',
     )
   
   st.download_button(
     label="Download data as users_new.CSV",
     data=csv2,
     file_name='users_new.csv',
     mime='text/csv',
     )


cwd = os.getcwd()
st.markdown('Directory :')
cwd



   





