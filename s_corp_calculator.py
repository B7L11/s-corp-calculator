import streamlit as st

def calculate_s_corp_income(k1_2024, k1_2023, s_corp_2024, s_corp_2023, override_income):
    total_2024 = k1_2024 + s_corp_2024
    total_2023 = k1_2023 + s_corp_2023
    avg_income = (total_2024 + total_2023) / 24  # Monthly average
    trend = "Increasing Income" if total_2024 > total_2023 else "Decreasing/Unstable Income"

    return total_2024, total_2023, round(avg_income, 2), override_income, trend

st.title("S-Corp Income Calculator")

st.sidebar.header("Input Values")
k1_2024 = st.sidebar.number_input("Schedule K-1 Total (2024)", value=1297796.00)
k1_2023 = st.sidebar.number_input("Schedule K-1 Total (2023)", value=777815.00)
s_corp_2024 = st.sidebar.number_input("S-Corp Total (2024)", value=329520.00)
s_corp_2023 = st.sidebar.number_input("S-Corp Total (2023)", value=138854.00)
override_income = st.sidebar.number_input("Override Qualifying Income", value=95433.51)

if st.button("Calculate"):
    total_2024, total_2023, avg_income, qualifying_income, trend = calculate_s_corp_income(
        k1_2024, k1_2023, s_corp_2024, s_corp_2023, override_income
    )

    st.subheader("Results")
    st.write(f"**Total Income 2024:** ${total_2024:,.2f}")
    st.write(f"**Total Income 2023:** ${total_2023:,.2f}")
    st.write(f"**Average Monthly Income:** ${avg_income:,.2f}")
    st.write(f"**Qualifying Income (Override):** ${qualifying_income:,.2f}")
    st.write(f"**Income Trend:** {trend}")
