import pandas as pd
import streamlit as st
import plotly.express as px

class IntroductionSection():
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

        st.title("From Vehicle Data to Sustainability")
        st.subheader("Global Warming and CO² Emissions")
        df_co2= get_co2_data()

        st.write("""
        <b>Paris Climate Agreement</b> was accepted on 5 October 2015 with the participation
        of <b>195 countries and the European Union</b>. Countries, that have signed a historic 
        decision to combat global warming, aim to reduce their global carbon emissions to <b>zero
        by 2050</b> in order to meet the target of keeping the global temperature rise <b>below 2 
        degrees Celsius</b>.""", unsafe_allow_html=True)

        st.write("""
        The graphs below show the CO2 emissions per capita for the entire 
        world and individual countries over time.
        Select a year with the slider in the left-hand graph and countries 
        from the drop down menu in the other one.
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
            fig2.update_layout({
                                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                    })  
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown('__Data Source:__ _Our World in Data CC BY_')


        st.write("""
        Sustainability matters more than ever, especially across Allianz Group. Allianz aims to be 
        a leading company on sustainability and shape the financial sector, inform public about climate
        urgency and Allianz's climate strategy, and be part of the conversation and engage in sustainability.""", unsafe_allow_html=True)

        st.write("""
        In order to achieve these goals, we, as Allianz, need to have end-to-end knowledge of sustainability in all processes 
        we are involved in, have a good command of sustainability methods and ESG terminology, and be able to apply this knowledge 
        in our personal and professional lives. One of the most important areas where we will apply this information is to our 
        motor portfolio. """, unsafe_allow_html=True)

        st.write("""
        As a result of the importance of our sustainability and carbon reduction targets, knowing the amount of carbon emitted 
        by the vehicles we insure will be of great benefit to us in determining the premiums. So how do we get this information 
        using the CO2 emissions data already available at certain OEs? How can we match existing information with the vehicle 
        portfolio from other OEs? Or how can we evaluate the CO2 emission information of vehicles on a global scale?

        As part of Global Data Hackathon Challenge, we, <b>Carbon C.R.E.W.</b>,  found solutions to these problems. Please, kindly go to next section to 
        find out our findings.
        """, unsafe_allow_html=True)

        st.markdown("---")

        
        



