import streamlit as st
from generator import generate_qr, auto_detect_logo
import tempfile
import os


st.set_page_config(
    page_title="QR Code Generator",
    page_icon="favicon.png",
    layout="centered"
)


st.title("QR Code Generator")
st.write("Create custom QR codes with logos.")

st.divider()


# URL input
url = st.text_input(
    "🔗 Enter URL / Link",
    placeholder="https://example.com"
)


# Logo options
st.subheader("Logo Options")

logo_option = st.radio(
    "Choose logo",
    [
        "Auto Detect",
        "Custom Logo",
        "No Logo"
    ],
    horizontal=True
)


logo_path = None


# Auto detect
if logo_option == "Auto Detect":

    if url:
        detected_logo = auto_detect_logo(url)

        if detected_logo:
            logo_path = detected_logo
            st.success(f"Logo detected: {detected_logo}")
        else:
            st.info(
                "No predefined logo found. "
                "A website favicon will be tried."
            )


# Custom logo
elif logo_option == "Custom Logo":

    uploaded_logo = st.file_uploader(
        "Upload your logo",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_logo:

        temp_logo = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        temp_logo.write(uploaded_logo.getbuffer())
        temp_logo.close()

        logo_path = temp_logo.name

        st.image(
            uploaded_logo,
            caption="Uploaded Logo",
            width=120
        )


# Color
st.subheader("QR Code Color")

fill_color = st.color_picker(
    "Choose QR color",
    "#000000"
)


# Generate button
st.divider()

generate_button = st.button(
    "Generate QR Code",
    use_container_width=True
)


if generate_button:

    if not url.strip():
        st.error("Please enter a URL first.")

    else:

        try:

            with st.spinner("Generating QR Code..."):

                # Temporary output file
                output_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".png"
                )

                output_file.close()

                # Generate QR
                generate_qr(
                    url=url.strip(),
                    logo_path=logo_path,
                    fill_color=fill_color,
                    back_color="white",
                    save_as=output_file.name
                )

            st.success("QR Code generated successfully!")

            # Display QR
            st.image(
                output_file.name,
                caption="Your QR Code",
                width=350
            )


            # Download button
            with open(output_file.name, "rb") as file:

                st.download_button(
                    label="Download QR Code",
                    data=file,
                    file_name="qr_code.png",
                    mime="image/png",
                    use_container_width=True
                )


        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )