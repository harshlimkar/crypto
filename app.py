import streamlit as st
from PIL import Image
import io
from modules.crypto_utils import encrypt_message, decrypt_message
from modules.stego_utils import embed_data, extract_data

st.set_page_config(page_title="Secure Communication System", layout="wide")

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("<h1>🔐 Multi-Layer Secure Communication System</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "🔐 Encrypt & Hide",
    "🔓 Extract & Decrypt",
    "📊 About"
])

# ================= ENCRYPT =================
with tab1:
    st.markdown("## Encrypt & Hide Confidential Message")

    col1, col2 = st.columns([1,1], gap="large")

    with col1:
        message = st.text_area(
            "Secret Message",
            height=150,
            label_visibility="collapsed"
        )

        image_file = st.file_uploader(
            "Upload PNG Image",
            type=["png"],
            label_visibility="collapsed"
        )

    with col2:
        st.markdown("""
        ### 🔒 Security Layers
        ✔ AES-256 Encryption  
        ✔ SHA-256 Integrity  
        ✔ LSB Steganography  
        ✔ Multi-Layer Defense  
        """)

    if st.button("🚀 Encrypt & Generate Secure Image"):
        if message and image_file:
            image = Image.open(image_file)

            payload_json, payload = encrypt_message(message)
            stego_image = embed_data(image, payload_json)

            st.markdown("---")
            st.subheader("Encryption Output")

            with st.expander("View Encryption Details"):
                st.json(payload)

            st.image(stego_image, caption="Generated Secure Stego Image")

            buf = io.BytesIO()
            stego_image.save(buf, format="PNG")

            st.download_button(
                "⬇ Download Secure Image",
                buf.getvalue(),
                file_name="secure_stego_image.png",
                mime="image/png"
            )
        else:
            st.warning("Please enter message and upload image.")

# ================= DECRYPT =================
with tab2:
    st.markdown("## Extract & Decrypt Hidden Message")

    image_file = st.file_uploader(
        "Upload Stego Image",
        type=["png"],
        label_visibility="collapsed"
    )

    if st.button("🔍 Extract & Decrypt"):
        if image_file:
            image = Image.open(image_file)

            extracted_payload = extract_data(image)
            decrypted_message, integrity = decrypt_message(extracted_payload)

            st.markdown("---")

            with st.expander("View Extracted Payload"):
                st.code(extracted_payload)

            if integrity:
                st.success("Integrity Verified Successfully ✅")
                st.subheader("Decrypted Message")
                st.write(decrypted_message)
            else:
                st.error("Integrity Check Failed ❌ Image may be tampered.")
        else:
            st.warning("Please upload a stego image.")

# ================= ABOUT =================
with tab3:
    st.markdown("## About This System")

    st.markdown("""
    ### Multi-Layer Security Architecture

    This system follows a Defense-in-Depth model:

    1️⃣ AES-256 for Confidentiality  
    2️⃣ SHA-256 for Integrity Verification  
    3️⃣ LSB Steganography for Covert Communication  

    ### Objective

    To securely transmit confidential information
    using encryption and image-based concealment.
    """)
