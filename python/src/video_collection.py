"""A video collection class."""

from .video import Video


class VideoCollection:
    """A class used to represent a Video Collection"""

    def __init__(self):
        self._videos = {}

    def add_video(self, video: Video):
        """Adds a video to the collection."""

        self._videos[video.video_id] = video

    def remove_video(self, video_id: Video.video_id):
        self._videos.pop(video_id, None)

    def clear(self):
        self._videos = {}

    def video_exists(self, video: Video) -> bool:
        return video.video_id in self._videos

    def get_all_videos(self):
        """Returns all available video information from the video collection."""

        return list(self._videos.values())


    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the video collection.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)
