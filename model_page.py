import streamlit as st
import joblib
import emoji

# Load model dan vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')


def show_model_page():
    st.title("Selamat Datang di Aplikasi Klasifikasi Teks Keluhan Konsumen 🌟")
    st.markdown("""
    Ini adalah aplikasi sederhana untuk mengklasifikasikan teks consumer complaint ke dalam beberapa kategori produk consumer berdasarkan model yang telah dilatih. Silakan masukkan kalimat di bawah dan tekan tombol 'Prediksi' untuk melihat kategori prediksi 🚀. """ )

    # Input teks dari pengguna
    user_input = st.text_area("Masukkan kalimat di sini:")

    # Tombol untuk prediksi
    if st.button("Prediksi"):
        if user_input:
            # Transformasi teks dengan TfidfVectorizer
            X_new = vectorizer.transform([user_input])
            
            # Prediksi dengan model
            prediction = model.predict(X_new)
            
            # Debugging print statement
            st.write(f"Prediction: {prediction}")
            st.write(f"Prediction type: {type(prediction[0])}")

            # Hasil prediksi adalah string kategori
            predicted_category = prediction[0]
            st.success(f"Kalimat terdeteksi sebagai: {predicted_category}")
        else:
            st.error("Masukkan kalimat terlebih dahulu!")


    st.write("""Hasil prediksi tersebut didapatkan dari hasil pelatihan model machine learning menggunakan vestorizer TF-IDF dan model Super Vector Machine""")

    # Informasi kelas-kelas produk
    class_info = """
    0. Credit reporting, repair, or other 📝
    1. Debt collection 💰
    2. Consumer Loan 🏦
    3. Credit card or prepaid card 💳
    4. Mortgage 🏠
    5. Vehicle loan or lease 🚗
    6. Student loan 🎓
    7. Payday loan, title loan, or personal loan 🏦
    8. Checking or savings account 💼
    9. Bank account or service 🏦
    10. Money transfer, virtual currency, or money service 💸
    11. Money transfers 💵
    12. Other financial service 🛠️
    """

    # Menampilkan informasi kelas-kelas produk
    st.markdown("### Kelas-kelas produk yang akan diklasifikasikan:")
    st.markdown(class_info)