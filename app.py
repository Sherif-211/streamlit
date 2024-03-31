import streamlit as st

st.title("Калькулятор")

# creates a horizontal line
st.write("---")

# input 1
num1 = st.number_input(
label="Введите первое число")

# input 2
num2 = st.number_input(label="Введите второе число")

st.write("Операции")

operation = st.radio("Выберите операцию над числами:",("Сложение", "Вычитание", "Умножение", "Деление"))

ans = 0

def calculate():
    if operation == "Сложение":
        ans = num1 + num2
    elif operation == "Вычитание":
        ans = num1 - num2
    elif operation == "Умножение":
        ans = num1 * num2
    elif operation=="Деление" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("Ошибка при делении на 0. Пожалуйста, введите ненулевое число..")
        ans = "Not defined"

    st.success(f"Answer = {ans}")

if st.button("Результат"):
    calculate()