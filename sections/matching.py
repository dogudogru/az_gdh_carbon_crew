import streamlit as st
import pandas as pd
import numpy as np
from pycaret.regression import *

class MatchingSection():
    def __init__(self, co2_final) -> None:
        
        self.co2_final = co2_final
        st.header("Match your vehicle and find out its CO2 emission")

        selectbox = st.selectbox("Chose one of the two options", options=("Find your car's CO2 emission by ABICODE/HSN-TSN number", 
                                                                "Calculate your car's CO2 emission by entering parameters"))

        if selectbox == "Find your car's CO2 emission by ABICODE/HSN-TSN number":
            
            radio = st.radio("Which code would you like to use?", options=("ABICODE (UK)", "HSN/TSN (GER)"))

            if radio == "ABICODE (UK)":
                abicode = st.text_input("Enter ABICODE")

                try:
                    abi_info = self.co2_final.loc[self.co2_final['identifier'] == abicode, 'CO2 Emissions G/KM'].iloc[0]
                    abi_manu = self.co2_final.loc[self.co2_final['identifier'] == abicode, 'Manufacturer'].iloc[0]
                    st.markdown(f"""This <b>{abi_manu}</b> vehicle with ABICODE number <b>{abicode}</b> seems to emit <b>{abi_info}</b> grams of CO2. """, unsafe_allow_html=True)
                except:
                    st.error("ABICODE could not be found!")

            else:
                col1, space1, col2, space2 = st.columns((5,1,5,15))
        
                with col1:
                    hsn = st.text_input("Enter HSN code")
                with col2:
                    tsn = st.text_input("Enter TSN code")

                hsn_tsn = hsn + "/" + tsn

                try:
                    hsn_info = self.co2_final.loc[self.co2_final['identifier'] == hsn_tsn, 'CO2 Emissions G/KM'].iloc[0]
                    hsn_manu = self.co2_final.loc[self.co2_final['identifier'] == hsn_tsn, 'Manufacturer'].iloc[0]
                    st.markdown(f"""This <b>{hsn_manu}</b> vehicle with HSN/TSN number <b>{hsn_tsn}</b> seems to emit <b>{np.round(hsn_info,1)}</b> grams of CO2. """, unsafe_allow_html=True)
                except:
                    st.error("HSN/TSN code could not be found!")

        else:
            model = load_model('data/saved_xgb_model_2')

            col1, space1, col2, space2, col3 = st.columns((5,1,5,1,5))

            with col1:
                fuel = st.selectbox("Fuel Type", options=(1, 2, 4, 6, 7, 8, 9, 10, 15, 22, 23, 25, 26, 34, 37))
                
            with col2:
                cc = st.number_input("Engine Capacity (CC)")

            with col3:                
                weight = st.number_input("Car Mass (kg)")

            col4, space3, col5, space4, col6 = st.columns((5,1,5,1,5))

            with col4:
                length = st.number_input("Length (mm)")
                
            
            with col5:
                height = st.number_input("Height (mm)")
                
            
            with col6:
                width = st.number_input("Width (mm)")
                
            
            col7, space5, col8, space6, col9, space7, col10 = st.columns((5,1,5,1,5,1,5))
            
            with col7:
                power = st.number_input("Power Output (kwh)")
            
            with col8:
                drive_type = st.selectbox("Drive Type", options=(1, 2, 3))
            
            with col9:
                speed = st.number_input("Speed (km/h)")
            
            with col10:
                seat = st.number_input("Number of Seats", min_value=1, max_value=300, step=1, value=4)

            space8, col11, space9 = st.columns((2,1,2))

            with col11:

                if st.button("Calculate CO2 Emission of your car"):
                    
                    data = {'fuel':fuel,
                            'cc':cc,
                            'weight':weight,
                            'power':power,
                            'lenght': length,
                            'drive_type':drive_type,
                            'height':height,
                            'width':width,
                            'speed':speed,
                            'seat':seat,}

                    df = pd.DataFrame.from_dict(data=[data],
                                                orient='columns')
                                                
                    st.code(float(predict_model(model, df)['Label']))

            st.markdown("---")
            st.write("Fuel Type and Drive Type fields are quite tricky to understand. Please refer below legends to understand input variables and choose your vehicle's technical information.")

            with st.expander("Fuel Type 👇"):
                
                st.markdown("""
                - 1 - Petrol
                - 2 - Diesel
                - 4 - Fully Electric
                - 6 - Petrol + LPG
                - 7 - Petrol + CNG
                - 8 - Petrol Hybrid
                - 9 - CNG
                - 10 - Diesel Hybrid
                - 15 - Fuelcell/Hydrogen
                - 22 - CNG Hybrid
                - 23 - Petrol + Ethanol
                - 25 - Petrol Plug-in Hybrid
                - 26 - Diesel Plug-in Hybrid
                - 34 - Ethanol + Petrol 
                - 37 - LNG + Diesel
                """, unsafe_allow_html=True)

            with st.expander("Drive Type 👇"):

                st.markdown("""
                - 1 - Two Wheel Drive / Four Wheel Drive
                - 2 - All Wheel Drive
                - 3 - Trucks, Bigger Vehicles
                """, unsafe_allow_html=True)
