
from gtts import gTTS

#set up text to speech with google text-to-speech
def text_2_speech(input_text, output_filepath):
    language='en'
    audio_obj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audio_obj.save(output_filepath)
    return output_filepath
# input_text="My name is Savera. What is your name?"
# output_filepath='testing_speech.mp3'
# text_2_speech(input_text=input_text,output_filepath=output_filepath)



### you may use elevenlabs isntead of gtts if you want custom voices, it is a better option but it has limited free credits###

#text to speech with elevenlabs
# import os
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY=os.environ.get('ELEVENLABS_API_KEY')

# def text_2_speech_11labs(text_input,output_filepath):
#     elevenlabs=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=elevenlabs.text_to_speech.convert(
#         text=text_input,
#         voice_id='XfNU2rGpBa01ckF309OY',
#         output_format='mp3_22050_32',
#         model_id='eleven_turbo_v2'
#     )
#     with open(output_filepath, 'wb') as f:
#         for chunk in audio:
#             f.write(chunk)
    
    # return output_filepath

#text_2_speech_11labs(text_input="this is an apple, i like apples, they say doctor a day keeps an apple away",output_filepath='testing_speech_11labs.mp3')

    

