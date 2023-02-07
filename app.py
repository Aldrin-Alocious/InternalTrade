import streamlit as st
st.title('TTC Assignment')
tab1, tab2 = st.tabs(["Internal Trade", "Communication Services"])
tab1.subheader("Internal Trade")
op1=tab1.radio('Pick one', ['Whole Sale Trade', 'Retail Trade'])
if op1=='Whole Sale Trade':
  tab1.image('cd4da6f1-bb09-4e25-a203-48565df9a723.jpg')
elif op1=='Retail Trade':
  tab1.image('3719326c-f43f-417a-b6f1-1c4fe70ec865.jpg')
tab2.subheader("Communication Services")
op2=tab2.radio('Pick one', ['Post', 'Mobile', 'Television', 'Dish'])
if op2=='Post':
  tab2.image('52d4f12c-a36b-4346-ab91-531882e74196.jpg')
elif op2=='Mobile':
  tab2.image('53e1e72b-4c70-459a-8092-0ce2a2e18e10.jpg')
elif op2=='Television':
  tab2.image('40b399fd-bf64-49b8-9cc9-edb546e6405a.jpg')
elif op2=='Dish':
  tab2.image('b10217ce-310c-4e30-916b-80211835448c.jpg')
