from gtts import gTTS
import os
from mutagen.mp3 import MP3

video_audio_relative_path = r"./util_audio/video_audio/"
cue_audio_relative_path = r"./util_audio/cue_audio/"
if not os.path.exists(video_audio_relative_path):
    os.makedirs(video_audio_relative_path)

if not os.path.exists(cue_audio_relative_path):
    os.makedirs(cue_audio_relative_path)

def cue_time_calculator(text, cue_word, language="en", replace_older_file=False):
    if type(cue_word) is str and cue_word in text:
        cue_index = text.find(cue_word)
        partial_text = text[: cue_index + len(cue_word)]
        file_name_for_partial_text = 'cue_'+ cue_word + "_for_" + text[: len(text)//2]
        generate_audio_file_from_text(text=partial_text, file_path=cue_audio_relative_path ,file_name=file_name_for_partial_text, language=language, replace_older_file=replace_older_file)
        cue_time = int(MP3(cue_audio_relative_path + file_name_for_partial_text + ".mp3").info.length) * .8
        return cue_time
    
    else:
        return 0

def generate_audio_file_from_text(text, file_name, file_path ,file_extention=".mp3", language="en", replace_older_file=False):
    file_name_already_exists = os.path.isfile(file_path + file_name + file_extention)

    if file_name_already_exists and replace_older_file:
        os.remove(file_path + file_name + file_extention)
        file_name_already_exists = False

    if not file_name_already_exists:
        gTTS(text=text, lang=language, slow=False).save(file_path + file_name + file_extention)

def add_audio_to_video_from_text(scene, text, file_name, file_extention=".mp3", cue_word=None, language="en", replace_older_file=False ,sync=True):
    generate_audio_file_from_text(text=text, file_path=video_audio_relative_path ,file_name=file_name, file_extention=file_extention, language=language, replace_older_file=replace_older_file)

    scene.add_sound(video_audio_relative_path + file_name + file_extention)

    audio_time = int(MP3(video_audio_relative_path + file_name + file_extention).info.length)
    if sync:
        scene.wait(audio_time)
    
    cue_time = cue_time_calculator(text=text, cue_word=cue_word, language=language, replace_older_file=replace_older_file)

    remaning_time_after_cue = audio_time - cue_time

    return audio_time, cue_time, remaning_time_after_cue