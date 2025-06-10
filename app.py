import streamlit as st

st.set_page_config(page_title="Proses Pembuatan Kertas", layout="centered")

# ========== TEMA ==========
def get_css(theme):
    if theme == "Gelap":
        return """
        <style>
        body, .stApp {
            background-color: #0e1117;
            color: #f0f0f0;
        }
        </style>
        """
    return """
    <style>
    body, .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    </style>
    """

tema = st.radio("🎨 Pilih Tema", ["Terang", "Gelap"], horizontal=True)
st.markdown(get_css(tema), unsafe_allow_html=True)

# ========== KONTEN ==========
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧾 Dari Pulp Menjadi Kertas</h1>", unsafe_allow_html=True)
st.markdown("### 🌿 Website Edukasi tentang Proses Industri Kertas", unsafe_allow_html=True)

def image_from_url(url, caption=""):
    st.image(url, caption=caption, use_column_width=True)

# Animasi Umum
st.markdown("---")
st.markdown("### 📽️ Proses Secara Umum")
image_from_url("https://upload.wikimedia.org/wikipedia/commons/f/f0/Paper_machine_process_animation.gif", 
               caption="Animasi Proses Pembuatan Kertas")

# Penjelasan Proses
st.markdown("---")
st.markdown("### 🏭 Langkah-Langkah Pembuatan Kertas")

st.markdown("""
1. **Pemanenan Bahan Baku**
   - Kayu dari pohon pinus/eucalyptus dikupas dan dipotong.

2. **Pulping (Pengubahan Kayu Jadi Bubur)**
   - Proses mekanik & kimia untuk menghasilkan pulp.

3. **Pencucian dan Pemutihan**
   - Menggunakan klorin dioksida atau H₂O₂.

4. **Pembentukan Lembaran**
   - Bubur dikeringkan di atas kawat saringan.

5. **Pressing dan Pengeringan**
   - Ditekan dan dikeringkan dengan rol panas.

6. **Finishing & Pemotongan**
   - Dihaluskan dan dipotong sesuai ukuran.

""")

# Gambar Ilustrasi
st.markdown("### 🖼️ Diagram Proses")
image_from_url("https://www.researchgate.net/profile/Muhammad-Shahid-201/publication/336517632/figure/fig1/AS:817536936902658@1570972622504/Schematic-diagram-of-paper-making-process.png",
               caption="Diagram Proses dari ResearchGate")

# Penutup
st.markdown("---")
st.markdown("### 📘 Kesimpulan")
st.success("""
Pembuatan kertas melibatkan proses kompleks dari bahan baku alami hingga produk siap pakai.
Dengan metode yang efisien, industri kertas mendukung berbagai kebutuhan manusia modern.
""")

st.markdown("<center><sub>Dibuat dengan ❤️ menggunakan Python + Streamlit</sub></center>", unsafe_allow_html=True)