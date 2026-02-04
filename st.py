import streamlit as st

st.set_page_config(page_title="Simple File Uploader")

st.title("📁 Simple File Uploader")

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["txt", "csv", "png", "jpg", "pdf"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    st.write("### File details")
    st.write("**Name:**", uploaded_file.name)
    st.write("**Type:**", uploaded_file.type)
    st.write("**Size (bytes):**", uploaded_file.size)

    # ----- TEXT FILE HANDLING -----
    if uploaded_file.type.startswith("text") or uploaded_file.name.endswith(".txt"):
        try:
            file_bytes = uploaded_file.read()
            text = file_bytes.decode("utf-8")

            st.write("### File content")
            st.text_area(
                label="Text inside the file",
                value=text,
                height=300
            )

        except Exception as e:
            st.error("Unable to read this file as text.")
