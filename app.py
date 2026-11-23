import random
import streamlit as st

# 웹페이지 제목 및 아이콘 설정
st.set_page_config(page_title="점심 메뉴 추천기", page_icon="🍱")

st.title("🍱 오늘의 점심 메뉴 추천")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 뽑아보세요.")

# 추천할 점심 메뉴 목록 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "제육볶음",
    "왕돈까스",
    "짜장면 & 탕수육",
    "얼큰한 순대국밥",
    "모둠 초밥",
    "소고기 쌀국수",
    "수제버거 세트",
    "투움바 파스타",
    "돌솥 비빔밥",
    "떡볶이 & 모둠튀김",
    "치즈 닭갈비",
    "부대찌개",
    "바지락 칼국수",
]

# 버튼을 눌렀을 때 실행될 동작
if st.button("🎲 오늘의 메뉴 추천받기", type="primary"):
    # 리스트에서 무작위로 메뉴 1개 선택
    today_menu = random.choice(lunch_menus)

    # 화면에 결과 출력 및 축하 효과
    st.balloons()
    st.success(f"오늘의 추천 메뉴는 **{today_menu}**입니다! 맛있게 드세요 😋")
