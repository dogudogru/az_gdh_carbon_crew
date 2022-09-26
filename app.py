import streamlit as st
import pandas as pd
import numpy as np

from sections.sidebar import SideBarInput
from sections.exploration import ExplorationSection

st.set_page_config(layout="wide", page_title='CO2 Emission', page_icon=':orange_book')

sidebar = SideBarInput(
    title="Allianz Global",
    header="Data Hackathon",
)



outputs = []

try:
    exploration = ExplorationSection()
    outputs.append(exploration)
except Exception as e:
    print(e)