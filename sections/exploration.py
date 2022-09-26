import pandas as pd
import streamlit as st
import plotly.express as px

class ExplorationSection():
    def __init__(self) -> None:

        @st.cache
        def get_data(url):
            return pd.read_csv(url)
        @st.cache
        def get_co2_data(): 
            # OWID Data on CO2 and Greenhouse Gas Emissions
            # Creative Commons BY license
            url = 'https://github.com/owid/co2-data/raw/master/owid-co2-data.csv'
            return get_data(url)

        st.title("CO2 Emission")
        df_co2= get_co2_data()

        st.write("""
        The graphs below show the CO2 emissions per capita for the entire 
        world and individual countries over time.
        Select a year with the slider in the left-hand graph and countries 
        from the drop down menu in the other one.
        Scroll down to see charts demonstrating the correlation between 
        the level of CO2 and global warming.
        Hover over any of the charts to see more detail
        """, unsafe_allow_html=True)

        col2, space2, col3 = st.columns((10,1,10))

        with col2:
            year = st.slider('Select year',1750,2020)
            fig = px.choropleth(df_co2[df_co2['year']==year], locations="iso_code",
                                color="co2_per_capita",
                                hover_name="country",
                                range_color=(0,25),
                                color_continuous_scale=px.colors.sequential.Reds)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('__Data Source:__ _Our World in Data CC BY_')

        with col3: 
            default_countries = ['World', 'United Kingdom', 'European Union (27)']
            countries = df_co2['country'].unique()
            
            selected_countries = st.multiselect('Select country or group', countries, default=default_countries)

            df3 = df_co2.query('country in @selected_countries' )

            fig2 = px.line(df3,"year","co2_per_capita",color="country")

            st.plotly_chart(fig2, use_container_width=True)
            st.markdown('__Data Source:__ _Our World in Data CC BY_')

        
        



