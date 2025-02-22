import streamlit as st
st.title("My First streamlit app")
st.header("I am header")
st.subheader("I am sub header")
st.write("Welcome to streamlit")
st.button("Click me")
st.radio("Choose an option:", [1, 2, 3])
st.text_input("Enter your name : ")
st.slider("Pick a number : ", 0,100)
st.selectbox("Choose:", ["a", "b", "c"])
st.checkbox("Check me")
st.image("https://images.pexels.com/photos/247819/pexels-photo-247819.jpeg?auto=compress&cs=tinysrgb&w=300")
# st.audio("audio.mp3")
# st.video("video.mp4")
st.file_uploader("Upload a file")
st.success("Success message!")
st.warning("Warning Message!")
st.info("Information Message!")
st.progress(50)

import pandas as pd
data = pd.DataFrame({"Column 1": [1, 2, 3], "Column 2":[4, 5, 6]})
st.table(data)
st.line_chart(data)
st.bar_chart(data)


import streamlit as st
# Title of the app
st.title("Simple Calculator")
# Input fields
st.header("Enter Your Numbers")
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)
# Dropdown menu for operation selection
operation = st.selectbox("Select an Operation:", ["Addition",
"Subtraction", "Multiplication", "Division"])
# Perform the operation based on user input
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
#         st.success(f"The result of addition is: {result}")
#     elif operation == "Subtraction":
#         result = num1 - num2
#         st.success(f"The result of subtraction is: {result}")
#     elif operation == "Multiplication":
#         result = num1 * num2
#         st.success(f"The result of multiplication is: {result}")
#     elif operation == "Division":
#         if num2 != 0:
#             result = num1 / num2
#             st.success(f"The result of division is: {result}")
#     else:
#         st.error("Division by zero is not allowed!")


import streamlit as st


# Create a custom header
st.markdown("""
    <style>
        /* Global style for header */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #131921;
            padding: 10px 20px;
            color: white;
            font-family: 'Arial', sans-serif;
        }

        .header .logo img {
            width: 100px;
        }

        .header .search-bar {
            display: flex;
            align-items: center;
            background-color: white;
            padding: 5px 10px;
            border-radius: 5px;
            width: 50%;
        }

        .header .search-bar input {
            width: 90%;
            border: none;
            padding: 8px;
            border-radius: 5px;
        }

        .header .search-bar button {
            background-color: #FF9900;
            border: none;
            padding: 8px;
            border-radius: 5px;
            cursor: pointer;
        }

        .header .nav-links a {
            color: white;
            text-decoration: none;
            padding: 0 10px;
            font-size: 16px;
            font-weight: 500;
        }

        .header .nav-links a:hover {
            text-decoration: underline;
        }

    </style>
    """, unsafe_allow_html=True)

# Header section (mimicking Amazon)
st.markdown('<div class="header">', unsafe_allow_html=True)

# Logo Section
st.markdown('<div class="logo"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" alt="Amazon Logo" /></div>', unsafe_allow_html=True)

# Search Bar Section
st.markdown("""
    <div class="search-bar">
        <input type="text" placeholder="Search for products, brands, and more" />
        <button>Search</button>
    </div>
""", unsafe_allow_html=True)

# Navigation Links (like Amazon header)
st.markdown('<div class="nav-links">', unsafe_allow_html=True)
st.markdown('<a href="#">Hello, Sign in</a>', unsafe_allow_html=True)
st.markdown('<a href="#">Returns & Orders</a>', unsafe_allow_html=True)
st.markdown('<a href="#">Cart</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Adding some content for testing the header
st.title("Welcome to the Simple Amazon Header")
st.write("Here you can test the layout of your app below the header.")



import streamlit as st
from datetime import datetime

# Function to calculate age
def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Title of the app
st.title("Age Calculator")

# Description of the app
st.write("""
This is a simple app to calculate your age based on the date of birth.
Please select your birthdate and the app will calculate your current age.
""")

# Input for the user's birthdate with a broader range
min_date = datetime(1900, 1, 1)  # Set to the minimum year you want to allow
max_date = datetime.today()  # Allow selecting any date up to today

birth_date = st.date_input("Select your birthdate:", min_value=min_date, max_value=max_date)

# If birthdate is selected, calculate age
if birth_date:
    age = calculate_age(birth_date)
    st.write(f"Your age is {age} years old.")

# Function to convert temperature from Celsius to other units
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

# Title of the app
st.title("Temperature Converter")

# Description of the app
st.write("""
This is a simple app to convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**.
Select the units and input the temperature value to perform the conversion.
""")

# User input for temperature value
value = st.number_input("Enter temperature value:", value=0.0)

# User input for selecting temperature units
from_unit = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion button
if st.button("Convert the temperature"):
    if from_unit != to_unit:
        converted_value = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
    else:
        st.write("Please select different units for conversion.")

# Dictionary of exchange rates for conversion (as of a certain date)
import streamlit as st

exchange_rates = {
    "GBP": 0.0044,  # 1 PKR to GBP (example rate)
    "USD": 0.0057,  # 1 PKR to USD (example rate)
    "CNY": 0.038,   # 1 PKR to CNY (example rate)
    "RUB": 0.42     # 1 PKR to RUB (example rate)
}

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    if from_currency == "PKR":
        conversion_rate = exchange_rates[to_currency]
        return amount * conversion_rate

# Title of the app
st.title("Currency Converter (PKR to GBP, USD, CNY, RUB)")

# Description of the app
st.write("""
This is a simple app that converts **PKR (Pakistani Rupee)** to **GBP (Pounds)**, **USD (Dollars)**, **CNY (Yuan)**, or **RUB (Ruble)**.
Choose the amount in PKR and select the currency you want to convert to.
""")

# Input for PKR amount
amount = st.number_input("Enter the amount in PKR:", min_value=1.0, step=1.0)

# Input for selecting target currency
to_currency = st.selectbox("Select target currency:", ["GBP", "USD", "CNY", "RUB"])

# Conversion button
if st.button("Convert the currency"):
    if amount > 0:
        converted_amount = convert_currency(amount, "PKR", to_currency)
        st.write(f"{amount} PKR is equal to {converted_amount:.2f} {to_currency}.")
    else:
        st.write("Please enter a valid amount in PKR.")
