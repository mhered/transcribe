from pytube import Channel
import datetime
import json
from utils import get_id_from_url
import logging
import sys


def scan_channel(channel_url: str = None, json_file: str = "channel.json"):
    """ updates JSON file with details of all videos in a channel"""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # create Channel object
    if not channel_url:
        logging.error("Please specify YouTube channel to scan")
        exit()

    logging.info("Scanning YouTube channel...")
    c = Channel(channel_url)
    num_videos = len(c.video_urls)
    logging.info(f"{num_videos} videos found in the channel.")
    logging.info("Building data structure...")

    # make a dict with video ID as key and a dict with main fields as values
    channel_dict = {}
    progress = last_progress = 0

    for video, video_url in zip(c.videos, c.video_urls):
        video_id = get_id_from_url(video_url)
        channel_dict[video_id] = {
            'url': video_url,
            'title': video.title,
            'published': video.publish_date.strftime("%d/%m/%y"),
            'views': video.views,
            'transcript': "",
            # 'description': video.description,
        }
        progress += 100/num_videos
        if progress-last_progress > 5:
            logging.info(f"{progress:.2f}% ...")
            last_progress = progress

    # Serialize json
    channel_json = json.dumps(
        channel_dict,
        indent=4,
        ensure_ascii=False)

    logging.info("Writing JSON...")
    # Write to file
    with open(json_file, "w") as outfile:
        outfile.write(channel_json)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Scan a YouTube channel and create a JSON file with contents')

    required_name = parser.add_argument_group('required named arguments')
    required_name.add_argument(
        "--channel",
        required=True,
        help="(Required) URL of the YouTube channel to scan")

    parser.add_argument(
        "--file",
        help="Name of the input file (Optional, default is 'channel.json')",
        default="channel.json")
    args = parser.parse_args()

    scan_channel(args.channel, args.file)

    # https://www.youtube.com/c/PythonEspa%C3%B1aOficial/videos
