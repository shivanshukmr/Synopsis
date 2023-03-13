import requests 
import hashlib
import os 


import yt_dlp
import magic

def is_json(request):
    return request.headers.get('Content-Type') == 'application/json'

def get_path(url):
    return str(hashlib.sha256(url.encode("utf-8")).hexdigest())

#private function to check valid file to be processed
def _is_valid_file(path):
    valid_mime = ("text/plain",
                  "video/mp4",
                  "video/webm",
                  "audio/webm",
                  "audio/mp3",
                  "audio/mpeg")

    if os.path.isfile(path):
        return get_filetype(path) in valid_mime

    return None
        





#to download file from web 
def download_audio(url):
    print("DOwnwloading file.....")
    file_name = get_path(url)
    ydl_opts = {'format': 'worstaudio',
    "outtmpl": f"{file_name}",
    'postprocessors': [{ 
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
        if error_code:
            return False
    return file_name+".mp3"

#function to give file mime type
def get_filetype(path):
    if os.path.isfile(path):
        return magic.from_file(path,mime=True)
    return None 


#function to check whether is processable file 
def is_valid_filetype(path):
    return os.path.isfile(path) and _is_valid_file(path)


