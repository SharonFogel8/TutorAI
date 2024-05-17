import streamlit as st
import define

def render_header():
    st.markdown("<h1 style='text-align: center; color: black;'>Study Buddy</h1>", unsafe_allow_html=True)
    st.header("Study Buddy :books:")

def get_user_question_input():
    return st.text_input("Ask a question about your documents:")

def get_uploaded_pdfs():
    return st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)



def show_options(func_click_chat, vectorstore):
    if 'chat' not in st.session_state:
        st.session_state.chat = False
    st.button("chat", on_click=func_click_chat(vectorstore))

    # clicked_button = {}
    # for option in define.OPTIONS.keys():
    #     clicked_button[option] = st.button(define.OPTIONS[option], on_click=funcr, args=(a,d))
    # return clicked_button

