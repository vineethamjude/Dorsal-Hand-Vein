import streamlit as st
from PIL import Image

def main():
    st.title("Image Input")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

if __name__ == "__main__":
    main()
