import streamlit as st
import define
from modules import conversation_manager
from modules import ui
from modules import pdf_handler, text_processor, generate_question

def create_button(*args, button_name: str, func_click):
    st.button(button_name, on_click=func_click, args=args)

def summarized_clicked(vectorstore):
    create_button(vectorstore, button_name=define.SUMMARIZE_BUTTON, func_click=summarized_clicked)
    st.session_state['user_input'] = "Summarize the files to half page"
    st.session_state.conversation = conversation_manager.get_conversation_chain(vectorstore)
    conversation_manager.handle_user_input()

def chat_clicked(vectorstore):
    create_button(vectorstore, button_name=define.CHAT_BUTTON, func_click=chat_clicked)
    st.write("Chat")
    st.session_state.conversation = conversation_manager.get_conversation_chain(vectorstore)
    init_user_question_input()

def generate_question_clicked(vectorstore, raw_text):
    create_button(vectorstore, button_name=define.GENERATE_QUESTION_BUTTON, func_click=generate_question_clicked)
    generate_question.generate_ques(raw_text)

def process_button_clicked(pdf_docs):
    with st.spinner("Processing"):
        raw_text = pdf_handler.extract_text_from_pdfs(pdf_docs)
        text_chunks = text_processor.split_text_into_chunks(raw_text)
        vectorstore = text_processor.create_vector_store(text_chunks)
    create_button(vectorstore, button_name=define.SUMMARIZE_BUTTON, func_click=summarized_clicked)
    create_button(vectorstore, button_name=define.CHAT_BUTTON, func_click=chat_clicked)
    create_button(vectorstore, raw_text, button_name=define.GENERATE_QUESTION_BUTTON, func_click=generate_question_clicked)

def get_user_question():
    conversation_manager.handle_user_input()
    init_user_question_input()


def init_user_question_input():
    st.text_input("Ask a question about your documents:", on_change=get_user_question, key="user_input")