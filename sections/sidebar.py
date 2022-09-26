import streamlit as st
from PIL import Image


class SideBarInput:
    def __init__(self, title, header) -> None:
        self.title = title
        self.header = header
        
        with st.sidebar:
            logo = Image.open("img/carboncrew.png")
            st.image(logo)
            st.title(self.title)
            st.header(self.header)


