import streamlit as st

webtoon_list = ['랜덤채팅의 그녀!','홍시는 날 좋아해!','여신강림']

mwt1_categories = ['준우','태양']
mwt2_categories = ['견우','시호','태호','혜성']
mwt3_categories = ['서준','수호']

wwt1_categories = ['리라','성아','유리','하민']
wwt2_categories = ['가을','단아','순정']
wwt3_categories = ['주경']

st.set_page_config(
    page_title="Find Similar Webtoon-Character!"
)

st.write("## 안녕하세요!")
st.write("### 당신과 닮은 웹툰 캐릭터를 확인해보세요!")

st.markdown(
    """
    #### 사용방법
    - 왼쪽에서 성별에 맞게 접속해주세요.
    - 원하시는 사진 업로드 방식을 선택해주세요.
    - 선택한 방식대로 진행해주세요.
    - 당신과 닮은 캐릭터가 나옵니다.
    
    #### 주의사항
    - 직접 촬영 시, 바로 캠이 작동합니다. 놀라지마세요!
    - 과몰입NO! 재미로만 확인해주세요!
    - 아직 많은 웹툰들이 포함되어 있지 않아요!
"""
)

st.write("")

st.markdown(
    """
    #### 현재 추가되어 있는 웹툰
"""
)

tab1, tab2, tab3 = st.tabs([webtoon_list[0],webtoon_list[1],webtoon_list[2]])

with tab1:
    st.markdown(f"""#### {webtoon_list[0]}""")
    with st.expander("남자"):
        col1, col2, col3, col4 = st.columns(4)
        for i, m in enumerate(mwt1_categories):
            with globals()['col{}'.format(i+1)]:
                st.image("../faces/대표/남자/{}_대표.png".format(m), caption=m)
    with st.expander("여자"):
        col1, col2, col3, col4 = st.columns(4)
        for i, m in enumerate(wwt1_categories):
            with globals()['col{}'.format(i+1)]:
                st.image("../faces/대표/여자/{}_대표.png".format(m), caption=m)              

with tab2:
    st.markdown(f"""#### {webtoon_list[1]}""")
    with st.expander("남자"):
        col1, col2, col3, col4 = st.columns(4)
        for i, m in enumerate(mwt2_categories):
            with globals()['col{}'.format(i+1)]:
                st.image("../faces/대표/남자/{}_대표.png".format(m), caption=m)
    with st.expander("여자"):
        col1, col2, col3, col4 = st.columns(4)
        for i, m in enumerate(wwt2_categories):
            with globals()['col{}'.format(i+1)]:
                st.image("../faces/대표/여자/{}_대표.png".format(m), caption=m)                   
                
with tab3:
    st.markdown(f"""#### {webtoon_list[2]}""")
    with st.expander("남자"):
        col1, col2, col3, col4 = st.columns(4)
        for i, m in enumerate(mwt3_categories):
            with globals()['col{}'.format(i+1)]:
                st.image("../faces/대표/남자/{}_대표.png".format(m), caption=m)
    with st.expander("여자"):
        col1, col2, col3, col4 = st.columns(4)
        for i, m in enumerate(wwt3_categories):
            with globals()['col{}'.format(i+1)]:
                st.image("../faces/대표/여자/{}_대표.png".format(m), caption=m)      