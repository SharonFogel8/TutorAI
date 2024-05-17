import streamlit as st
from dotenv import load_dotenv
from modules import pdf_handler, text_processor, ui, generate_question
from modules import conversation_manager
from modules import buttons_actions
from modules.htmlTemplates import css, bot_template, user_template
import define


def main():
    print('main')
    load_dotenv()
    st.set_page_config(page_title="Study Buddy", page_icon=":books:")

    # ui.render_header()
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        print('conversation is none')
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        print('chat_history is none')
        st.session_state.chat_history = None
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = ui.get_uploaded_pdfs()
        buttons_actions.create_button(pdf_docs, button_name=define.PROCESS_BUTTON, func_click=buttons_actions.process_button_clicked)

    # if pdf_docs and is_process_button_clicked:
    #     with st.spinner("Processing"):
    #         raw_text = pdf_handler.extract_text_from_pdfs(pdf_docs)
    #         text_chunks = text_processor.split_text_into_chunks(raw_text)
    #         vectorstore = text_processor.create_vector_store(text_chunks)
    #         st.session_state.conversation = conversation_manager.init_conversation_chain(vectorstore)
    #     buttons_actions.summarized_clicked(vectorstore)
    #     buttons_actions.chat_clicked(vectorstore)
    #     buttons_actions.generate_question_clicked(vectorstore)

            # generate_question.generate_ques(raw_text)
            # user_question = ui.get_user_question_input()
            # if user_question:
            #     conversation_manager.handle_user_input(user_question, vectorstore)

    # if st.session_state[process_button_name] and ui.create_button("Generate Questions"):
    #     generate_question.generate_ques(raw_text)
    #
    # if st.session_state[process_button_name] and ui.create_button("Summarize"):
    #     user_question = "Summarize the files to half page"
    #     conversation_manager.handle_user_input(user_question, vectorstore)
    #
    # if st.session_state[process_button_name] and ui.create_button("QA"):
    #     user_question = ui.get_user_question_input()
    #     if user_question:
    #         conversation_manager.handle_user_input(user_question, vectorstore)

            # chat_button = st.button("Chat")
            # QA_button = st.button("QA")
            # summarize_button = st.button("Summeraize")

            # st.button("Chat", on_click=click_chat(vectorstore))
            # elif st.button("QA"):
            #     generate_question.generate_ques(raw_text)
            # elif st.button("Summeraize"):
            #     user_question = "Summarize the files to half page"
            #     conversation_manager.handle_user_input(user_question, vectorstore)
            # ui.show_options(click_chat, vectorstore)
        # if clicked_button is not None:
        #

            # if clicked_button["chat"]:
            #     st.write("chat")
            #     user_question = ui.get_user_question_input()
            #     if user_question:
            #         conversation_manager.handle_user_input(user_question, vectorstore)
            #     elif clicked_button["QA"]:
            #         generate_question.generate_ques(raw_text)
            #     elif clicked_button["summarize"]:
            #         user_question = "Summarize the files to half page"
            #         conversation_manager.handle_user_input(user_question, vectorstore)

def click_chat(vectorstore):
    st.session_state.chat = True
    user_question = ui.get_user_question_input()
    if user_question:
        with st.spinner("Processing"):
            conversation_manager.handle_user_input(user_question, vectorstore)

if __name__ == '__main__':
    main()
