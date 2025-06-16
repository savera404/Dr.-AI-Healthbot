import streamlit as st
import tempfile

from brain import encode_img, analyze_img_n_query
from voice_doctor import text_2_speech
from voice_patient import speech_2_text


def inputs(audio_file_obj, image_file_obj):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(audio_file_obj.read())
        temp_audio_path = temp_audio.name
    speech_to_text=speech_2_text(temp_audio_path)
    if image_file_obj:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
            temp_image.write(image_file_obj.read())
            temp_image_path = temp_image.name
        encoded_img=encode_img(temp_image_path)
        doctor_res=analyze_img_n_query(encoded_img,speech_to_text)
    else:
        doctor_res="No image provided"
    doctor_voice=text_2_speech(doctor_res,output_filepath="doctor_response.mp3")
    
    return speech_to_text, doctor_res, doctor_voice



st.title("🧑‍⚕️ Dr. AI Healthbot")
st.header("Check Symptoms. Get Guidance. Stay Informed.")

patient_audio=st.audio_input("Record a voice message")
uploaded_image=st.file_uploader("Upload an image",type=["jpg", "jpeg", "png"] )

if patient_audio is not None and uploaded_image is not None:
    with st.spinner("Analyzing..."):
        patient_text, doctor_text, doctor_voice = inputs(patient_audio, uploaded_image)
        st.subheader("Patient (You):")
        st.markdown(
            f"""
            <div style="
                margin-bottom: 1rem;
                background-color: black;
                padding: 1rem;
                border-radius: 10px;
                font-family: 'Segoe UI', 'Roboto', sans-serif;
                font-size: 1rem;
                border: 1px solid red;
            ">
            {patient_text}
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image(uploaded_image)
        # st.code(patient_text, language='text' ,height=100)

        st.subheader("Dr.AI's Response:")
        st.markdown(
            f"""
            <div style="
                background-color: black;
                padding: 1rem;
                border-radius: 10px;
                font-family: 'Segoe UI', 'Roboto', sans-serif;
                font-size: 1rem;
                border: 1px solid red;
                margin-bottom: 1rem;
            ">
            {doctor_text}
            </div>
            """,
            unsafe_allow_html=True
        )
        #st.code(doctor_text, language='text', height=250)
        st.audio(doctor_voice)
else:
    st.info("Please record a voice message and upload an image to get started.")