import streamlit as st

st.header("Tournament Payout Structure")
st.subheader("Useful for determining payout for participants in tourneys")

st.subheader('\n\n')

col1, col2 = st.columns(2, gap="medium")


with col1:
    money_cost = st.number_input('Enter Entry Fee', 0)
    number_entrant = st.number_input('Enter Entrant Count', 0)
    pot_bonus = st.number_input('Enter Pot Bonus', 0)

with col2:
    total_money = money_cost * number_entrant + pot_bonus
    if number_entrant < 10:
        first_place = total_money * .7
        second_place = total_money * .3
        st.write("1st place: " + str(first_place))
        st.write("2nd place: " + str(second_place))
    elif 10 <= number_entrant <= 20:
        first_place = total_money * .6
        second_place = total_money * .3
        third_place = total_money * .1
        st.write("1st place: " + str(first_place))
        st.write("2nd place: " + str(second_place))
        st.write("3rd place: " + str(third_place))
    elif 20 < number_entrant <= 30:
        first_place = total_money * .50
        second_place = total_money * .30
        third_place = total_money * .15
        fourth_place = total_money * .05
        st.write("1st place: " + str(first_place))
        st.write("2nd place: " + str(second_place))
        st.write("3rd place: " + str(third_place))
        st.write("4th place: " + str(fourth_place))
    elif 30 < number_entrant <= 40:
        first_place = total_money * .40
        second_place = total_money * .25
        third_place = total_money * .15
        fourth_place = total_money * .10
        fifth_place = total_money * .05
        st.write("1st place: " + str(first_place))
        st.write("2nd place: " + str(second_place))
        st.write("3rd place: " + str(third_place))
        st.write("4th place: " + str(fourth_place))
        st.write("5th place: " + str(fifth_place))
        st.write("5th place: " + str(fifth_place))
    else:
        first_place = total_money * .40
        second_place = total_money * .20
        third_place = total_money * .15
        fourth_place = total_money * .10
        fifth_place = total_money * .05
        seventh_place = total_money * .025
        st.write("1st place: " + str(first_place))
        st.write("2nd place: " + str(second_place))
        st.write("3rd place: " + str(third_place))
        st.write("4th place: " + str(fourth_place))
        st.write("5th place: " + str(fifth_place))
        st.write("5th place: " + str(fifth_place))
        st.write("7th place: " + str(seventh_place))
        st.write("7th place: " + str(seventh_place))


with st.expander('payout structure'):
    st.header("Payout Percentages")
    st.subheader("Under 10")
    st.write(" 70 / 30 ")
    st.subheader("more than 10 up until 20")
    st.write(" 60 / 30 / 10 ")
    st.subheader("more than 20 up until 30")
    st.write(" 50 / 30 / 15 / 5 ")
    st.subheader("more than 30 up until 40")
    st.write(" 40 / 25 / 15 / 10 / 5 / 5 ")
    st.subheader("41+")
    st.write(" 40 / 20 / 15 / 10 / 5 / 5 / 2.5 / 2.5 ")
