import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import ask_grok

st.set_page_config(page_title="AI Manajemen Keuangan Mahasiswa", layout="wide")

st.title("📘 AI Manajemen Keuangan Mahasiswa")
st.write("Aplikasi untuk membantu mahasiswa menganalisis pemasukan, pengeluaran, dan mendapatkan rekomendasi berbasis AI.")

# ---- INPUT DATA ----
st.header("📥 Input Data Keuangan")

income = st.number_input("Pemasukan Bulanan (Rp)", min_value=0, step=10000)
expense_food = st.number_input("Pengeluaran Makan (Rp)", min_value=0, step=5000)
expense_transport = st.number_input("Transportasi (Rp)", min_value=0, step=5000)
expense_other = st.number_input("Pengeluaran Lainnya (Rp)", min_value=0, step=5000)

total_expense = expense_food + expense_transport + expense_other

if st.button("Simpan Data"):
    st.success("Data berhasil disimpan sementara.")

# ---- ANALISIS MANUAL ----
st.header("📊 Analisis Keuangan")

if income > 0:
    sisa = income - total_expense

    st.write(f"**Total Pengeluaran:** Rp {total_expense:,.0f}")
    st.write(f"**Sisa Uang:** Rp {sisa:,.0f}")

    # Grafik
    fig, ax = plt.subplots()
    kategori = ['Makan', 'Transport', 'Lainnya']
    nilai = [expense_food, expense_transport, expense_other]
    ax.bar(kategori, nilai)
    st.pyplot(fig)

# ---- AI FEATURE ----
st.header("🤖 Rekomendasi AI")

if st.button("Dapatkan Saran dari AI"):
    prompt = f"""
    Saya mahasiswa dengan pemasukan {income}.
    Pengeluaran makan {expense_food}, transportasi {expense_transport}, lainnya {expense_other}.
    Buat analisis dan saran manajemen keuangan yang jelas, singkat, dan mudah dipahami mahasiswa.
    """
    ai_reply = ask_grok(prompt)
    st.info(ai_reply)
