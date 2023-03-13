import openai
from libs import constant
from libs import utils
from libs.utils import get_path
import os

openai.api_key = constant.OPENAI_KEY


import time


def get_transcript(url):
    file_name = get_path(url)
    if os.path.exists(file_name + ".txt"):
        return open(file_name + ".txt").read()

    path = utils.download_audio(url)
    if utils.is_valid_filetype(path):
        print("Transcribing file.....")
        audio_file = open(path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file, language="en")
        open(path + ".txt", "w").write(transcript["text"])
        return transcript["text"]
    return None
