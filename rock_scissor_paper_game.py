import streamlit as st
import random

# Title
st.title("🎮 Rock, Paper, Scissors Game")

# Choices
choices = {
    "Paper": "📄",
    "Scissors": "✂️",
    "Rock": "🪨"
}

# User choice
user_choice = st.radio("Choose your option:", list(choices.keys()))

if st.button("Play"):
    # Computer choice
    computer_choice = random.choice(list(choices.keys()))
    
    # Show choices
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👤 You")
        st.markdown(f"<h1 style='font-size:100px;'>{choices[user_choice]}</h1>", unsafe_allow_html=True)
        st.caption(user_choice)
    with col2:
        st.subheader("💻 Computer")
        st.markdown(f"<h1 style='font-size:100px;'>{choices[computer_choice]}</h1>", unsafe_allow_html=True)
        st.caption(computer_choice)
    
    # Game logic
    if user_choice == computer_choice:
        st.info("🤝 It's a tie!")
    elif (
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Rock" and computer_choice == "Scissors")
    ):
        st.success("🎉 You win!")
    else:
        st.error("😢 You lose!")

