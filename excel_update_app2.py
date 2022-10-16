import streamlit as st
import pandas as pd
import glob
import os

st.title ('Excel Update App - Ενημέρωση υφιστάμενου αρχείου csv : data/users.csv & δημιουργία νέου αρχείου csv : data/users_new.csv')

df = pd.read_csv('data/users.csv')
st.header('Existing File : data/users.csv')
st.write(df)

st.sidebar.header('Options')
options_form = st.sidebar.form('options_form')
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
   st.header('New File : data/users_new.csv - Created')
   st.write(df)
   st.header('Existing file : /data/users.csv has been updated.')
   df.to_csv('data/users.csv', index=False)
   st.header('New file : /data/users_new.csv has been created.')
   df.to_csv('data/users_new.csv', index=False)



cwd = os.getcwd()
st.markdown('Directory :')
cwd
   





