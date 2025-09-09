import streamlit as st
import random

# نمایش عنوان
st.title("🎮 بازی سنگ، کاغذ، قیچی")

# گزینه‌ها
choices = {
    "کاغذ": "📄",
    "قیچی": "✂️",
    "سنگ": "🪨"
}

# انتخاب کاربر
user_choice = st.radio("انتخاب کن:", list(choices.keys()))

if st.button("شروع بازی"):
    # انتخاب کامپیوتر
    computer_choice = random.choice(list(choices.keys()))
    
    # نمایش انتخاب‌ها
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👤 شما")
        st.write(choices[user_choice])
    with col2:
        st.subheader("💻 کامپیوتر")
        st.write(choices[computer_choice])
    
    # منطق بازی
    if user_choice == computer_choice:
        st.info("🤝 مساوی شد!")
    elif (
        (user_choice == "کاغذ" and computer_choice == "سنگ") or
        (user_choice == "قیچی" and computer_choice == "کاغذ") or
        (user_choice == "سنگ" and computer_choice == "قیچی")
    ):
        st.success("🎉 شما بردید!")
    else:
        st.error("😢 باختید!")
