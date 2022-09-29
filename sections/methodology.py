import pandas as pd
import streamlit as st
from PIL import Image

class MethodologySection():
    def __init__(self) -> None:

        st.title("Methodology")

        slide4 = Image.open("img/Slide4.png")
        slide5 = Image.open("img/Slide5.png")
        slide6 = Image.open("img/Slide6.png")
        slide7 = Image.open("img/Slide7.png")
        slide8 = Image.open("img/Slide8.png")
        slide9 = Image.open("img/Slide9.png")
        slide10 = Image.open("img/Slide10.png")
        slide11 = Image.open("img/Slide11.png")
        slide12 = Image.open("img/Slide12.png")

        st.image(slide4, caption="Data Analysis and Technical Reasoning")
        st.markdown("---")
        st.image(slide5, caption="Technical Structure")
        st.markdown("---")
        st.image(slide6, caption="High Level Structure")
        st.markdown("---")
        st.image(slide7, caption="Preprocessing")
        st.markdown("---")
        st.image(slide8, caption="Hierarchical Clustering Tree")
        st.markdown("---")
        st.image(slide9, caption="Figure 1")
        st.markdown("---")
        st.image(slide10, caption="Carbon Emission Prediction Model")
        st.markdown("---")
        st.image(slide11, caption="Carbon Emission Groups")
        st.markdown("---")
        st.image(slide12, caption="Program.sh")
        st.markdown("---")