import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime 

from function import headline_scraping
from function import preprocessing, make_corpus, model

# test url 
# https://n.news.naver.com/article/011/0004045478?cds=news_media_pc
# https://news.v.daum.net/v/20220422143418498
# https://sports.news.naver.com/news?oid=108&aid=0003047493

st.set_page_config(
    page_title = "뉴스 토픽 분류 AI 서비스",
    page_icon="🎈",
)

def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

# 나란히 열로 배치된 컨테이너 삽입 
# 나란히 배치된 여러 다중 요소 컨테이너를 삽입하고 컨테이너 개체 목록 반환
c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    st.title("🔑 뉴스 토픽 분류 AI 서비스")
    st.header("")

with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   *뉴스 토픽 분류 AI 서비스*는 당신의 뉴스를 7개의 토픽으로 분류해주는 서비스 입니다!
-   정치, 경제, 사회, 세계, 생활/문화, IT/과학, 스포츠 중 하나로 분류해줍니다🤗 
-   자연어 전처리 과정도 살펴봐주세요! 
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste News Link**")

with st.form(key="my_form"):

    input_url = st.text_area(
        "Paste your News Link below (Only naver news, daum news)",
        height=10
    )

    a = st.form_submit_button('Get your news Topic')

st.header("")
st.markdown("## **🎈 Check preprocessing & results**")

expander = st.expander("Result", expanded=True)
with expander:
    con = st.container() # 임의의 컨테이너를 만듬 
    con.write('''
    #### Step 1. 뉴스 제목 스크래핑
    ''')
    con_headline = con.empty()

    con.write('''
    #### Step 2. 자연어 전처리 
    ''')
    con_pre = con.empty()  

    con.write('''
    #### Step 3. 분류된 토픽은? 
    ''')
    con_model = con.empty()

    if a and len(input_url)!=0:

        ## 뉴스 URL에서 뉴스 헤드라인만 뽑아내기 
        headline = headline_scraping(input_url)

        ## 뉴스 헤드라인 페이지에 보여주기   
        con_headline.write(
            f'''
            ##### {str(headline)}
            '''
        )
        
        ## 전처리 적용하기 
        headline_aft_pre = make_corpus(headline)
        con_pre.write(
            f'''
            ##### {str(headline_aft_pre)}
            '''
        )
        
        # 모델 적용하기 
        headline_model = model(headline)
        con_model.write(
            f'''
            # {str(headline_model)}
            '''
        )