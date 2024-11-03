import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='나야 불량품 조', layout="wide", page_icon='😱')

# Sidebar menu setup
with st.sidebar:
    st.title("목록")
    sidebar_option = option_menu(
        "main",
        ['분석 목표와 과정', '모델 도출', '최종 결과'],
        icons=['house', 'kanban', 'bi bi-robot'],
        menu_icon="app-indicator",
        default_index=0,
        styles={
            "container": {"padding": "4!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#08c7b4"},
        }
    )

# Header and project info
st.header('우리조의 4주차 프로젝트를 소개합니다!')

# Define image paths for each tab
tab1_images = [f'images/{i}.jpg' for i in range(2, 11)]  # 2~10.jpg
tab2_images = [f'images/{i}.jpg' for i in range(11, 21)]  # 11~20.jpg
tab3_images = [f'images/{i}.jpg' for i in range(21, 31)]  # 21~30.jpg

# Display images based on sidebar selection
if sidebar_option == '분석 목표와 과정':
    st.info("""코딩 금쪽이들의 험난한 데이터 분석 모험기""")
    st.image("images/1.jpg", caption="첫 장", use_column_width=True)
    tab1, tab2, tab3 = st.tabs(["1", "2", "3"])


    with tab1:
        st.header("분석 목표 및 계획")
        st.image(tab1_images, caption=[f"이미지 {i}" for i in range(2, 11)], use_column_width=True)

    with tab2:
        st.header("EDA")
        st.image(tab2_images, caption=[f"이미지 {i}" for i in range(11, 21)], use_column_width=True)

    with tab3:
        st.header("전처리")
        st.image(tab3_images, caption=[f"이미지 {i}" for i in range(21, 31)], use_column_width=True)

elif sidebar_option == '모델 도출':
    images = ['images/31.jpg', 'images/32.jpg', 'images/40.jpg', 'images/41.jpg']
    st.image(images, caption=["모델 이미지 1", "모델 이미지 2", "모델 이미지 3","모델 이미지 4"], use_column_width=True)

elif sidebar_option == '최종 결과':
    images = ['images/33.jpg', 'images/34.jpg', 'images/35.jpg','images/36.jpg','images/37.jpg']
    st.image(images, caption=["결과 이미지 1", "결과 이미지 2", "결과 이미지 3", "결과 이미지 4", "결과 이미지 5"], use_column_width=True)

