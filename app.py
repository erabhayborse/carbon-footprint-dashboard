import streamlit as st
st.image("logo.png", width=120)

st.title("Personal Carbon Footprint Dashboard (Germany)")
st.markdown("""
### What is a carbon footprint?

A carbon footprint is the total amount of CO2 emissions caused by your daily activities. 
Travel, electricity use, flights, and even your diet all contribute to it.

### What does this tool do?

This tool gives you a simple estimate of your yearly carbon footprint. 
Adjust the values below to see how your lifestyle affects your emissions.
""")
st.write("")
# ---- Inputs ----
km = st.slider("Weekly travel (km)", 0, 500, 50)
electricity = st.slider("Monthly electricity (kWh)", 0, 1000, 200)
flights = st.slider("Flights per year (km)", 0, 20000, 1000)
diet = st.selectbox("Diet type", ["Vegetarian", "Mixed", "Heavy Meat"])

# ---- Emission factors ----
car = 0.21
power = 0.4
flight = 0.15

diet_values = {
    "Vegetarian": 1.5,
    "Mixed": 2.5,
    "Heavy Meat": 3.5
}

# ---- Calculation ----
total = (
    km * 52 * car +
    electricity * 12 * power +
    flights * flight +
    diet_values[diet] * 1000
)

tons = total / 1000
import pandas as pd

data = {
    "Category": ["Transport", "Electricity", "Flights", "Diet"],
    "CO2 (kg)": [
        km * 52 * car,
        electricity * 12 * power,
        flights * flight,
        diet_values[diet] * 1000
    ]
}

df = pd.DataFrame(data)

chart_data = df.set_index("Category")

st.bar_chart(chart_data)

st.caption("Y-axis shows CO2 emissions in kg per year")
# ---- Output ----
st.subheader(f"Your annual carbon footprint is {tons:.2f} tons CO2")
st.caption("This estimate is based on your lifestyle inputs (transport, energy, diet, and travel).")
st.progress(min(tons / 20, 1.0))

if tons > 11:
    st.write("Above Germany average")
else:
    st.write("Below Germany average")
    st.divider()

st.subheader("Recommendations")

tips = []

if km > 100:
    tips.append("Reduce car travel or switch to public transport")

if electricity > 300:
    tips.append("Use energy-efficient appliances or green electricity")

if flights > 5000:
    tips.append("Reduce flights or choose trains when possible")

if diet == "Heavy Meat":
    tips.append("Reduce meat consumption")
st.write(f"Your highest emissions come from **{df.loc[df['CO2 (kg)'].idxmax(), 'Category']}**")# ---- Show tips ----
if tips:
    for tip in tips:
        st.write(f"- {tip}")
else:
    st.success("Your lifestyle is already quite sustainable. Keep it up!")
 
if tons > 11:
    st.warning("Your emissions are higher than average. Small changes can make a big difference!")
else:
    st.info("You are doing better than average. Try optimizing further for even lower impact.")
st.caption("This is a simplified estimate and not a full carbon assessment.")
st.write("---")
st.caption("Developed by Abhay Borse")