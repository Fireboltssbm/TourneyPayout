import streamlit as st

st.header("Round Robin Calculator")
st.subheader("Useful for determining Round Robin Pools Lengths")
st.subheader("\n\tefficiency factor is 1.33")

st.subheader('\n\n')

average_time = st.number_input('Enter Average Time Per Set', 0)
number_players = st.number_input('Enter Number of Players/Teams in Pool', 0)
number_setups = st.number_input('Enter Number of Setups per pool', 1)

total_time: float = (1.33*average_time*(number_players*number_players-1))/(2*number_setups)


st.header('total time needed for round robin pools')
st.subheader(total_time)



with st.expander('LOGIC'):
    st.write("""
    kt(n(n-1)/2s\n
    k = efficiency factor
    t = average time per set
    n = number of players per pool
    s = setups
    """)
