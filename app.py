import streamlit as st

st.set_page_config(page_title="Smoke test", layout="wide")
st.title("✅ Render funciona")
st.write("Si ves este texto, el frontend está bien.")
st.slider("Prueba el slider", 0, 100, 50)
