# Calculating impact of donations
# Inspired by Efectiva Ayuda and using their data from here:
# https://ayudaefectiva.org/como-calculamos-impacto

import streamlit as st

# Calculate impact of donation to each charity
def calculate_impact(montly_amount,cost_per_recipient,impact_units,cost_per_death_averted):
    """
    Input parameters:
        montly_amount: float, amount donated per month (eur)
        cost_per_recipient: float, cost per recipient (e.g. child reached)
        impact_units: string, units of impact (e.g. children provided with vitamin A)
    cost_per_death_averted: float, cost to avert one death (eur)

    Returns:
        impact: dict, containing the following keys:
            - amount_per_year: float, amount donated per year (eur)
            - number_of_recipients: float, number of recipients reached per year
            - years_to_save_life: float, number of years to save a life
            - impact_units: string, units of impact (e.g. children provided with vitamin A)

    """

    # Calculate yearly amount donated
    amount_per_year = montly_amount * 12

    # Calculate number of recipients and years to save a life
    number_of_recipients = amount_per_year / cost_per_recipient

    # Calculate number of years to save a life (zero if no donation is made)
    if amount_per_year == 0:
        years_to_save_life = 0
    else:
        years_to_save_life = cost_per_death_averted / amount_per_year

    # Create dictionary to store results
    impact = {
        "amount_per_year": amount_per_year,
        "number_of_recipients": number_of_recipients,
        "years_to_save_life": years_to_save_life,
        "impact_units": impact_units
    }
    return impact

st.markdown("# Simulating the impact of your donations")

st.markdown("## Hellen Keller International")

# Impact numbers for Hellen Keller International (from Ayuda Efectiva)
# Impact umits
u_hki = "Children protected from vitamin A deficiency"
# Cost per child under 5 reached (eur)
c_hki = 2.0
# Cost per death averted (eur)
da_hki = 3500

# Make a slider for the user to input their monthly donation amount
a_hki = st.slider("Money donated per month to Hellen Keller International",0,100,0)

# Calculate impact
hki_impact = calculate_impact(a_hki, c_hki, u_hki, da_hki)

# Print out results
impact_list = hki_impact
st.write("You will donate €", impact_list["amount_per_year"], "per year")
st.write(impact_list["impact_units"],": ", round(impact_list["number_of_recipients"], 2)    )
st.write("Number of years to save a life: ", round(impact_list["years_to_save_life"], 2), "years.")



st.markdown("## Against Malaria Foundation")
# Impact numbers for Against Malaria (from Ayuda Efectiva)
# Impact umits
u_amf = "Children protected by insecticide-treated bed nets"
# Cost per child under reached (eur) 
c_amf = 6/1.8 # Each 6 eur bed net protects 1.8 children
# Cost per death averted (eur)
da_amf = 5000

# Make a slider for the user to input their monthly donation amount
a_amf = st.slider("Money donated per month to Against Malaria Foundation",0,100,0)

# Calculate impact
amf_impact = calculate_impact(a_amf, c_amf, u_amf, da_amf)

# Print out results
impact_list = amf_impact
st.write("You will donate €", impact_list["amount_per_year"], "per year")
st.write(impact_list["impact_units"],": ", round(impact_list["number_of_recipients"], 2)    )
st.write("Number of years to save a life: ", round(impact_list["years_to_save_life"], 2), "years.")


st.markdown("## New Incentives")
# Impact numbers for New Incentives (from Ayuda Efectiva)
# Impact umits
u_ni = "Children receiving all essential vaccines"
# Cost per child under reached (eur) 
c_ni = 126
# Cost per death averted (eur)
da_ni = 4000

# Make a slider for the user to input their monthly donation amount
a_ni = st.slider("Money donated per month to New Incentives",0,100,0)

# Calculate impact
ni_impact = calculate_impact(a_ni, c_ni, u_ni, da_ni)

# Print out results
impact_list = ni_impact
st.write("You will donate €", impact_list["amount_per_year"], "per year")
st.write(impact_list["impact_units"],": ", round(impact_list["number_of_recipients"], 2)    )
st.write("Number of years to save a life: ", round(impact_list["years_to_save_life"], 2), "years.")



st.markdown("## Malaria Consortium")
# Impact numbers for Malaria Consortium (from Ayuda Efectiva)
# Impact umits
u_mc = "Children provided preventive malaria treatment"
# Cost per child under reached (eur) 
c_mc = 7.
# Cost per death averted (eur)
da_mc = 3500

# Make a slider for the user to input their monthly donation amount
a_mc = st.slider("Money donated per month to Malaria Consortium",0,100,0)

# Calculate impact
mc_impact = calculate_impact(a_mc, c_mc, u_mc, da_mc)

# Print out results
impact_list = mc_impact
st.write("You will donate €", impact_list["amount_per_year"], "per year")
st.write(impact_list["impact_units"],": ", round(impact_list["number_of_recipients"], 2)    )
st.write("Number of years to save a life: ", round(impact_list["years_to_save_life"], 2), "years.")



st.markdown("## GiveDirectly")
# Impact numbers for GiveDirectly (from Ayuda Efectiva)
# Impact umits
u_gd = "People receiving cash transfers"
# Cost per child under reached (eur) 
c_gd = 245
# Cost per death averted (eur)
da_gd = 0 # No data available for GiveDirectly

# Make a slider for the user to input their monthly donation amount
a_gd = st.slider("Money donated per month to GiveDirectly",0,100,0)

# Calculate impact
gd_impact = calculate_impact(a_gd, c_gd, u_gd, da_gd)

# Print out results
impact_list = gd_impact
st.write("You will donate €", impact_list["amount_per_year"], "per year")
st.write(impact_list["impact_units"],": ", round(impact_list["number_of_recipients"], 2)    )
#st.write("Number of years to save a life: ", round(impact_list["years_to_save_life"], 2), "years.")


# Summary of donations and impact
st.markdown("# Summary")

st.write("Total amount donated per year: €", 
         round(hki_impact["amount_per_year"] + 
               amf_impact["amount_per_year"] + 
               ni_impact["amount_per_year"] + 
               mc_impact["amount_per_year"] + 
               gd_impact["amount_per_year"], 2))

st.write("Total number of lives improved per year: ",
         round(hki_impact["number_of_recipients"] +
               amf_impact["number_of_recipients"] +
               ni_impact["number_of_recipients"] +
               mc_impact["number_of_recipients"] +
               gd_impact["number_of_recipients"], 2))
