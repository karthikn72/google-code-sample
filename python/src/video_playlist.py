"""A video playlist class."""

from .video_collection import VideoCollection


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name):
        self._playlist_name = name
        self._videos = VideoCollection()
