import streamlit as st

st.title("welcome")
st.write(
    "welcome to bima web."
)
st.header("a rafe dawgh")
st.image("IMG_20250422_121644_814.jpg", width=150)

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
st.title("menyatakan perasaanku kepadamu")
st.header("maukah kamu menjadi pacarku")
pilih = st.choose_input("tulis mau atau tidak:",value=0, step=1)

if (pilih mau) ==0:
    st.write(f"{pilih} kamu jadi pacar aku")
else:
    st.write(f"{pilih} kamu harus jadi pacar aku")

import streamlit as st

def main_page():
    st.title("Halaman Utama")
    st.write("Ini adalah halaman utama aplikasi Streamlit.")
    st.write("Klik pada sidebar untuk ke halaman selanjutnya.")

def next_page():
    st.title("Halaman Selanjutnya")
    st.write("Selamat datang di halaman selanjutnya!")
    st.write("Anda bisa menambahkan konten apapun di sini.")
    # Example interactive element
    name = st.text_input("Masukkan nama Anda:")
    if name:
        st.write(f"Halo, {name}! Senang bertemu dengan Anda di halaman ini.")

def main():
    st.sidebar.title("Navigasi")
    page = st.sidebar.radio("Pilih halaman:", ("Halaman Utama", "Halaman Selanjutnya"))

    if page == "Halaman Utama":
        main_page()
    elif page == "Halaman Selanjutnya":
        next_page()

if __name__ == "__main__":
    main()


