import streamlit as st
from converter import convert_units


# Apply custom CSS styles for better UI
st.markdown("""
    <style>
         /* Main Title Styling */
    .main-title { 
        font-size: 32px; 
        font-weight: bold; 
        text-align: center; 
        color: #1E90FF;
        margin-bottom: 20px;
    }

    /* Subheading Styling */
    .sub-title {
        font-size: 24px;
        font-weight: bold;
        color: #ff6347;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    /* Buttons Styling */
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 8px;
        border: none;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #ff6347;
    }

    /* Sidebar Styling */
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: #228B22;
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Unit Converter")

# Sidebar for Unit Converter Information
st.sidebar.title("About the Unit Converter")
st.sidebar.write("""
This application allows you to convert between different units of measurement.
Simply select the type of conversion, choose the units, enter the value, and click 'Convert'.
""")
st.sidebar.write("### Benefits of Using the Unit Converter:")
st.sidebar.write("""
- **User-Friendly**: Intuitive interface for quick conversions.
- **Multiple Units**: Supports various types of units including length, weight, temperature, area, and volume.
- **Visual Representation**: Provides charts to visualize conversion factors.
""")

# Initialize default values
converter_type = "Length"
unit_from = "Meters"
unit_to = "Feet"
value = 0

# User input for conversion type
converter_type = st.selectbox("Please select your converter", ["Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"])
# Update unit options based on selected converter type
units = []


# Update unit options based on selected converter type
if converter_type == "Area":
    units = ["Square Meters", "Acres", "Hectares"]
elif converter_type == "Data Transfer Rate":
    units = ["Mbps", "Gbps", "Kbps"]
elif converter_type == "Digital Storage":
    units = ["Bytes", "Kilobytes", "Megabytes", "Gigabytes"]
elif converter_type == "Energy":
    units = ["Joules", "Calories", "Kilowatt-hours"]
elif converter_type == "Frequency":
    units = ["Hertz", "Kilohertz", "Megahertz"]
elif converter_type == "Fuel Economy":
    units = ["Miles per Gallon", "Kilometers per Liter"]
elif converter_type == "Length":
    units = ["Meters", "Kilometers", "Feet", "Inches"]
elif converter_type == "Mass":
    units = ["Kilograms", "Grams", "Pounds"]
elif converter_type == "Plane Angle":
    units = ["Degrees", "Radians"]
elif converter_type == "Pressure":
    units = ["Pascals", "Bar", "Atmospheres"]
elif converter_type == "Speed":
    units = ["Meters per Second", "Kilometers per Hour", "Miles per Hour"]
elif converter_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
elif converter_type == "Time":
    units = ["Seconds", "Minutes", "Hours"]
elif converter_type == "Volume":
    units = ["Liters", "Milliliters", "Gallons"]

col1, col2 = st.columns(2)
with col1:
    unit_from = st.selectbox("Select unit from", units)
with col2:
    unit_to = st.selectbox("Select unit to", units)


value = st.number_input("Enter value to convert", key="value_input")  # Added unique key

# Function to create conversion charts
def create_chart(converter_type):
    import matplotlib.pyplot as plt
    import numpy as np

    if converter_type == "Length":
        units = ["Meters", "Feet", "Kilometers", "Inches"]
        conversion_factors = [1, 3.28084, 0.001, 39.3701]
    elif converter_type == "Weight":
        units = ["Kilograms", "Pounds", "Grams"]
        conversion_factors = [1, 2.20462, 1000]
    elif converter_type == "Temperature":
        units = ["Celsius", "Fahrenheit"]
        conversion_factors = [1, 9/5]
    elif converter_type == "Area":
        units = ["Square Meters", "Acres", "Hectares"]
        conversion_factors = [1, 0.000247105, 0.0001]
    else:  # Volume
        units = ["Liters", "Gallons", "Cubic Meters"]
        conversion_factors = [1, 0.264172, 0.001]

    # Create a bar chart
    plt.bar(units, conversion_factors)
    plt.title(f'Conversion Factors for {converter_type}')
    plt.xlabel('Units')
    plt.ylabel('Conversion Factor')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

# Conversion button
if st.button("Convert", key="convert_button_1"):
    # Clear button to reset inputs
    if st.button("Clear", key="clear_button"):
        converter_type = "Length"  # Reset to default
        unit_from = "Meters"        # Reset to default
        unit_to = "Feet"            # Reset to default
        value = 0                   # Reset to default

    result = convert_units(converter_type, unit_from, unit_to, value)
    st.write(f"Converted value: {result}")
    create_chart(converter_type)  # Show chart after conversion











