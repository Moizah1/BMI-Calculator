# ⚖️ BMI Calculator

A simple, interactive Body Mass Index (BMI) calculator built with [Streamlit](https://streamlit.io/).

## Features

- Supports **Metric (kg/cm)** and **Imperial (lb/in)** units
- Instantly calculates BMI as you adjust inputs
- Color-coded result showing your BMI category
- Reference table for BMI category ranges
- Clean, responsive UI

## Demo

Run the app locally and it will open in your browser at `http://localhost:8501`.

## Requirements

- Python 3.8+
- Streamlit

## Installation

1. Clone or download this repository / files.
2. Install dependencies:
   ```bash
   pip install streamlit
   ```

## Usage

Run the app with:

```bash
streamlit run bmi_calculator.py
```

Then:
1. Choose your preferred unit system (Metric or Imperial).
2. Enter your weight and height.
3. View your BMI and category instantly.

## BMI Categories

| BMI Range     | Category        |
|---------------|------------------|
| Below 18.5    | Underweight      |
| 18.5 – 24.9   | Normal weight    |
| 25.0 – 29.9   | Overweight       |
| 30.0 and up   | Obesity          |

## Disclaimer

BMI is a general screening tool and does not account for muscle mass, bone density, or overall body composition. It should not be used as a sole indicator of health. Consult a healthcare professional for personalized advice.
