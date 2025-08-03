# Friendship Day Streamlit App for Tenu and Pragya

import streamlit as st
from PIL import Image
import base64

# Custom CSS for cuteness
custom_css = """
<style>
.friend-card {
    background: #fffbe7;
    border-radius: 20px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    padding: 2rem;
    margin: 1rem 0;
    text-align: center;
    transition: transform 0.2s;
}
.friend-card:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 32px rgba(0,0,0,0.12);
}
.cute-btn {
    background: #ffb6b9;
    color: #fff;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.5rem;
    font-size: 1.1rem;
    cursor: pointer;
    margin-top: 1rem;
    transition: background 0.2s;
}
.cute-btn:hover {
    background: #f67280;
}
.sparkle {
    animation: sparkle 1.5s infinite alternate;
}
@keyframes sparkle {
    0% { filter: brightness(1); }
    100% { filter: brightness(1.5); }
}
</style>
"""

st.set_page_config(page_title="Happy Friendship Day!", page_icon="🥰")
st.markdown(custom_css, unsafe_allow_html=True)

st.title("🥰 Happy Friendship Day! 🥰")
st.markdown("<h2 class='sparkle'>To my dearest friends, Tenu & Pragya!</h2>", unsafe_allow_html=True)

# Quotes and wishes
quotes = [
    "A friend is someone who knows all about you and still loves you. – Elbert Hubbard",
    "Friendship is the only cement that will ever hold the world together. – Woodrow Wilson",
    "Good friends are like stars. You don't always see them, but you know they're always there.",
    "A real friend is one who walks in when the rest of the world walks out. – Walter Winchell",
    "Friendship doubles your joy and divides your sorrow."
]

# Load images from local files
tenu_img = Image.open("WhatsApp Image 2025-08-03 at 22.32.08_75bece3f.jpg")
pragya_img = Image.open("WhatsApp Image 2025-08-03 at 22.32.08_818c2c49.jpg")


col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='friend-card'>", unsafe_allow_html=True)
    st.image(tenu_img, width=220, caption="Tenu")
    st.markdown("<h3>💖 Tenu 💖</h3>", unsafe_allow_html=True)
    st.write("Thank you for being my partner in crime, my secret keeper, and my endless source of laughter!")
    st.markdown(f"<b>Favourite Quote:</b> <i>\"{quotes[0]}\"</i>", unsafe_allow_html=True)
    # Only use Streamlit's button below the image
    if st.button("Click for a Surprise! 💝", key="tenu_btn_real"):
        st.balloons()
        st.markdown("""
        <div style='font-size:1.3rem; color:#f67280; margin-top:1rem;'>❤️❤️❤️❤️❤️❤️❤️❤️❤️<br>🎉 Happy Friendship Day, Tenu! You are awesome! 🎉<br>Here's to more fun, laughter, and memories together! 💖<br><span style='font-size:1.5rem;'>Celebrating <b>9 years</b> of our beautiful friendship! 🥰</span><br>❤️❤️❤️❤️❤️❤️❤️❤️❤️</div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <style>
        .stButton>button {
            animation: wiggle 0.4s 2;
        }
        @keyframes wiggle {
            0% { transform: rotate(-5deg); }
            25% { transform: rotate(5deg); }
            50% { transform: rotate(-5deg); }
            75% { transform: rotate(5deg); }
            100% { transform: rotate(0deg); }
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='friend-card'>", unsafe_allow_html=True)
    st.image(pragya_img, width=220, caption="Pragya")
    st.markdown("<h3>💖 Pragya 💖</h3>", unsafe_allow_html=True)
    st.write("Thank you for your kindness, your wisdom, and for always being there when I need you most!")
    st.markdown(f"<b>Favourite Quote:</b> <i>\"{quotes[1]}\"</i>", unsafe_allow_html=True)
    if st.button("Click for a Surprise! 💝", key="pragya_btn_real"):
        st.snow()
        st.markdown("""
        <div style='font-size:1.3rem; color:#f67280; margin-top:1rem;'>❤️❤️❤️❤️❤️❤️❤️❤️❤️<br>🎊 Happy Friendship Day, Pragya! You are awesome! 🎊<br>May our friendship always shine bright! 💖<br><span style='font-size:1.5rem;'>Celebrating <b>9 years</b> of our beautiful friendship! 🥰</span><br>❤️❤️❤️❤️❤️❤️❤️❤️❤️</div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <style>
        .stButton>button {
            animation: wiggle 0.4s 2;
        }
        @keyframes wiggle {
            0% { transform: rotate(-5deg); }
            25% { transform: rotate(5deg); }
            50% { transform: rotate(-5deg); }
            75% { transform: rotate(5deg); }
            100% { transform: rotate(0deg); }
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Friendship fun facts
with st.expander("🌟 Fun Friendship Fact!"):
    st.write("Did you know? According to a study, it takes about 200 hours to become good friends with someone!")

# Friendship Day wish
st.markdown("""
<div style='margin-top:2rem; text-align:center;'>
    <h2>Wishing us many more years of laughter, adventures, and memories together! 🥳</h2>
    <p style='font-size:1.3rem; color:#f67280;'><b>Happy Friendship Day, Tenu & Pragya!</b><br>
    <span style='font-size:1.5rem;'>With lots of love, Akansha</span><br>
    <span style='display:inline-block; margin-top:1rem; color:#ffb6b9;'>
        Celebrating <b>9 years</b> of our beautiful friendship! <span style='font-size:2rem;'>❤️❤️❤️❤️❤️❤️❤️❤️❤️</span>
    </span>
    </p>
</div>
""", unsafe_allow_html=True)
