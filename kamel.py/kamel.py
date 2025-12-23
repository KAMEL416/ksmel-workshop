import streamlit as st
import base64
from datetime import date

# 1. إعدادات الصفحة (لازم تكون أول سطر في الكود)
st.set_page_config(page_title="ورشة محمود كامل", layout="wide", page_icon="🏗️")

# 2. دالة تشغيل الخلفية الشفافة (دي اللي بتشيل البياض)
def set_bg_local(main_bg):
    try:
        with open(main_bg, "rb") as f:
            bin_str = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/png;base64,{bin_str});
                background-size: cover;
                background-attachment: fixed;
            }}
            /* جعل المحتوى شفاف فوق الصورة */
            .main {{
                background-color: rgba(0,0,0,0);
            }}
            /* تنسيق الكلام عشان يبان */
            h1, h2, h3, p, label {{
                color: white !important;
                text-shadow: 2px 2px 5px black;
                text-align: right;
            }}
            /* تنسيق الصناديق عشان تكون واضحة */
            .stTextInput input, .stNumberInput input, .stSelectbox div {{
                background-color: rgba(255, 255, 255, 0.9) !important;
                color: black !important;
                border-radius: 10px !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("⚠️ يا محمود، حط صورة باسم bg.jpg في نفس الفولدر عشان تظهر الخلفية")

# تشغيل الخلفية
set_bg_local('bg.jpg')

# 3. واجهة الموقع
st.markdown("<h1 style='text-align: center;'>🏗️ ورشة محمود كامل للديكور والإستانلس</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>متخصصون في المطابخ العصرية وتجليد الواجهات</p>", unsafe_allow_html=True)

st.divider()

# 4. قائمة الشغل (المقايسات)
MATERIALS = [
    "✨ إستانلس ذهبي", "🥈 إستانلس فضي", 
    "🍳 مطبخ كلادينج", "🪵 مطبخ MDF", 
    "🏠 واجهة كلادينج", "🏛️ بديل رخام"
]

col1, col2 = st.columns(2)

with col1:
    customer_name = st.text_input("اسم العميل")
    material = st.selectbox("نوع الخامة/الشغل", MATERIALS)

with col2:
    width = st.number_input("العرض (متر)", min_value=0.0, step=0.1)
    height = st.number_input("الارتفاع (متر)", min_value=0.0, step=0.1)

area = width * height

if st.button("🚀 حفظ المقايسة"):
    if area > 0 and customer_name:
        st.balloons()
        with open("workshop_records.txt", "a", encoding="utf-8") as f:
            f.write(f"{date.today()} | {customer_name} | {material} | {area:.2f}م٢\n")
        st.success(f"تم الحفظ بنجاح: {customer_name}")
    else:
        st.error("أكمل البيانات أولاً")