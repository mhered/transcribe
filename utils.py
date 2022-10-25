import re


def get_id_from_url(video_url):
    """ Extract the video ID from the video url"""
    return re.findall("=(.+)$", video_url)[0]
