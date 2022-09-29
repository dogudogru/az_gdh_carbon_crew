import streamlit as st
import pandas as pd
import plotly.express as px


class ExplorationSection():
    def __init__(self, co2_final) -> None:
        
        self.co2_final = co2_final

        st.title("Exploration")
        with st.expander("Take a look at sample dataframe with 10 rows 👇"):
            st.write(self.co2_final.sample(10))

        top10_emittors = self.co2_final[self.co2_final.origin == 'UK'][["identifier", "Manufacturer", "Model", "CO2 Emissions G/KM"]].sort_values(by="CO2 Emissions G/KM", ascending=False).head(10)
        top10_emittors["vehicle"] = top10_emittors["Manufacturer"] + " - " + top10_emittors["Model"] + " - " + top10_emittors["identifier"]
        
        fig = px.bar(top10_emittors, x="CO2 Emissions G/KM", y="vehicle", orientation='h')
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        fig.update_layout({
                                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                    })  

        top10_emittors_mkt = self.co2_final[self.co2_final.origin == 'UK'][["identifier", "Manufacturer", "Model", "market_co2"]].sort_values(by="market_co2", ascending=False).head(10)
        top10_emittors_mkt["vehicle"] = top10_emittors_mkt["Manufacturer"] + " - " + top10_emittors_mkt["Model"] + " - " + top10_emittors_mkt["identifier"]
        fig2 = px.bar(top10_emittors_mkt, x="market_co2", y="vehicle", orientation='h')
        fig2.update_layout(yaxis={'categoryorder':'total ascending'})
        fig2.update_layout({
                                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                    })

        col1, space1, col2 = st.columns((4,1,4))

        with col1:
            st.subheader("Vehicles with the highest CO2 emissions")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Vehicles that are causing the most CO2 emissions")
            st.plotly_chart(fig2, use_container_width=True)
        
        st.markdown("---")

        #Year visualisation in CO2 emission by fuel type and origin
        yearly_co2 = self.co2_final.groupby(['Year', 'origin', 'fuel_type_desc'], as_index=False)['CO2 Emissions G/KM'].mean()
        select_year_range = sorted(self.co2_final['Year'].unique())
        select_year_range = [e for e in select_year_range if e not in (0, 8037)]
        st.subheader("Yearly Average CO2 Emissions by Fuel Type")
        year = st.select_slider("Select year range", options=select_year_range, value=(2022, 2016))
        lrng, hrng = list(year)[0], list(year)[1]
        fig = px.scatter(yearly_co2.query(f"Year >= {lrng} & Year <= {hrng}"), 
                                        x="Year", 
                                        y="CO2 Emissions G/KM", 
                                        size="CO2 Emissions G/KM", 
                                        color="fuel_type_desc",
                                        hover_name="origin")

        fig.update_layout({
                                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                    })  

        st.plotly_chart(fig, use_container_width=True)  

        st.markdown("---")

        col1, space1, col2 = st.columns((5,1,10))

        with col1:
            st.subheader("Determining Factors in CO2 Emissions")
            select_chart = st.selectbox("Select chart type", options=["Engine Capacity (CC)","Car Mass", "Power/Weight Ratio"])
            
            if select_chart == "Engine Capacity (CC)":
                fig = px.scatter(self.co2_final, x="cc", y="CO2 Emissions G/KM", title=f"{select_chart}")
                fig.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        })
                st.plotly_chart(fig, use_container_width=True)
            elif select_chart == "Car Mass":
                fig = px.scatter(self.co2_final, x="weight", y="CO2 Emissions G/KM", title=f"{select_chart}")
                fig.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        })
                st.plotly_chart(fig, use_container_width=True)

            else:
                fig = px.scatter(self.co2_final, x="power/weight", y="CO2 Emissions G/KM", title=f"{select_chart}")
                fig.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        })
                st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Fuel Type Comparison with respect to CO2 Emissions")
            fig = px.box(yearly_co2, x="fuel_type_desc", y="CO2 Emissions G/KM", color="origin", title="Fuel Type")
            fig.update_layout({
                                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                    })  
            st.markdown("   ")
            st.markdown("   ")
            st.markdown("   ")
            st.markdown("   ")
            st.markdown("   ")
            st.markdown("   ")
            st.markdown("   ")
            st.markdown("   ")
            st.markdown("   ")

            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        fueltype_co2 = self.co2_final.groupby(['fuel_type_desc'], as_index=False)[['inforce_co2', 'market_co2']].sum()
        fueltype_co2["az_co2share"] = fueltype_co2["inforce_co2"] / fueltype_co2["market_co2"]

        st.subheader("Allianz&Market Comparison by Fuel Type and CO2 Emission")

        col1, space1, col2, space2, col3 = st.columns((4,1,4,1,4))

        with col1:
    
            fig = px.pie(fueltype_co2, values='inforce_co2', names='fuel_type_desc', title='Allianz - Total CO2 Emission')
            st.plotly_chart(fig, use_container_width=True)

        with col2:
    
            fig2 = px.pie(fueltype_co2, values='market_co2', names='fuel_type_desc', title='Market - Total CO2 Emission')
            st.plotly_chart(fig2, use_container_width=True)

        with col3:
    
            fig3 = px.bar(fueltype_co2, x="az_co2share", y="fuel_type_desc", orientation='h', title="Allianz's Market Share")
            fig3.update_layout(yaxis={'categoryorder':'total ascending'})
            fig3.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        })

            st.plotly_chart(fig3, use_container_width=True)