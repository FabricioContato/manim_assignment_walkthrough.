from gtts import gTTS
import os
from mutagen.mp3 import MP3

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
        wait_time = int(MP3(file_name + file_extention).info.length)
        scene.wait(wait_time)

def add_parallel_audioTTS_with_animation(scene, animation, text, cue_word, file_name, file_extention=".mp3", language="en", replace_older_file=False):
    
    add_audio_to_video_from_text(scene=scene, text=text, file_name=file_name, file_extention=file_extention, language=language, replace_older_file=replace_older_file ,sync=False)

    if type(cue_word) is str and cue_word in text:
        cue_index = text.find(cue_word)
        partial_text = text[: cue_index + len(cue_word)]
        file_name_for_partial_text = 'cue_'+ cue_word + "_for_" + file_name
        generate_audio_file_from_text(text=partial_text, file_name=file_name_for_partial_text, file_extention=file_extention, language=language, replace_older_file=replace_older_file)
        wait_time = int(MP3(file_name_for_partial_text + file_extention).info.length) * .8
        scene.wait(wait_time)

    scene.play(animation)