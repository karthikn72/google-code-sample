"""A video playlist class."""

from .video_collection import VideoCollection


class Playlist(VideoCollection):
    """A class used to represent a Playlist."""

    def __init__(self):
        super().__init__()

