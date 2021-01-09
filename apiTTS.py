from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from datetime import datetime

"""
The issue may be with the newest version of PyJWT package (2.0.0). 
use 'pip install PyJWT==1.7.1' to downgrade to the previous version
"""

day = int(datetime.now().day)
final = "INSERT_WHAT_TO_SAY_HERE"

if day < 8:
    key = 'svYg5IbwDaMBzqiXBMzbsKMQblbBraUB9faSeGUko3Xf'
elif day < 15:
    key = ""
elif day < 22:
    key = ""
else:
    key = ""

authenticator = IAMAuthenticator(key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(
    'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/2c2cf7f1-d6e8-49fa-a190-d50445c7de67')

with open('test2.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            final,
            voice='en-GB_JamesV3Voice',
            accept='audio/wav'
        ).get_result().content)
