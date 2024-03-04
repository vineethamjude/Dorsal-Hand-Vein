import streamlit as st
st.title('First project')

import streamlit as st

def main():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Logged in as {}".format(username))
            # You can redirect to another page or perform any action here after successful login
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()
