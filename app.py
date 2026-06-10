# 스트림릿
import streamlit as st

# 제목 출력
st.write('Hello, Title!')

# 마크다운
st.markdown('''
            # Hello, Markdown!
            1. 항목
            - **중요한 내용**
            ''')

# 사이드바
menu = st.sidebar.selectbox(
    "메뉴 선택",
 ["홈", "회원관리", "설정"]
)

# 탭
tab1, tab2, tab3 = st.tabs(["메뉴1", "메뉴2", "메뉴3"])
## 리턴 값이 3개인 이유는 탭이 3개이기 때문입니다.
## 변수 3개에 각각 탭이 할당됩니다.

with tab1:
    st.write("첫 번째 탭입니다.")
    with st.expander("자세히 보기"):
        st.write("숨겨진 내용입니다.")

with tab2:
    st.write("두 번째 탭입니다.")
    a = st.selectbox("기능", ["복사하기", "붙여넣기", "잘라내기"])
    st.write(f"선택한 기능: {a}")
    # st.write로 선택한 기능을 출력합니다.

with tab3:
    st.write("세 번째 탭입니다.")

    # 버튼을 클릭하면 아무런 동작도 하지 않습니다.  
    if st.button("버튼"):
        st.write("버튼이 클릭되었습니다.")
    # 버튼을 클릭하면 "버튼이 클릭되었습니다."라는 메시지가 출력됩니다.