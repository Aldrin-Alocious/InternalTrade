import streamlit as st
tab1, tab2 = st.tabs(["Internal Trade", "Communication Services"])
tab1.write("Internal Trade")
op1=st.selectbox('Pick one', ['Whole Sale Trade', 'Retail Trade'])
if op1=='Whole Sale Trade':
  tab1.image('cd4da6f1-bb09-4e25-a203-48565df9a723.jpg')
elif op1=='Retail Trade':
  tab1.image('3719326c-f43f-417a-b6f1-1c4fe70ec865.jpg')
tab2.write("Communication Services")
op2=st.selectbox('Pick one', ['Post', 'Mobile', 'Television', 'Dish'])
if op2=='Post':
  tab2.image('cd4da6f1-bb09-4e25-a203-48565df9a723.jpg')
elif op2=='Mobile':
  tab2.image('3719326c-f43f-417a-b6f1-1c4fe70ec865.jpg')
elif op2=='Television':
  tab2.image('3719326c-f43f-417a-b6f1-1c4fe70ec865.jpg')
elif op2=='Dish':
  tab2.image('3719326c-f43f-417a-b6f1-1c4fe70ec865.jpg')
