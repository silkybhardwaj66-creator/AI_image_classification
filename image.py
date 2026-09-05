import streamlit as st
import google.generativeai as genai
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart Vehicle Inspection",
    page_icon="🥻",
    layout="wide"
)

st.title(" Smart Vehicle Inspection")
st.write("Upload a image and get insights using Gemini 2.5 Flash.")

# -----------------------------
# Gemini API Configuration
# -----------------------------
GOOGLE_API_KEY = "AQ.Ab8RN6KjWXbb_gL4LdUNsFo3ZHlj2ioBf6U7Iox67Xfe87yRaA"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")

# -----------------------------
# Image Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Analyze Button
# -----------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with col2:

        if st.button("Analyze Image"):

           with st.spinner("Analyzing image..."):

                prompt = """
                You are an AI visual vehicle-inspection assistant.

                Analyze the uploaded vehicle image and identify visible exterior damage.

                Your analysis must be limited to what can be observed from the image.

                Identify:

                1. Vehicle type
                2. Visible body components
                3. Scratches
                4. Dents
                5. Cracks
                6. Broken components
                7. Paint damage
                8. Misalignment that is visibly apparent
                9. Approximate location of each issue
                10. Apparent severity

                Severity categories:
                - Minor
                - Moderate
                - Severe
                - Cannot determine

                Also identify:
                11. Components that may require professional inspection
                12. Potential safety concerns visible from the image

                OUTPUT FORMAT:

                ## 🚗 Vehicle
                ...

                ## 🔍 Visible Damage

                | Area | Damage Type | Severity
                | Evidence |
                |---|---|---|---|
                | | | | |

                ## ⚠️ Potential Safety Concerns
                - ...

                ## 🔧 Areas Requiring Inspection
                - ...

                ## 📋 Overall Visual Assessment
                ...

                IMPORTANT:
                Do not provide a definitive mechanical diagnosis.
                Do not estimate repair costs.
                Do not claim hidden damage.
                Only describe visible evidence.

                Provide practical styling suggestions while clearly basing your observations only on what is visible in the image.
                """

                response = model.generate_content(
                    [prompt, image]
                )

                st.subheader("Analysis Result")
                st.write(response.text)
