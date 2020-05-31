import speech_recognition as sr
import os
import random
import pygame

def speak(text):
    os.system(f'espeak -v "es" "{text}"')

def playSound(filename):
    pygame.mixer.music.load(f"frases_cortazar/{filename}.wav")
    pygame.mixer.music.play()

pygame.init()
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
for i, microphone_name in enumerate(mic_list): 
    device_id = i 

phrases = ["ah","claro","tremendo","posta"]# + ["mira_vos","si"]

with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    r.adjust_for_ambient_noise(source) 
    #r.energy_threshold = 4000 # hardcodeo lo que interpreto como un buen threshold
    while True:
        print("Te escucho")
        audio = r.listen(source)
        random.shuffle(phrases)
        playSound(phrases[0])
