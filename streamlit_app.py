import streamlit as st

st.title("welcome")
st.write(
    "welcome to bima web."
)
st.header("a rafe dawgh")
st.image("IMG_20250422_121644_814.jpg", width=200)

st.title("special day")
st.write(
    "never thought I could come this far with you 🙀.")
st.write(
    "siap sangka bisa kenal lebih dalam sama kylie 😲.")
st.image("IMG_20250424_190909_919.jpg", width=200)
st.write("\n")
st.title("TSB")
st.image("IMG-20250513-WA0069.jpg", width=200)
st.write(
    "Hari duper seruu sama mereka, meskipun capenya banget🖕🏼🖕🏼,")
st.write("\n")
st.write(
    "info adu lumpat💨🚀.")
st.video("VID-20250518-WA0012.mp4")
st.write("\n")
st.title("aplikasi sederhana")
st.header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("tulis sebuah angka:",value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil")
st.write("\n")
st.header("Rabu 21 Mei 2025")
st.write(
    "hari ini hari tercampur aduk")
st.image("1748603352323.jpg")

