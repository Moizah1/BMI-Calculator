import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and see what category it falls into.")

# Let the user choose units
units = st.radio("Choose your units:", ["Metric (kg/cm)", "Imperial (lb/in)"], horizontal=True)

col1, col2 = st.columns(2)

if units == "Metric (kg/cm)":
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.5)
    with col2:
        height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.5)
    height_m = height / 100
    bmi = weight / (height_m ** 2)
else:
    with col1:
        weight = st.number_input("Weight (lb)", min_value=1.0, max_value=700.0, value=154.0, step=0.5)
    with col2:
        height = st.number_input("Height (in)", min_value=20.0, max_value=100.0, value=67.0, step=0.5)
    bmi = (weight / (height ** 2)) * 703

# Determine category
if bmi < 18.5:
    category = "Underweight"
    color = "#3498db"
elif bmi < 25:
    category = "Normal weight"
    color = "#2ecc71"
elif bmi < 30:
    category = "Overweight"
    color = "#f39c12"
else:
    category = "Obesity"
    color = "#e74c3c"

st.divider()

st.metric(label="Your BMI", value=f"{bmi:.1f}")

st.markdown(
    f"""
    <div style="padding: 12px; border-radius: 8px; background-color: {color}20; border: 1px solid {color};">
        <span style="color: {color}; font-weight: bold; font-size: 18px;">Category: {category}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

with st.expander("📊 BMI Categories Reference"):
    st.markdown(
        """
        | BMI Range     | Category        |
        |---------------|------------------|
        | Below 18.5    | Underweight      |
        | 18.5 – 24.9   | Normal weight    |
        | 25.0 – 29.9   | Overweight       |
        | 30.0 and up   | Obesity          |
        """
    )

st.caption("Note: BMI is a general screening tool and does not account for muscle mass, bone density, or body composition.")
