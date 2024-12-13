import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 구글 시트 인증 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('pages/credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("조석 이용 사례 제출").sheet1

# 제목 표시
st.title("조석의 이용 사례 과제 제출")

# 이미지 파일 경로
image1_path = "사진1.jpg"
image2_path = "사진2.jpg"

# 테이블 스타일로 구성
st.subheader("조석 이용 사례 과제 예시")

# 행을 맞추기 위해 수정된 레이아웃
row1_col1, row1_col2, row1_col3 = st.columns([1, 2, 3])
row2_col1, row2_col2, row2_col3 = st.columns([1, 2, 3])

# 첫 번째 행
with row1_col1:
    st.markdown("<div style='text-align: center;'><b>활동</b></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>조개 캐기</div>", unsafe_allow_html=True)
with row1_col2:
    st.markdown("<div style='text-align: center;'><b>이미지</b></div>", unsafe_allow_html=True)
    st.image(image1_path, caption="조개 캐기", width=150)
with row1_col3:
    st.markdown("<div style='text-align: center;'><b>설명</b></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>간조 때 넓게 드러난 갯벌에서 조개를 캔다.</div>", unsafe_allow_html=True)

# 두 번째 행
with row2_col1:
    st.markdown("<div style='text-align: center;'>고기잡이</div>", unsafe_allow_html=True)
with row2_col2:
    st.image(image2_path, caption="고기잡이", width=150)
with row2_col3:
    st.markdown("<div style='text-align: center;'>바다에 돌담이나 그물을 세우고 조류를 이용하여 물고기를 잡는다.</div>", unsafe_allow_html=True)

# 학생 제출 폼
st.subheader("학생 제출 폼")
name = st.text_input("이름")
activity = st.text_input("활동")
description = st.text_area("설명")
image_url = st.text_input("이미지 URL")

if st.button("제출"):
    if name and activity and description and image_url:
        sheet.append_row([name, activity, description, image_url])
        st.success("제출이 완료되었습니다!")
    else:
        st.error("모든 필드를 입력해주세요.")
