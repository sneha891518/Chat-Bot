from fastapi import Body
import requests
from decouple import config

ELEVEN_LABS_API_KEY=config("ELEVEN_LABS_API_KEY")

#Eleven Labs
#Convert Text to Speech



def convert_text_to_speech(message):

    #Define Data(Body)
    body={
        "text":message,
        "voice_settings":{
            "stability":0,
            "similarly_boost":0,
        } 
    }

#Define voice 
voice_kerry="21m00Tcm4TlvDq8ikWAM"


#Constructing Headers and Endpoint
headers={"xi-api-key":ELEVEN_LABS_API_KEY,"Content-Type":"application/json", "accept":"audio/mpeg"}
endpoint={"https://api.elevenlabs.io/v1/text-to-speech/{voice_kerry}"}

#Send request

try:
    response=requests.post(endpoint,json=Body,headers=headers)

except Exception as e:
    return


#Handle Response
if response.status_code==200:
    return response.content
else:
    return