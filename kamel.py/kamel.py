import streamlit as st
import base64
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="ورشة محمود كامل", layout="wide")

# 2. دالة الخلفية
def set_bg_local(main_bg):
    try:
        with open(main_bg, "rb") as f:
            bin_str = base64.b64encode(f.read()).decode()
        st.markdown(f"""
            <style>
            .stApp {{ background: url(data:image/png;base64,{bin_str}); background-size: cover; background-attachment: fixed; }}
            .auth-box {{ background-color: rgba(0, 0, 0, 0.85); padding: 25px; border-radius: 15px; border: 2px solid #FFD700; color: white; max-width: 400px; margin: 0 auto; text-align: center; }}
            [data-testid="stSidebar"] {{ background-color: rgba(0, 0, 0, 0.7) !important; border-left: 2px solid #FFD700; }}
            .user-welcome {{ color: #FFD700; font-weight: bold; font-size: 18px; text-align: center; padding: 10px; border: 1px solid #FFD700; border-radius: 10px; }}
            .promo-box {{ background-color: rgba(0,0,0,0.7); padding: 20px; border-radius: 15px; border-right: 5px solid #FFD700; margin-bottom: 20px; }}
            h1, h2, h3, p, label {{ color: white !important; text-shadow: 1px 1px 3px black; text-align: right; }}
            </style>
            """, unsafe_allow_html=True)
    except: pass

set_bg_local('bg.jpg')

# 3. نظام قاعدة البيانات
DB_FILE = "users_db.txt"
def save_user(u, p):
    with open(DB_FILE, "a", encoding="utf-8") as f: f.write(f"{u}:{p}\n")
def check_user(u, p):
    if not os.path.exists(DB_FILE): return False
    with open(DB_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                name, pwd = line.strip().split(":")
                if name == u and pwd == p: return True
    return False

if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False

# --- شاشة الدخول ---
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align:center;'>ورشة محمود كامل للدعاية</h1>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["🔐 دخول", "📝 حساب جديد"])
    with t1:
        u_l = st.text_input("اسم المستخدم")
        p_l = st.text_input("كلمة السر", type="password")
        if st.button("دخول"):
            if check_user(u_l, p_l):
                st.session_state.update({"logged_in": True, "user_name": u_l})
                st.rerun()
            else: st.error("خطأ في البيانات")
    with t2:
        u_n = st.text_input("اسم جديد")
        p_n = st.text_input("كلمة سر جديدة", type="password")
        if st.button("إنشاء الحساب"):
            if u_n and p_n: save_user(u_n, p_n); st.success("تم! اذهب للدخول")

# --- محتوى الموقع (بعد الدخول) ---
else:
    # 1. الترحيب في الزاوية
    with st.sidebar:
        st.markdown(f'<div class="user-welcome">👋 أهلاً بك يا {st.session_state["user_name"]}</div>', unsafe_allow_html=True)
        if st.sidebar.button("تسجيل خروج"):
            st.session_state['logged_in'] = False
            st.rerun()

    st.markdown("<h1 style='text-align:center;'>ورشة محمود كامل للدعاية والإعلان</h1>", unsafe_allow_html=True)
    
    # 2. قسم الدعاية
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='promo-box'><h3>✨ قسم الإستانلس</h3><p>تصميمات ذهبية وفضية عصرية</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='promo-box'><h3>🍳 قسم المطابخ</h3><p>أحدث خامات الكلادينج وMDF</p></div>", unsafe_allow_html=True)

    # 3. خانة الحاسبة (فوق أرقام التواصل)
    with st.expander("🧮 اضغط هنا لفتح حاسبة المقاسات"):
        col_w = st.number_input("العرض", 0.0)
        col_h = st.number_input("الارتفاع", 0.0)
        if col_w * col_h > 0:
            st.success(f"المساحة الإجمالية: {col_w * col_h:.2f} متر مربع")

    # 4. أرقام التواصل (تحت خالص)
    st.markdown("""
    <div style='text-align:center; background: rgba(0,0,0,0.8); padding: 15px; border-radius: 15px; border: 1px solid #FFD700; margin-top:20px;'>
        <p>📞 01118524557 | 01001941060</p>
        <p>📧 k0482713@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)