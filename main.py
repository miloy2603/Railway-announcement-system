import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def wordToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language)
    myobj.save(filename)

# This function returns pydubs audiosegment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    #1.Generate Kripya dhyan dijiye
    start = 88000
    finished = 90200
    audioProcessed = audio[start:finished]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from city

    #3 - Generate se chalkar
    start = 91000
    finished = 92200
    audioProcessed = audio[start:finished]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 Generate ke raaste
    start = 94000
    finished = 95000
    audioProcessed = audio[start:finished]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 Generate ko jaane wali gaadi sankhya
    start = 96000
    finished = 98900
    audioProcessed = audio[start:finished]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train number no and name

    # 9 Generate kuch hi samay mei platform sankhya
    start = 105500
    finished = 108200
    audioProcessed = audio[start:finished]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 Generate par aa rahi hai
    start = 109000
    finished = 112250
    audioProcessed = audio[start:finished]
    audioProcessed.export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from city
        wordToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        wordToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
        wordToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train number no and name
        wordToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        wordToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{item['train_name']}.mp3", format="mp3")

if __name__ == '__main__':
    print("Generating.....")
    generateSkeleton()
    print("Now Generating Announcement....")
    generateAnnouncement("announce_hindi.xlsx")
