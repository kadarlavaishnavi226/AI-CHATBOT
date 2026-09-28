import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ================= CSS =================
st.markdown("""
<style>

/* Entire application */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e3f2fd, #ffffff);
}

/* Main content area */
[data-testid="stMainBlockContainer"] {
    max-width: 900px;
    padding-top: 30px;
}

/* Title */
h1 {
    color: #1565c0 !important;
    text-align: center;
    font-size: 45px !important;
    font-weight: bold;
}

/* Headers */
h2 {
    color: #0d47a1 !important;
}

h3 {
    color: #1976d2 !important;
}

/* Text input */
[data-testid="stTextInput"] input {
    border: 2px solid #1976d2 !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* Text area */
[data-testid="stTextArea"] textarea {
    border: 2px solid #1976d2 !important;
    border-radius: 10px !important;
}

/* Number input */
[data-testid="stNumberInput"] input {
    border: 2px solid #1976d2 !important;
    border-radius: 10px !important;
}

/* Select box */
[data-testid="stSelectbox"] > div {
    border-radius: 10px !important;
}

/* Button */
[data-testid="stButton"] button {
    width: 100%;
    background-color: #1565c0 !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 12px !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Button hover */
[data-testid="stButton"] button:hover {
    background-color: #0d47a1 !important;
}

/* Caption */
[data-testid="stCaptionContainer"] {
    color: #555555;
}

/* Divider */
hr {
    border: 2px solid #90caf9;
}

/* Alert boxes */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Slider */
[data-testid="stSlider"] {
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)


# ================= CONTENT =================

st.title("🤖 AI CHATBOT")

st.header("ABOUT")
st.subheader("DETAILS")

st.text("HELLO WORLD")

st.markdown("**Hello World**")

st.caption("This is Caption")

st.code("print('Hello')", language="python")

st.latex(r"E=mc^2")

st.divider()


# ================= INPUTS =================

name = st.text_input("Enter your Name")

message = st.text_area("Enter your Message")

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    step=1
)

value = st.slider(
    "Select a value",
    0,
    100
)

option = st.selectbox(
    "Choose an Option",
    ["A", "B", "C"]
)

options = st.multiselect(
    "Choose options",
    ["A", "B", "C"]
)

choice = st.radio(
    "Select your Gender",
    ["Male", "Female", "Other"]
)

agree = st.checkbox("I agree")

status = st.toggle("Enable feature")


# ================= BUTTON =================

if st.button("CLICK ME"):

    date = st.date_input("Select a date")

    time = st.time_input("Select a time")

    file = st.file_uploader("Upload a file")

    color = st.color_picker(
        "Choose a color",
        "#000000"
    )

    st.success("Operation Completed Successfully!")

    st.info("This is some information")

    st.warning("Please Be Careful")

    st.error("Something Went Wrong")

    # DataFrame
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [20, 21, 22]
    })

    st.dataframe(df)

    st.table(df)

    # Metric
    st.metric("Sales", "₹50,000")

    # JSON
    data = {
        "Name": name,
        "Age": age,
        "Gender": choice
    }

    st.json(data)

    st.write("Hello World")

    # Camera
    st.camera_input("Take a Picture")