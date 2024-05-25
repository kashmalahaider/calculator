import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

calc_button_pressed = st.button("Calculate")

def calculate(num1, num2, operation):
	if operation == "Add":
		return num1 + num2
	elif operation == "Subtract":
		return num1 - num2
	elif operation == "Multiply":
		return num1 * num2
	elif operation == "Divide":
		if num2 != 0:
			return num1 / num2
		else:
			return "Error: Division by zero"

if calc_button_pressed:
	result = calculate(num1, num2, operation)
	st.write("Result:", result)
