import streamlit as st
from dotenv import load_dotenv
from modules import buttons_actions

def callback():
    print("callback")
    st.button("gen", on_click=generate)
    with st.spinner("Processing"):
        st.text("lalala")



# def create_button(button_name):
#     st.session_state[button_name] = False
#     st.button(button_name, on_click=callback, args = (button_name))

def main():
    # print(st.session_state.click)
    print("main")
    # load_dotenv()
    # st.set_page_config(page_title="Study Buddy", page_icon=":books:")
    #
    # pros_but = st.button("button_name", on_click=callback)
    # print(st.session_state)
    # if pros_but:
    #     with st.spinner("Processing"):
    #         st.text("lalala")
    # if pros_but:
    #     if st.button("generate"):
    #         st.session_state.gen = True
    #         print(st.session_state)
    #         generate()
    load_dotenv()
    st.set_page_config(page_title="Study Buddy", page_icon=":books:")
    buttons_actions.create_button("fdfdf", button_name='lala', func_click=lala)
    # st.button("button_name", on_click=callback)

    # if st.session_state.keys().__contains__("click") and st.session_state.click == True:
    #     callback()
    # print(st.session_state.items())

def lala(arg):
    print(arg)

def generate():
    st.button("gen", on_click=generate)
    st.balloons()

if __name__ == '__main__':
    main()
