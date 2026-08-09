import streamlit as st

st.title("Movie Ticket Booking System")

# Customer name
name = st.text_input("Enter your name")

# Movie selection
movie = st.selectbox(
    "Select your movie",
    ["Avengers", "Dangal", "3 Idiots", "Stree 2"]
)

# Show time selection
show_time = st.selectbox(
    "Select show time",
    ["10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM"]
)

# Number of tickets
tickets = st.number_input(
    "Number of tickets",
    min_value=1,
    max_value=10,
    value=1
)

# Ticket price
if movie == "Avengers":
    price = 250
elif movie == "Dangal":
    price = 200
elif movie == "3 Idiots":
    price = 180
else:
    price = 220

# Book button
if st.button("Book Tickets"):

    if name:
        total = price * tickets

        st.success("Booking Confirmed!")

        st.write(f"Hello{name}!")
        st.write(f" Movie:{movie}")
        st.write(f" Show Time:{show_time}")
        st.write(f" Tickets:{tickets}")
        st.write(f" Price per ticket:₹{price}")
        st.write(f" Total Amount: ₹{total}")

    else:
        st.warning("Please enter your name first.")