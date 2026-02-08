import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="ANPR JPJ", layout="centered")

st.title("Sistem Pengesahan Nombor Plat JPJ (ANPR)")

uploaded_file = st.file_uploader(
    "Muat naik imej nombor plat kenderaan",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imej Nombor Plat", use_column_width=True)

    if st.button("Analisis Nombor Plat"):
        st.info("Sedang memproses imej...")

        detected_plate = "ABC1234"
        status = random.choice(["Patuh JPJ", "Tidak Patuh JPJ"])

        st.subheader("Keputusan Analisis")
        st.write(f"**Nombor Plat:** {detected_plate}")

        if status == "Patuh JPJ":
            st.success("✔ Status: PATUH JPJ")
        else:
            st.error("✖ Status: TIDAK PATUH JPJ")
            st.write("**Sebab Ketidakpatuhan:**")
            st.write("- Saiz aksara tidak seragam")
            st.write("- Jarak antara aksara tidak mengikut piawaian")
