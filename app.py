import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

from sections.sidebar import SideBarInput
from sections.introduction import IntroductionSection
from sections.exploration import ExplorationSection
from sections.matching import MatchingSection
from sections.methodology import MethodologySection

st.set_page_config(layout="wide", page_title='CO2 Emission', page_icon=':orange_book')

logo = Image.open("img/carboncrew.png")
st.sidebar.image(logo)

pages = st.sidebar.radio("",('📖 Introduction', '📚 Methodology', '🔍 Exploration', '🧮 CO² Emission Calculator'))

sidebar = SideBarInput(
    title="Allianz Global",
    header="Data Hackathon Challenge",
)

co2_final = sidebar.co2_final


outputs = []

if pages == '📖 Introduction':

    try:
        introduction = IntroductionSection()
        outputs.append(introduction)
    except Exception as e:
        print(e)
        
elif pages == '📚 Methodology':

    try:
        methodology = MethodologySection()
        outputs.append(methodology)
    except Exception as e:
        print(e)

elif pages == '🔍 Exploration':

    try:
        exploration = ExplorationSection(co2_final)
        outputs.append(exploration)
    except Exception as e:
        print(e)

else:

    try:
        matching = MatchingSection(co2_final)
        outputs.append(matching)
    except Exception as e:
        print(e)
