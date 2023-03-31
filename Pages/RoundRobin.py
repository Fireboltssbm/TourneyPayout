import streamlit as st

st.header("Round Robin Calculator")
st.subheader("Useful for determining Round Robin Pools Lengths")

st.subheader('\n\n')

efficiency_factor = st.number_input('Enter Effiency Factor', 0)
average_time = st.number_input('Enter Average Time Per Set', 0)
number_players = st.number_input('Enter Number of Players/Teams in Pool', 0)
number_setups = st.number_input('Enter Number of Setups per pool', 0)

total_time = (efficiency_factor*average_time*(number_players*number_players-1))/(2*number_setups)


st.header('total time needed for round robin pools is' + str(total_time))



with st.expander('logic'):
    st.write("""
    kt(n(n-1)/2s\n
    k = efficiency factor
    t = average time per set
    n = number of players per pool
    s = setups
    """)
