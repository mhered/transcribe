import logging
import pytube
import whisper
import sys
import argparse
from utils import get_id_from_url


def transcribe_video(video_url: str = None, model: str = 'small'):
    """Generate a transcript from Youtube video"""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    if not video_url:
        logging.error("Please pass a YouTube url to transcribe")
        exit()

    logging.info("Downloading Whisper model")
    model = whisper.load_model(model)

    logging.info("Downloading the video from YouTube...")
    video = pytube.YouTube(video_url)

    logging.info("Extracting the audio...")
    audio = video.streams.get_audio_only()
    audio.download(filename='tmp.mp4')

    logging.info("Transcribing the audio...")
    result = model.transcribe('tmp.mp4')

    video_id = get_id_from_url(video_url)

    print(result["text"])
    with open(f"./transcripts/{video_id}.transcript") as outfile:
        outfile.write(result["text"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe a YouTube video using Whisper')

    parser.add_argument("--video", help="URL of the YouTube video to transcribe")
    parser.add_argument("--model", help="Whisper model to download and use", default="small")
    args = parser.parse_args()

    transcribe_video(args.video, args.model)
