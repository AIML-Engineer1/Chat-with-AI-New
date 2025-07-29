import streamlit as st

from translator_config import SENTENCE

IMAGE_ADDRESS = "https://legalaid.bc.ca/sites/default/files/2023-09/LAN%20Graphic%201.png"

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False
    

if not st.session_state.logged_in:

    username = st.text_input("Username")

    password = st.text_input("Password", type="password")

    if st.button("Log In"):

        if username == "admin" and password == "password123":

            st.session_state.logged_in = True

        else:

            st.error("Invalid credentials")

if st.session_state.logged_in:

    st.success("You are logged in!")

    # Show your app content here

if 'lang' not in st.session_state:
    st.session_state.lang = "en"

with st.sidebar:
    option = st.selectbox(
            SENTENCE["sent6"][st.session_state.lang],
            ("English", "Spanish"),
            placeholder=SENTENCE["sent7"][st.session_state.lang],
            index = None
        )
    # else select language
    if option == "English":
        st.session_state.lang = "en"
        st.rerun()
    elif option == "Spanish":
        st.session_state.lang = "sp"
        st.rerun()

# Home page
st.title(SENTENCE["sent1"][st.session_state.lang])
st.subheader(SENTENCE["sent2"][st.session_state.lang])
st.write(SENTENCE["sent3"][st.session_state.lang])

# Add a coral reef image
st.image(IMAGE_ADDRESS)

redirect_uri = "http://localhost:8501/oauth2callback"

cookie_secret = "abcde12345"

client_id = "493520145160-42ua5asc6tpqa94p479tj3iohjbv4jf2.apps.googleusercontent.com"

client_secret = "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"

server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

OPENAI_API_KEY="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"

PINECONE_API_KEY="pcsk_46NVQq_DgxhugvATtVunv2dmczroFYtzCNUK1gnejoZvqQyTCUtUgYmeFfYVPyJ9xZKmQn"

INDEX_HOST="https://rag-8nasclb.svc.aped-4627-b74a.pinecone.io"

if not st.experimental_user.is_logged_in:
    print(st.session_state.lang)
    if st.sidebar.button(SENTENCE["sent4"][st.session_state.lang], type="primary", icon=":material/login:"):
        st.login()
else:
    if st.sidebar.button(SENTENCE["sent5"][st.session_state.lang], type="secondary", icon=":material/logout:"):
        st.logout()
        st.stop()
