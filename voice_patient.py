
import os
from groq import Groq


### use this code if you are not using streamlit, otherwise it is not needed as streamlit handles audio input###

#first install portaudio and ffmpeg globally

# import logging
# import speech_recognition as sr
# from pydub import AudioSegment
# from io import BytesIO

# logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s - %(message)s')

# def record_audio(file_path, timeout=20, phrase_time_limit=60):
#     """
#     Args:
#     filepath= where to save recorded audio file
#     timeout=maximum time for phrase to start, in s
#     phrase_time_limit=maximum length of audio allowed
#     """

#     #processes and store the audio
#     recognizer=sr.Recognizer()

#     try:
#         with sr.Microphone() as source:
#             logging.info("Checkong for bg noise")
#             recognizer.adjust_for_ambient_noise(source,duration=1)
#             logging.info("Start speaking now")

#             #record the audio
#             audio_data=recognizer.listen(source,timeout=timeout, phrase_time_limit=phrase_time_limit)
#             logging.info("recording complete")

#             #convert the recorded audio 
#             wav_data=audio_data.get_wav_data()
#             audio_segment=AudioSegment.from_wav(BytesIO(wav_data))
#             audio_segment.export(file_path, format="mp3", bitrate="128K")

#             logging.info(f"Audio saved at {file_path}")



#     except Exception as e:
#         logging.error(f"Error occured: {e}")

# audio_file_path="testing_voice.mp3"
# record_audio(file_path=audio_file_path)


#set up speech to text llm
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
def speech_2_text(audio_file_path):
    client=Groq()
    model='whisper-large-v3'
    audio_file=open(audio_file_path,'rb')
    transcription=client.audio.transcriptions.create(
        model=model,
        file=audio_file,
        language='en'
    )

    return transcription.text
