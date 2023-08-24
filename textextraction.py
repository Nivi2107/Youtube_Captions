import argparse
from pytube import YouTube
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os 

# create a speech recognition object
r = sr.Recognizer()

# def download(video_url):
#     VIDEO_SAVE_DIRECTORY = "./videos"
#     video = YouTube(video_url)
#     video = video.streams.get_highest_resolution()
#     video.download(VIDEO_SAVE_DIRECTORY)

# def download_audio(video_url):
#     AUDIO_SAVE_DIRECTORY = "./audio"
#     video = YouTube(video_url)
#     audio = video.streams.filter(only_audio = True).first()
#     audio.download(AUDIO_SAVE_DIRECTORY)

# def extract_speech_text(video_url):
#     VIDEO_SAVE_DIRECTORY = "./video"
#     video = YouTube(video_url)
#     video = video.streams.get_highest_resolution()
#     video.download(VIDEO_SAVE_DIRECTORY, "vid.mp4")
#     video_file = mp.VideoFileClip("video/vid.mp4")
#     audio_file = video_file.audio
#     audio_file.write_audiofile( "aud.wav")
#     audio_file_path = "aud.wav"
#     chunk_duration_ms = 60000
#     # Load the audio file
#     audio = AudioSegment.from_file(audio_file_path)
#     # Calculate the number of chunks needed
#     num_chunks = len(audio) // chunk_duration_ms
#     # Create a directory to store the chunks
#     output_dir = os.path.splitext(audio_file_path)[0] + '_chunks'
#     os.makedirs(output_dir, exist_ok=True)
#     whole_text = ""
#     # Split the audio into chunks and save them
#     for i in range(num_chunks):
#         start_time = i * chunk_duration_ms
#         end_time = (i + 1) * chunk_duration_ms
#         chunk = audio[start_time:end_time]
#         chunk.export(f"{output_dir}/chunk_{i}.wav", format="wav")
#         with sr.AudioFile(f"{output_dir}/chunk_{i}.wav") as source:
#             audio_listened = r.record(source)
#             # try converting it to text
#             try:
#                 text = r.recognize_google(audio_listened)
#             except sr.UnknownValueError as e:
#                 print("Error:", str(e))
#             else:
#                 text = f"{text.capitalize()}. "
#                 # print(chunk_filename, ":", text)
#                 whole_text += text
#     # Handle the last chunk (if any)
#     last_chunk = audio[num_chunks * chunk_duration_ms:]
#     if len(last_chunk) > 0:
#         last_chunk.export(f"{output_dir}/chunk_{num_chunks}.wav", format="wav")
#         with sr.AudioFile(f"{output_dir}/chunk_{i}.wav") as source:
#             audio_listened = r.record(source)
#             # try converting it to text
#             try:
#                 text = r.recognize_google(audio_listened)
#             except sr.UnknownValueError as e:
#                 print("Error:", str(e))
#             else:
#                 text = f"{text.capitalize()}. "
#                 # print(chunk_filename, ":", text)
#                 whole_text += text
#     return whole_text

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from fpdf import FPDF

def download_youtube_captions(video_url):
    try:
        output_file = "text.srt"
        if "v=" in video_url:
            video_id = video_url.split("v=")[-1]
        else:
            video_id = video_url.split("tu.be/")[-1]
        captions = YouTubeTranscriptApi.get_transcript(video_id)

        if not captions:
            raise ValueError("No captions found for the specified video.")

        whole_text = ""
        with open(output_file, 'w', encoding='utf-8') as f:
            for caption in captions:
                text = f"{caption['start']} --> {caption['start'] + caption['duration']}\n\n"
                f.write(f"{caption['start']} --> {caption['start'] + caption['duration']}\n")
                whole_text += text
                text = f"{caption['text']}\n\n%"
                f.write(text)
                whole_text += text

        print(f"Captions downloaded successfully and saved to '{output_file}'.")

        return whole_text.split('%')

    except Exception as e:
        print(f"An error occurred: {e}")
    

def download_file():
    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)

    # open the text file in read mode
    f = open("text.srt", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x.encode("UTF-8"), ln = 1, align = 'C')

    # save the pdf with name .pdf
    pdf.output("captions.pdf")


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=VIDEO_ID"  # Replace with the YouTube video URL
    output_file = "captions.srt"

    download_youtube_captions(video_url, output_file)

# https://youtu.be/MWHN6ojlVXI

# https://www.youtube.com/watch?v=MWHN6ojlVXI