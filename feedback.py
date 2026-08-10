import streamlit as st
title = st.title("Customer feedback form")

st.header("We value your feedback")

name = st.text_input("Enter your name")

email = st.text_input("Enter your email")

rating = st.selectbox(
    "How would you rate your overall experience",
    ["select ratings", "Excellent", "Good", "Average", "Poor"],
    key = "rating"
)
experience = st.radio(
    "how was your overall experience",
    ["very satisfied", "satisfied", "neutral", "dissatisfied"],
    key = "experience"
)
recommend = st.radio(
    "would your recommend us to others",
    ["yes", "no"],
    key = "recommend"
)
feedback = st.text_area(
    "please share your feedback",
    placeholder = "please tell us what you liked and what we can improve..?"

)
st.divider()
if st.button("submit feedback"):
    
    if not name.strip():
        st.warning(
            "please enter your name first before submitting the feedback"
        )
    elif not email.strip():
        st.warning(
            "please enter your email first before submitting the feedback"
        )
    elif "@" not in email or "." not in email:
        st.warning(
            "please enter a valid Email address,"
            "For example: name@gmail.com"
        )
    elif rating == "select ratings":
        st.warning(
            "please select a rating for overall experience"
        )
    elif not feedback.strip():
        st.warning(
            "please share your feedback"
        )
    elif len(feedback.strip()) < 10:
        st.warning(
            "your feedback should contain at least 10 characters...add some more details about it"
        )
    else:
        st.success(
            "thanku for your valuable feedback, your feedback is submitted successfully"
        )
        st.balloons()
        st.divider()
        st.header("your feedback summary")
        st.write(f"NAME: {name}")
        st.write(f"EMAIL: {email}")
        st.write(f"RATING: {rating}")
        st.write(f"EXPERIENCE: {experience}")
        st.write(f"RECOMMEND: {recommend}")
        st.write(f"FEEDBACK: {feedback}")
