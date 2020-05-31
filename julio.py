import speech_recognition as sr
import os
import unidecode
import pygame
import time

youtube_links = {
    # musica
        "miran":"https://www.youtube.com/watch?v=a3hOeU7w59o&list=RDEM6bg0Nft9_yagKJj18qs1Ig&start_radio=1",
        "triste":"https://youtu.be/mb-XCaA2HZs",
        "contento":"https://www.youtube.com/watch?v=nnxPZLtGACs",
        "animo":"https://www.youtube.com/watch?v=nnxPZLtGACs",
        "feliz":"https://www.youtube.com/watch?v=nnxPZLtGACs",
        "droga":"https://www.youtube.com/watch?v=Pw8ZESzpL3M",
        "colores":"https://www.youtube.com/watch?v=Pw8ZESzpL3M",
        "sexo":"https://www.youtube.com/watch?v=DyDfgMOUjCI",
        "trap":"https://youtu.be/b-WbKJJjetQ",
        "electro":"https://youtu.be/dX3k_QDnzHE",
        "adolescente":"https://youtu.be/pXRviuL6vMY",
        "kid":"https://youtu.be/fe4EK4HSPkI",
        # falopa
        "pokemon": "https://www.youtube.com/watch?v=uDIoEbbFKAY",
        "matata":"https://www.youtube.com/watch?v=nnxPZLtGACs",
        "digimon": "https://www.youtube.com/watch?v=EOuHn6eiyjI",
        "paco": "https://youtu.be/BdRbvvfiBwU",
        "selva": "https://youtu.be/Tnh_kPHp9LM",
        "blanco": "https://youtu.be/NA03yDnXNWc",
        # tranca
        "roman":"https://www.youtube.com/watch?v=jQi77xni1p8",
        "amor":"https://www.youtube.com/watch?v=jQi77xni1p8",
        "chica": "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "chil": "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "estudiar": "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "relaja": "https://www.youtube.com/watch?v=5qap5aO4i9A",
    # video
        "evolucion": "https://youtu.be/RZtZia4ZkX8",
        "arte": "https://youtu.be/NL0AkAIHSCE",
        "baile": "https://youtu.be/c-tW0CkvdDI",
        "danza": "https://youtu.be/c-tW0CkvdDI",
    # ambiental
        "prend": "https://www.youtube.com/watch?v=_Uie2r5wWxw",
        "lluvia": "https://www.youtube.com/watch?v=q76bMs-NwRk",
        "bosque": "https://www.youtube.com/watch?v=xNN7iTA57jM"
}

def playSound(filename):
    pygame.mixer.music.load(f"frases_cortazar/{filename}.wav")
    pygame.mixer.music.play()

pygame.init()

preguntas = ["cuando","como","por que", "porque", "quien","cuanto","quien","que"]

def play(youtube_link):
    pause()
    os.system(f"google-chrome {youtube_link}")
    time.sleep(3)
    full_screen()

def search(sentence):
    search_term = '+'.join(sentence.split())
    search_url = f"https://www.google.com/search?q={search_term}&oq={search_term}&aqs=chrome..69i57j46j0l5.2840j0j7&sourceid=chrome&ie=UTF-8"
    os.system(f"google-chrome {search_url}")

run_shortcut = 'xdotool search --sync --onlyvisible --class "google-chrome" windowactivate key'

def full_screen():
    os.system(f'{run_shortcut} F')

def pause():
    os.system(f'{run_shortcut} space')

def close_tab():
    os.system(f'{run_shortcut} ctrl+Q')

def next_video():
    os.system(f'{run_shortcut} shift+N')

def up_volume():
    os.system(f'{run_shortcut} Up+Up')
    time.sleep(2)
    os.system(f'{run_shortcut} Up+Up')
    time.sleep(2)
    os.system(f'{run_shortcut} Up+Up')
    time.sleep(2)
    os.system(f'{run_shortcut} Up+Up')
    time.sleep(2)
    os.system(f'{run_shortcut} Up+Up')

def down_volume():
    os.system(f'{run_shortcut} Down+Down')
    time.sleep(2)
    os.system(f'{run_shortcut} Down+Down')
    time.sleep(2)
    os.system(f'{run_shortcut} Down+Down')
    time.sleep(2)
    os.system(f'{run_shortcut} Down+Down')
    time.sleep(2)
    os.system(f'{run_shortcut} Down+Down')

commands = {
    "baja": down_volume,
    "subi": up_volume,
    "sube": up_volume,
    "cambia": next_video,
    "siguiente": next_video,
    "proxim": next_video,
    "pausa": pause,
    "para": pause,
    "completa": full_screen
}

def normalized_test(phrase):
    text = str(phrase)
    return unidecode.unidecode(text).lower()

def speak(text):
    os.system(f'espeak -v "es" "{text}"')

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()  
for i, microphone_name in enumerate(mic_list): 
    device_id = i 

with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    r.adjust_for_ambient_noise(source)
    #r.energy_threshold = 7000 # hardcodeo lo que interpreto como un buen threshold
    while True:
        print("Yo: Te escucho")
        audio = r.listen(source,snowboy_configuration=["snowboy",["snowboy/julio.pmdl"]])
        #audio = r.listen(source)
        #print(r.energy_threshold)
        print("Yo: Termine de escuchar")
        try:
            text = r.recognize_google(audio, language="es-ES")
            sentence = normalized_test(text)
            print("Vos: " + text)

            if "juli" in sentence:
                #speak("A ver ahi me fijo")
                playSound('ahi_me_fijo')

                for key_word in commands:
                    if key_word in sentence:
                        command = commands[key_word]
                        command()
                        break

                for key_word in youtube_links:
                    if key_word in sentence:
                        link = youtube_links[key_word]
                        play(link)
                        break

                #for pregunta in preguntas:
                #    if pregunta in sentence:
                #        search(sentence)

        except sr.UnknownValueError: 
            print("Google Speech Recognition no entendio nada")
            speak("No entendí naaaada, maaal ahí")
        except sr.RequestError as e: 
            print("No se pudo acceder a Google Speech Recognition; {0}".format(e)) 
            speak("No entendí naaaada, maaal ahí")