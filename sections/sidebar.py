import streamlit as st
import pandas as pd


class SideBarInput:
    def __init__(self, title, header) -> None:
        self.title = title
        self.header = header

        @st.cache(allow_output_mutation=True)
        def get_data(url):
            return pd.read_csv(url)

        with st.sidebar:
            
          st.title(self.title)
          st.header(self.header)



          self.co2_final = get_data('data/co2_final.csv')
          self.co2_final = self.co2_final.drop(columns=['Unnamed: 0'])
          self.co2_final["fuel"] = self.co2_final["fuel"].astype(int)
          self.co2_final["drive_type"] = self.co2_final["drive_type"].astype(int)
          self.co2_final["seat"] = self.co2_final["seat"].astype(int)
          self.co2_final["Year"] = self.co2_final["Year"].fillna(0).astype(int)
          self.co2_final["fuel_type_desc"] = self.co2_final["fuel"].apply(lambda x: "Combustion Engine" if x==1 else ("Combustion Engine" if x==2 
                                                                 else ("Electric/Hydrogen" if x==4 else ("Combustion Engine" if x==6 
                                                                                          else ("Combustion Engine" if x==7 
                                                                                               else ("Hybrid" if x==8 
                                                                                                    else ("Combustion Engine" if x==9
                                                                                                         else "Hybrid" if x==10
                                                                                                         else ("Electric/Hydrogen" if x==15
                                                                                                              else ("Hybrid" if x==22
                                                                                                                   else ("Combustion Engine" if x==23
                                                                                                                        else ("Hybrid" if x==25
                                                                                                                             else ("Hybrid" if x==26
                                                                                                                                  else ("Combustion Engine" if x==34
                                                                                                                                       else ("Combustion Engine" if x==37
                                                                                                                                            else "Combustion Engine"))))))))))))))
          self.co2_final["size_cm3"] = (self.co2_final["height"] * self.co2_final["width"] * self.co2_final["lenght"]) / 1000000
     
          self.co2_final["inforce_co2"] = self.co2_final["inforce"] * self.co2_final["CO2 Emissions G/KM"]
          self.co2_final["market_co2"] = self.co2_final["market_qty"] * self.co2_final["CO2 Emissions G/KM"]
          self.co2_final["az_co2_share"] = self.co2_final["inforce_co2"] / self.co2_final["market_co2"]
          self.co2_final["power/weight"] = self.co2_final["power"] / self.co2_final["weight"]