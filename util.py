import gTTS
import os
from mutagen.wave import WAVE

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks Joe!'

# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

def generate_audio_file_from_text(text, file_name, file_extention=".mp3", language="en", replace_older_file=False):
    file_name_already_exists = os.path.isfile(r"./" + file_name + file_extention)

    if file_name_already_exists and replace_older_file:
        os.remove(file_name + file_extention)
        file_name_already_exists = False

    if not file_name_already_exists:
        gTTS(text=text, lang=language, slow=False).save(file_name + file_extention)


def add_audio_to_video_from_text(scene, text, file_name, file_extention=".mp3", language="en", replace_older_file=False ,sync=True):
    generate_audio_file_from_text(text=text, file_name=file_name, file_extention=file_extention, language=language, replace_older_file=replace_older_file)

    scene.add_sound(file_name + file_extention)

    if sync:
        wait_time = WAVE(file_name + file_extention).info.length
        scene.wait(wait_time)