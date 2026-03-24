# Personal Carbon Footprint Dashboard (Germany)

An interactive web application built with Python and Streamlit that estimates a person's annual carbon footprint based on everyday lifestyle inputs.

Live App: https://carbon-footprint-dashboard.streamlit.app/
GitHub: https://github.com/erabhayborse/carbon-footprint-dashboard

---

## About This Project

This project translates everyday activities — travel, electricity use, flights, and diet — into measurable CO2 emissions and presents the results in a simple, visual format.

The goal is to make carbon accounting accessible to non-technical users and help them understand which part of their lifestyle contributes most to their emissions.

---

## How It Works

The calculation follows a standard carbon accounting formula:

```
CO2 emissions = activity data × emission factor
```

### User Inputs

| Input | Description |
|-------|-------------|
| Weekly travel distance | km per week by car |
| Monthly electricity consumption | kWh per month |
| Annual flight distance | km per year |
| Diet type | Vegetarian, Mixed, or Heavy Meat |

### Emission Factors

| Category | Factor |
|----------|--------|
| Transport | 0.21 kg CO2 per km |
| Electricity | 0.4 kg CO2 per kWh |
| Flights | 0.15 kg CO2 per km |
| Diet | 1,500 – 3,500 kg CO2 per year |

Transport and electricity values are scaled to annual figures before calculation. Diet uses fixed annual estimates based on food consumption research.

---

## Output

The application provides:

- Total annual carbon footprint in tons CO2 per year
- Progress bar comparison against Germany national average (~8 tons/year)
- Bar chart showing emission breakdown by category
- Identification of the highest contributing source
- Personalised reduction recommendations based on inputs

---

## App Screenshots

### Dashboard Interface
![Dashboard](figures/dashboard_header.png)

### Input Sliders
![Inputs](figures/input_sliders.png)

### Emission Breakdown Chart
![Chart](figures/emission_chart.png)

### Result Output
![Result](figures/result_output.png)

---

## Repository Structure

```
carbon-footprint-dashboard/
├── README.md
├── app.py
├── requirements.txt
├── logo.png
└── figures/
    ├── dashboard_header.png
    ├── input_sliders.png
    ├── emission_chart.png
    └── result_output.png
```

---

## How to Run

**Python:** 3.11+ | **Framework:** Streamlit

```bash
pip install -r requirements.txt
streamlit run app.py
```

Or access the deployed version directly:
https://carbon-footprint-dashboard.streamlit.app/

---

## Technologies Used

Python · Streamlit · Pandas · Carbon Accounting · Data Visualisation

---

## Limitations

This is a simplified model intended for awareness and educational purposes. It does not include:

- Regional electricity grid mix variation
- Detailed dietary intake modelling
- Full Life Cycle Assessment
- Transport mode differentiation (car vs public transport vs cycling)

---

## Planned Improvements

- Region-specific electricity emission factors
- Differentiated transport modes
- Improved diet modelling
- User data session tracking

---

## References

- German Environment Agency (UBA) — Average per capita emissions Germany
- IPCC AR6 (2021) — Emission factor guidance
- Defra (2023) — GHG Conversion Factors for emissions reporting

---

Abhay Gulabrao Borse | M.Sc. Environmental and Resource Management | BTU Cottbus-Senftenberg
