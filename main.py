import speech_recognition as sr
import webbrowser
from time import ctime
import time
import sys
import playsound
import os
import random
import pywhatkit
from gtts import gTTS

r=sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            luci_speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
        
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            luci_speak('Sorry, I did not get that')
        except sr.RequestError:
            luci_speak('Sorry, my speech service is down')
        return voice_data
def luci_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'your name' in voice_data:
        luci_speak('My name is Luci')

    if 'what day is it' in voice_data:
        luci_speak(ctime()) 

    if ' music on youtube' in voice_data:
        searchmusic=record_audio('What do u want to listen to')    
        pywhatkit.playonyt(searchmusic) 
        
        luci_speak('Playing '+searchmusic)
    if 'search' in voice_data:
        search=record_audio('What do u want to search for')    
        url='https://www.youtube.com/results?search_query='+search
        webbrowser.get().open(url)
        luci_speak('Here is what i found for'+search)
    if 'find location' in voice_data:
        location=record_audio('What location do u wanna find')    
        url='https://www.google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        luci_speak('Here is the location of'+location)
    if 'terminate' in voice_data:
        sys.exit()
    if 'i miss vodka' in voice_data:
        luci_speak('i miss it too buddy')
        os.startfile("russian.mp3")
    if 'you pass butter' in voice_data:
        luci_speak('oh my god')




time.sleep(1)    

while 1:
    luci_speak('How may i help you?')
    voice_data=(record_audio()).lower()
    print('                                                                Kaytho: '+voice_data)
    respond(voice_data)
    