import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Mini App", page_icon="🛍️😊", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Choose a Page:", ["E-Commerce 🛒✨", "BMI Calculator ⚖️😊"])

# ============================================================
# 🛒 PAGE 1: E-COMMERCE CLONE
# ============================================================
if page == "E-Commerce 🛒✨":
    st.markdown("""
        <style>
            body { background-color: #f4f6f8; }
            .product-card { 
                background: white; 
                border-radius: 10px; 
                padding: 1rem; 
                box-shadow: 0px 4px 10px rgba(0,0,0,0.1); 
                text-align: center; 
                transition: transform 0.2s; 
            }
            .product-card:hover { transform: scale(1.03); }
            .product-name { 
                font-family: 'Poppins', sans-serif; 
                font-weight: 600; 
                margin-top: 0.5rem; 
                color: #2b5876; 
            }
            .footer { text-align: center; color: gray; font-size: 0.9rem; margin-top: 40px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; color:#2b5876;'>🛍️ ShopEasy — Your Mini Store 🌟</h1>", unsafe_allow_html=True)
    st.markdown("#### Browse the latest products — frontend-only demo (no checkout) 😄")

    products = [
        {"name": "Apple iPhone 15 📱", "img": "https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-model-unselect-gallery-1-202309?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1693594200619"},
        {"name": "Sony WH-1000XM5 Headphones 🎧", "img": "https://m.media-amazon.com/images/I/71o8Q5XJS5L._SL1500_.jpg"},
        {"name": "Nike Air Max Plus 👟", "img": "https://static.nike.com/a/images/t_web_pdp_936_v2/f_auto/47b7945e-a379-4c24-b9df-98f4eef178e5/NIKE+AIR+MAX+PLUS.png"},
        {"name": "MacBook Air M2 💻", "img": "https://root-nation.com/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2023/08/6efd6ab0-e5d1-11ec-be6c-b2fe04160b9a.cf_.jpg.webp"},
        {"name": "Samsung Galaxy Watch 6 ⌚", "img": "https://images.samsung.com/is/image/samsung/p6pim/in/2307/gallery/in-galaxy-watch6-r945-469954-sm-r945fzkains-537406789?$684_547_PNG$"},
        {"name": "Canon EOS 1500D 📸", "img": "https://m.media-amazon.com/images/I/914hFeTU2-L._SL1500_.jpg"},
    ]

    cols = st.columns(3)
    for i, product in enumerate(products):
        with cols[i % 3]:
            st.markdown(f"""
                <div class='product-card'>
                    <img src='{product["img"]}' width='220'>
                    <div class='product-name'>{product["name"]}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("💡 Frontend-only demo — inspired by Flipkart & Amazon UI 😊✨")

    st.markdown("""
        <div class='footer'>
            <br><hr><br>
            <strong>Created by:</strong> • Akshita Soni 🤍 • Gaurav Singh 😄 • Gajraj Singh 😊 • Divyansh Sharma ✨️
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# ⚖️ PAGE 2: BMI CALCULATOR
# ============================================================
elif page == "BMI Calculator ⚖️😊":
    st.markdown("""
        <style>
            .result-box { padding: 1.2rem; border-radius: 10px; text-align: center; font-size: 1.2rem; font-weight: 600; }
            .footer { text-align: center; color: gray; font-size: 0.9rem; margin-top: 40px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>⚖️ BMI Calculator 😊</h1>", unsafe_allow_html=True)
    st.markdown("#### Calculate your Body Mass Index easily with flexible unit options 😄")

    height_unit = st.radio("Select height unit:", ["Centimeters (cm) 📏", "Feet/Inches 🦶"], horizontal=True)
    if height_unit == "Centimeters (cm) 📏":
        height_cm = st.slider("Height (cm)", 100, 220, 170)
    else:
        col1, col2 = st.columns(2)
        with col1:
            height_feet = st.number_input("Feet", min_value=3, max_value=8, value=5)
        with col2:
            height_inches = st.number_input("Inches", min_value=0, max_value=11, value=7)
        height_cm = (height_feet * 12 + height_inches) * 2.54

    weight_unit = st.radio("Select weight unit:", ["Kilograms (kg) ⚖️😊", "Pounds (lbs) 🏋️‍♂️😊"], horizontal=True)
    if weight_unit == "Kilograms (kg) ⚖️😊":
        weight_kg = st.slider("Weight (kg)", 30, 150, 65)
    else:
        weight_lbs = st.slider("Weight (lbs)", 66, 330, 150)
        weight_kg = weight_lbs * 0.453592

    age = st.number_input("Age 🎂", 10, 100, 25, step=1)
    gender = st.radio("Gender", ["Male ♂️", "Female ♀️", "Other 🌈"], horizontal=True)

    st.markdown("---")
    if st.button("🧮 Calculate BMI 😊"):
        bmi = weight_kg / ((height_cm / 100) ** 2)
        if bmi < 18.5:
            category = "Underweight 🟡"
            color = "#f4d03f"
        elif 18.5 <= bmi < 24.9:
            category = "Normal ✅"
            color = "#58d68d"
        elif 25 <= bmi < 29.9:
            category = "Overweight 🟠"
            color = "#f39c12"
        else:
            category = "Obese 🔴"
            color = "#e74c3c"

        st.markdown(
            f"<div class='result-box' style='background-color:{color}; color:white;'>"
            f"Your BMI is <strong>{bmi:.2f}</strong><br>{category}</div>",
            unsafe_allow_html=True
        )

        with st.expander("ℹ️ About BMI Categories 😊"):
            st.write("""
            - **Underweight:** BMI less than 18.5  
            - **Normal weight:** BMI between 18.5 and 24.9  
            - **Overweight:** BMI between 25 and 29.9  
            - **Obese:** BMI 30 or more
            """)
    else:
        st.info("👉 Please choose your height and weight, then click **Calculate BMI** 😊")

    st.markdown("---")
    st.markdown("""
        <div class='footer'>
            <br><hr><br>
            <strong>Created by:</strong> • Akshita Soni 🤍 • Gaurav Singh 😄 • Gajraj Singh 😊 • Divyansh Sharma ✨️
        </div>
    """, unsafe_allow_html=True)
