import streamlit as st
import pandas as pd

df = pd.read_csv('IPP5029.csv')

if 'index' not in st.session_state:
    st.session_state.index = 0

total_students = len(df)

def load_student(index):
    if index < total_students:
        student = df.iloc[index]
        return student["Tên"], student["Toán"], student["Văn"], student["Anh"]
    else:
        return "", 0.0, 0.0, 0.0

name, math, literature, english = load_student(st.session_state.index)

st.header("Thông tin học sinh")

st.markdown(f"**🧑‍🎓 Đang chỉnh sửa học sinh số: {st.session_state.index + 1}**")

name_input = st.text_input("Tên học sinh", value=name)
math_input = st.number_input("Điểm Toán", 0.0, 10.0, value=float(math))
literature_input = st.number_input("Điểm Văn", 0.0, 10.0, value=float(literature))
english_input = st.number_input("Điểm Anh", 0.0, 10.0, value=float(english))

c1, c2 = st.columns([1, 1])

with c1:
    if st.button("Quay lại"):
        if name_input.strip() != "":
            if st.session_state.index < len(df):
                df.iloc[st.session_state.index] = [name_input, math_input, literature_input, english_input]
            else:
                df.loc[len(df)] = [name_input, math_input, literature_input, english_input]
            df.to_csv('IPP5029.csv', index=False)
        if st.session_state.index > 0:
            st.session_state.index -= 1
        st.rerun()

with c2:
    if st.button("Tiếp theo"):
        if name_input.strip() != "":
            if st.session_state.index < len(df):
                df.iloc[st.session_state.index] = [name_input, math_input, literature_input, english_input]
            else:
                df.loc[len(df)] = [name_input, math_input, literature_input, english_input]
            df.to_csv('IPP5029.csv', index=False)
        st.session_state.index += 1
        st.rerun()

if st.button("Hiển thị biểu đồ"):
    df_chart = pd.read_csv('IPP5029.csv')
    if not df_chart.empty:
        st.bar_chart(
            df_chart.set_index("Tên")[["Toán", "Văn", "Anh"]],
            use_container_width=True
        )
    else:
        st.warning("Chưa có dữ liệu học sinh để hiển thị.")
