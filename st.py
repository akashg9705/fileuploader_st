import streamlit as st

st.set_page_config(page_title="Simple File Uploader")

st.title("📁 Simple File Uploader")

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["txt", "csv", "png", "jpg", "pdf"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    st.write("File details:")
    st.write("Name:", uploaded_file.name)
    st.write("Type:", uploaded_file.type)
    st.write("Size (bytes):", uploaded_file.size)

    if uploaded_file.type.startswith("text"):
        content = uploaded_file.read().decode("utf-8")
        st.text_area("File content", content, height=200)

