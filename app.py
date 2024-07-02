import streamlit as st
from model_page import show_model_page
from visualisasi_page import show_visualisasi_page
from welcome_page import show_welcome_page

page = st.sidebar.selectbox("Menu", ( "Welcome", "Klasfikasi Complent Data Customer", "Visualisasi Data"))

if page == "Welcome":
    show_welcome_page()
if page == "Klasfikasi Complent Data Customer":
    show_model_page()
if page == "Visualisasi Data":
   show_visualisasi_page()