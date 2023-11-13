# from dotenv import load_dotenv
# load_dotenv()
from langchain.chat_models import ChatOpenAI
import streamlit as st


# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은")
# print(result)
 
chat_model = ChatOpenAI()

st.title('귀엽고 멋진 김태연 시인')

content = st.text_input('시의 주제를 제시해주세요.')
st.write('시의 주제는', content)

if st.button('시 작성 해줘'):
    with st.spinner('시 작성 중...'):
        result = chat_model.predict(content+"에 대한 시를 써줘")
        st.write(result)
