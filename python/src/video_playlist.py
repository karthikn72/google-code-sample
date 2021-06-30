"""A video playlist class."""

from .video_collection import VideoCollection


class Playlist(VideoCollection):
    """A class used to represent a Playlist."""

    def __init__(self, name):
        super().__init__()
        self._playlist_name = name

