import streamlit as st

st.set_page_config(page_title="Python Cool Game")

# عنوان بازی
st.title("🎮 Python Cool Game")

# استفاده از session_state برای دنبال کردن مراحل بازی
if "stage" not in st.session_state:
    st.session_state.stage = "start"

# شروع بازی
if st.session_state.stage == "start":
    st.write("Welcome to the Python Cool Game.")
    st.write("You are at a crossroad. Which direction do you choose?")
    choice = st.radio("Choose your path:", ["Left", "Right"])

    if st.button("Submit Choice"):
        if choice.lower() == "right":
            st.session_state.stage = "hole"
        elif choice.lower() == "left":
            st.session_state.stage = "beach"
        st.experimental_rerun()

# اگر چپ رو انتخاب کنه
elif st.session_state.stage == "beach":
    st.write("You have reached the beach.")
    st.write("Now you must decide how to get to the island.")
    travel = st.radio("Do you want to wait for the boat or swim?", ["Wait", "Swim"])

    if st.button("Submit Travel Choice"):
        if travel.lower() == "wait":
            st.session_state.stage = "island"
        else:
            st.session_state.stage = "shark"
        st.experimental_rerun()

# مرحله نهایی در جزیره
elif st.session_state.stage == "island":
    st.write("You reached the island safely.")
    st.write("Final step: Choose the correct door to win!")
    door = st.radio("Which door do you choose?", ["Blue", "Yellow", "Green"])

    if st.button("Submit Door Choice"):
        if door.lower() == "blue":
            st.session_state.stage = "win"
        else:
            st.session_state.stage = "trap"
        st.experimental_rerun()

# پیام‌های مربوط به پایان بازی
elif st.session_state.stage == "hole":
    st.error("You fell in a hole. Game Over!")

elif st.session_state.stage == "shark":
    st.error("A big shark bit you. Game Over!")

elif st.session_state.stage == "trap":
    st.error("You fell into a trap. Game Over!")

elif st.session_state.stage == "win":
    st.success("Hooray! You win the game! 🎉")

# دکمه‌ی شروع مجدد بازی
if st.session_state.stage != "start":
    if st.button("Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
