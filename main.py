import streamlit as st
import pandas as pd
import os

# Tên file lưu trữ
FILE_NAME = "IPP5029.csv"

# Khởi tạo file nếu chưa có
if not os.path.exists(FILE_NAME):
    df_init = pd.DataFrame(columns=["Tên", "Toán", "Văn", "Anh"])
    df_init.to_csv(FILE_NAME, index=False)

# Đọc dữ liệu hiện tại
df = pd.read_csv(FILE_NAME)

# Trạng thái số thứ tự học sinh đang được hiển thị
if 'index' not in st.session_state:
    st.session_state.index = 0

# Tổng số học sinh đã có
total_students = len(df)

# Hàm hiển thị dữ liệu học sinh hiện tại
def load_student(index):
    if index < total_students:
        student = df.iloc[index]
        return student["Tên"], student["Toán"], student["Văn"], student["Anh"]
    else:
        return "", 0.0, 0.0, 0.0

# Lấy thông tin hiện tại
name, math, literature, english = load_student(st.session_state.index)

# === Form nhập liệu ===
st.header("Thông tin học sinh")

st.markdown(f"**🧑‍🎓 Đang chỉnh sửa học sinh số: {st.session_state.index + 1}**")

name_input = st.text_input("Tên học sinh", value=name)
math_input = st.number_input("Điểm Toán", 0.0, 10.0, value=float(math))
literature_input = st.number_input("Điểm Văn", 0.0, 10.0, value=float(literature))
english_input = st.number_input("Điểm Anh", 0.0, 10.0, value=float(english))

# === Các nút điều khiển ===
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("◀ Quay lại"):
        # Lưu dữ liệu trước khi chuyển học sinh
        if name_input.strip() != "":
            if st.session_state.index < len(df):
                df.iloc[st.session_state.index] = [name_input, math_input, literature_input, english_input]
            else:
                df.loc[len(df)] = [name_input, math_input, literature_input, english_input]
            df.to_csv(FILE_NAME, index=False)
        if st.session_state.index > 0:
            st.session_state.index -= 1
        st.rerun()

with col2:
    if st.button("▶ Tiếp theo"):
        # Lưu dữ liệu trước khi chuyển học sinh
        if name_input.strip() != "":
            if st.session_state.index < len(df):
                df.iloc[st.session_state.index] = [name_input, math_input, literature_input, english_input]
            else:
                df.loc[len(df)] = [name_input, math_input, literature_input, english_input]
            df.to_csv(FILE_NAME, index=False)
        st.session_state.index += 1
        st.rerun()

# === Hiển thị biểu đồ ===
st.markdown("---")
if st.button("📊 Hiển thị biểu đồ"):
    df_chart = pd.read_csv(FILE_NAME)
    if not df_chart.empty:
        st.bar_chart(
            df_chart.set_index("Tên")[["Toán", "Văn", "Anh"]],
            use_container_width=True
        )
    else:
        st.warning("Chưa có dữ liệu học sinh để hiển thị.")
