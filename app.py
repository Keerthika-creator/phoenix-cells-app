import streamlit as st
from PIL import Image
import base64

# --- Function to set background ---
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set your background image
set_background("background.jpg.jpeg")

# --- Page setup ---
st.set_page_config(page_title="Phoenix Cells", page_icon="🔥", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

html, body, [class*="css"]  {
    font-family: 'Orbitron', sans-serif;
    color: #00eaff;
}

h1 {
    font-size: 3rem !important;
    text-shadow: 0 0 10px #00eaff, 0 0 20px #00eaff;
    text-align: center;
}

h3 {
    color: #ff6600;
    text-shadow: 0 0 10px #ff6600;
    text-align: center;
}

button, .stButton>button {
    background-color: transparent;
    color: #00eaff;
    border: 2px solid #00eaff;
    padding: 0.5em 1em;
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
}
button:hover {
    background-color: #00eaff;
    color: black;
    box-shadow: 0 0 20px #00eaff;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.image("logo.png.jpeg", width=120)
st.markdown("<h1>Phoenix Cells</h1>", unsafe_allow_html=True)
st.markdown("<h3>AI Battery Revival & CT Scanning</h3>", unsafe_allow_html=True)

# --- About ---
st.write("""
Phoenix Cells scans lithium-ion batteries without opening them.
It detects microcracks, bulging, and overheating.
Then it predicts if the battery can be revived using nanotechnology healing.
""")

# --- Upload Section ---
uploaded_file = st.file_uploader("Upload a Thermal Battery Image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Thermal Image", use_column_width=True)
    st.success("Image uploaded successfully.")
    st.info("AI analysis will be displayed here.")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 Phoenix Cells | Sustainability First")
