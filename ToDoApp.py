import streamlit as st
from streamlit_extras.grid import grid


def layout():
    my_grid = grid([5, 1], vertical_align="bottom")
    data = my_grid.text_input("Enter Data")
    if my_grid.button("Add", use_container_width=True):
        st.title(data)


st.title("To-Do App")
layout()