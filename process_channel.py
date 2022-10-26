import datetime
import json
from utils import get_id_from_url
import logging
import sys
import os
import time


def process_channel(json_file: str = "channel.json"):
    """ reads JSON file and resumes processing videos from file JSON"""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info("Reading JSON file...")
    with open(json_file, "r") as f:
        channel_dict = json.loads(f.read())

    # prioritize videos with most views not yet processed
    pending = sorted((video for video in channel_dict.values()
                     if not video['transcript']),
                     key=lambda d: d['views'],
                     reverse=True)

    """
    # prioritize latest videos not yet processed
    pending = sorted((video for video in channel_dict.values()
                     if not video['transcript']),
                     key=lambda d: strptime("%d/%m/%y",d['views']),
                     reverse=True)
    """

    logging.info(f"Found {len(pending)} videos pending processing")

    for video in pending:
        video_id = get_id_from_url(video['url'])
        out_dir = f"./captions/{video_id}/"
        logging.info(f"Processing {video_id} which has {video['views']} views: {video['title']}\n")

        os.system(f"yt_whisper {video['url']} --format srt --output_dir {out_dir}")
        time.sleep(.3)

        # check SRT file was saved in directory
        if os.path.exists(out_dir) and os.path.isdir(out_dir):
            if os.listdir(out_dir):
                channel_dict[video_id]['transcript'] = out_dir
                logging.info("Writing JSON...")
                # Serialize json
                channel_json = json.dumps(
                    channel_dict,
                    indent=4,
                    ensure_ascii=False)
                # Write to file
                with open(json_file, "w") as outfile:
                    outfile.write(channel_json)
            else:
                logging.info(f"yt_whisper failed, {out_dir} is empty")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Resumes processing videos from a JSON file')

    parser.add_argument(
        "--file",
        help="Name of the input file (Optional, default is channel.json)",
        default="channel.json")
    args = parser.parse_args()

    process_channel(args.file)

    # https://www.youtube.com/c/PythonEspa%C3%B1aOficial/videos
